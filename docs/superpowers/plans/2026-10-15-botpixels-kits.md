# botpixels Kits Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate Clawd's 65 pixel poses for four more characters (Grok Bot, Gemini, Antigravity, ElevenLabs) from one command, with Clawd's own output unchanged.

**Architecture:** Clawd's pose code stays untouched. Each other character's pose is derived from Clawd's finished SVG by string surgery: swap the body path for the character's grid path, drop Clawd-orange limb groups, recolour remaining Clawd orange. A small `botpixels/` package holds the grid maths, the character table, and the derivation; `generate_icons.py` only gains a `main()` that writes every kit.

**Tech Stack:** Python 3 standard library only (`re`, `dataclasses`, `os`, `unittest`, `xml.etree`, `tempfile`). No new dependencies.

**Spec:** `docs/superpowers/specs/2026-10-15-botpixels-design.md`

## Global Constraints

- Every path below is relative to the repo root.
- Standard library only. No pip installs. Python 3.10 or newer (uses `str | None` and `str.removeprefix`).
- Clawd output (`icons/`, 65 poses + `clawd.svg` + `preview.html`) must stay byte-identical to upstream commit cb073fb.
- Grids are 24 columns, 1 to 16 rows, characters `#`, `o`, `.` only, at least one `#`.
- Grids are bottom-aligned so the last row ends on Clawd's feet line, unit y = 20 (first row at y = 20 - rows).
- Clawd orange is `#D97757`. It must not appear in any file under `kits/`.
- Non-Clawd characters drop the Clawd-orange limb groups in dance, run and wave; success's one orange confetti is recoloured to the body colour.
- Non-Clawd outputs go to `kits/<id>/` named `<id>_<pose>.svg`, plus `<id>.svg` and `preview.html`.
- Base icons use `translate(16,14) scale(4)`.
- Run tests from the repo root with `python3 -m unittest -v`.
- Executor rule: the Cursor agent writes code and never runs shell commands, tests, or git. Claude runs tests and commits.

## Review Focus

1. Running the script from a directory other than the repo root must still write into the repo, not into the caller's directory. Pinned in Task 3 by `test_root_is_script_dir`.
2. Running the generator twice must produce identical bytes. Pinned in Task 3 by `test_rerun_is_idempotent`.
3. Every image a kit's preview page links to must exist in that kit. Pinned in Task 3 by `test_preview_links_resolve`.
4. The run pose rotates and shrinks the body; its derived version must still swap the body, so Clawd's path string must appear in no kit file. Pinned in Task 3 by `test_no_clawd_path_in_kits`.
5. A grid row with a trailing space or tab, as happens when editing by hand, must fail validation, not draw a shifted character. Pinned in Task 1 by `test_rejects_trailing_space`.

---

### Task 1: Grid maths

**Files:**
- Create: `botpixels/__init__.py` (empty)
- Create: `botpixels/grid.py`
- Create: `tests/__init__.py` (empty)
- Test: `tests/test_grid.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `class GridError(ValueError)`
  - `validate_grid(rows: list[str], mascot_id: str) -> None` raises `GridError` whose message starts with `"<mascot_id>: "` and names the 1-based row when a row is at fault.
  - `runs_to_path(rows: list[str], char: str, y0: int) -> str`
  - `body_path(rows: list[str]) -> str` (runs of `#`, y0 = 20 - len(rows))
  - `eye_path(rows: list[str]) -> str` (runs of `o`, same y0; `""` if none)

- [ ] **Step 1: Write the failing tests** in `tests/test_grid.py`

```python
import unittest

from botpixels.grid import GridError, body_path, eye_path, runs_to_path, validate_grid

ROW = "." * 10 + "#" * 4 + "." * 10  # 24 wide


class RunsToPath(unittest.TestCase):
    def test_known_grid(self):
        self.assertEqual(
            runs_to_path(["##..#", ".###."], "#", 4),
            "M0 4h2v1h-2zM4 4h1v1h-1zM1 5h3v1h-3z",
        )

    def test_body_is_bottom_aligned(self):
        rows = [ROW] * 16
        self.assertTrue(body_path(rows).startswith("M10 4h4v1h-4z"))
        self.assertTrue(body_path([ROW] * 15).startswith("M10 5h4v1h-4z"))

    def test_eye_path_empty_without_eyes(self):
        self.assertEqual(eye_path([ROW]), "")

    def test_eye_cells_left_out_of_body(self):
        rows = ["." * 10 + "#o##" + "." * 10]
        self.assertEqual(body_path(rows), "M10 19h1v1h-1zM12 19h2v1h-2z")
        self.assertEqual(eye_path(rows), "M11 19h1v1h-1z")


class Validate(unittest.TestCase):
    def test_accepts_good_grid(self):
        validate_grid([ROW] * 16, "ok")

    def test_rejects_ragged_row(self):
        with self.assertRaisesRegex(GridError, r"^bad: row 2"):
            validate_grid([ROW, ROW + "."], "bad")

    def test_rejects_unknown_character(self):
        with self.assertRaisesRegex(GridError, r"^bad: row 1"):
            validate_grid([ROW.replace(".", "x", 1)], "bad")

    def test_rejects_trailing_space(self):
        with self.assertRaisesRegex(GridError, r"^bad: row 1"):
            validate_grid([ROW[:-1] + " "], "bad")

    def test_rejects_too_many_rows(self):
        with self.assertRaisesRegex(GridError, r"^bad: "):
            validate_grid([ROW] * 17, "bad")

    def test_rejects_no_rows(self):
        with self.assertRaisesRegex(GridError, r"^bad: "):
            validate_grid([], "bad")

    def test_rejects_grid_without_body(self):
        with self.assertRaisesRegex(GridError, r"^bad: "):
            validate_grid(["." * 24], "bad")
```

- [ ] **Step 2: Run to verify failure.** `python3 -m unittest tests.test_grid -v`. Expected: ImportError, no module `botpixels.grid`.

- [ ] **Step 3: Implement** `botpixels/grid.py`

```python
"""Pixel grids: validation and conversion to SVG path data in Clawd's 24-unit space."""

WIDTH = 24
MAX_ROWS = 16
FEET_Y = 20
ALLOWED = frozenset("#o.")


class GridError(ValueError):
    pass


def validate_grid(rows: list[str], mascot_id: str) -> None:
    if not rows:
        raise GridError(f"{mascot_id}: grid has no rows")
    if len(rows) > MAX_ROWS:
        raise GridError(f"{mascot_id}: grid has {len(rows)} rows, max {MAX_ROWS}")
    for i, row in enumerate(rows, 1):
        if len(row) != WIDTH:
            raise GridError(f"{mascot_id}: row {i} is {len(row)} wide, expected {WIDTH}")
        bad = sorted(set(row) - ALLOWED)
        if bad:
            raise GridError(f"{mascot_id}: row {i} has characters {bad!r}; only '#', 'o', '.' allowed")
    if not any("#" in row for row in rows):
        raise GridError(f"{mascot_id}: grid has no body cells")


def runs_to_path(rows: list[str], char: str, y0: int) -> str:
    parts = []
    for r, row in enumerate(rows):
        x = 0
        while x < len(row):
            if row[x] != char:
                x += 1
                continue
            start = x
            while x < len(row) and row[x] == char:
                x += 1
            w = x - start
            parts.append(f"M{start} {y0 + r}h{w}v1h-{w}z")
    return "".join(parts)


def body_path(rows: list[str]) -> str:
    return runs_to_path(rows, "#", FEET_Y - len(rows))


def eye_path(rows: list[str]) -> str:
    return runs_to_path(rows, "o", FEET_Y - len(rows))
```

- [ ] **Step 4: Run to verify pass.** `python3 -m unittest tests.test_grid -v`. Expected: 11 tests OK.

- [ ] **Step 5: Commit** (Claude): `git add botpixels tests && git commit` with message `feat: add grid validation and grid-to-path; Task 1 of botpixels kits`.

---

### Task 2: Characters and derivation

**Files:**
- Create: `botpixels/mascots.py`
- Create: `botpixels/derive.py`
- Test: `tests/test_derive.py`

**Interfaces:**
- Consumes: `validate_grid`, `body_path`, `eye_path` from Task 1.
- Produces:
  - `@dataclass(frozen=True) class Mascot` with fields `id: str`, `title: str`, `grid: tuple[str, ...]`, `body: str`, `eye: str | None` (None means hole eyes), `nudges: dict[str, tuple[int, int]]` (default empty).
  - `MASCOTS: tuple[Mascot, ...]` in order grokbot, gemini, antigravity, elevenlabs.
  - `CLAWD_COLOUR = "#D97757"`
  - `mascot_paths(m: Mascot, fill: str) -> str`
  - `base_svg(title: str, path_elements: str) -> str`
  - `derive_pose(clawd_svg: str, m: Mascot, pose: str, base_path: str) -> str`

- [ ] **Step 1: Write the failing tests** in `tests/test_derive.py`

```python
import unittest

import generate_icons as g
from botpixels.derive import CLAWD_COLOUR, base_svg, derive_pose, mascot_paths
from botpixels.grid import validate_grid
from botpixels.mascots import MASCOTS, Mascot

GHOST = next(m for m in MASCOTS if m.id == "grokbot")      # pixel eyes
SPARKLE = next(m for m in MASCOTS if m.id == "gemini")     # hole eyes


def d(pose, m=GHOST):
    return derive_pose(g.icons[f"clawd_{pose}"], m, pose, g.BASE_PATH)


class Table(unittest.TestCase):
    def test_roster(self):
        self.assertEqual([m.id for m in MASCOTS], ["grokbot", "gemini", "antigravity", "elevenlabs"])

    def test_every_grid_valid(self):
        for m in MASCOTS:
            validate_grid(list(m.grid), m.id)

    def test_colours(self):
        self.assertEqual({m.id: (m.body, m.eye) for m in MASCOTS}, {
            "grokbot": ("#E6ECF5", "#0F1115"),
            "gemini": ("#969DFF", None),
            "antigravity": ("#3186FF", None),
            "elevenlabs": ("#111111", "#FFFFFF"),
        })


class Derive(unittest.TestCase):
    def test_body_swapped(self):
        out = d("read")
        self.assertNotIn(g.BASE_PATH, out)
        self.assertIn(f'fill="{GHOST.body}"', out)

    def test_pixel_eyes_drawn(self):
        self.assertIn(f'fill="{GHOST.eye}"', d("read"))

    def test_hole_eyes_have_no_eye_path(self):
        self.assertEqual(mascot_paths(SPARKLE, SPARKLE.body).count("<path"), 1)

    def test_limbs_dropped(self):
        for pose in ("dance", "run", "wave"):
            out = d(pose)
            self.assertNotIn(CLAWD_COLOUR, out, pose)
        self.assertNotIn('<rect x="112" y="44"', d("wave"))
        self.assertNotIn('<rect x="36" y="100"', d("run"))

    def test_props_kept(self):
        self.assertIn("&#9835;", d("dance"))
        self.assertIn("<line", d("run"))

    def test_success_confetti_recoloured(self):
        out = d("success")
        self.assertNotIn(CLAWD_COLOUR, out)
        self.assertIn(f'<rect x="60" y="2" width="3" height="5" fill="{GHOST.body}"', out)

    def test_agent_mini_keeps_blue(self):
        out = d("agent")
        self.assertNotIn(g.BASE_PATH, out)
        self.assertIn(f'fill="{g.BLUE}"', out)

    def test_nudge_wraps_overlay(self):
        m = Mascot("t", "T", GHOST.grid, GHOST.body, GHOST.eye, {"read": (-2, 3)})
        out = derive_pose(g.icons["clawd_read"], m, "read", g.BASE_PATH)
        self.assertIn('<g transform="translate(-2,3)">', out)
        self.assertTrue(out.rstrip().endswith("</g>\n</svg>") or out.rstrip().endswith("</svg>"))
        self.assertNotIn('translate(-2,3)', derive_pose(g.icons["clawd_edit"], m, "edit", g.BASE_PATH))

    def test_clawd_base_matches_committed(self):
        clawd_el = f'<path clip-rule="evenodd" d="{g.BASE_PATH}" fill="{g.MASCOT}" fill-rule="evenodd"/>'
        with open("icons/clawd.svg") as f:
            self.assertEqual(base_svg("Clawd", clawd_el), f.read())
```

- [ ] **Step 2: Run to verify failure.** `python3 -m unittest tests.test_derive -v`. Expected: ImportError, no module `botpixels.derive`.

- [ ] **Step 3: Implement** `botpixels/mascots.py`

```python
"""The non-Clawd characters. Grids: 24 wide, '#' body, 'o' eye, '.' empty."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Mascot:
    id: str
    title: str
    grid: tuple[str, ...]
    body: str
    eye: str | None  # None: eyes are holes in the body
    nudges: dict[str, tuple[int, int]] = field(default_factory=dict)


MASCOTS: tuple[Mascot, ...] = (
    Mascot("grokbot", "Grok Bot", (
        "........########........",
        "......############......",
        ".....#########o####.....",
        "....#####o######o###....",
        "....######o#########....",
        "...########o#########...",
        "...##################...",
        "...##################...",
        "...##################...",
        "...##################...",
        "....################....",
        "....################....",
        ".....##############.....",
        "......############......",
        "........########........",
    ), "#E6ECF5", "#0F1115"),
    Mascot("gemini", "Gemini", (
        "...........##...........",
        "...........##...........",
        "..........####..........",
        "..........####..........",
        ".........#o##o#.........",
        "........##o##o##........",
        "......############......",
        "########################",
        "########################",
        "......############......",
        "........########........",
        ".........######.........",
        "..........####..........",
        "..........####..........",
        "...........##...........",
        "...........##...........",
    ), "#969DFF", None),
    Mascot("antigravity", "Antigravity", (
        ".........######.........",
        ".......##########.......",
        "......############......",
        ".....####o####o####.....",
        ".....####o####o####.....",
        "....################....",
        "....################....",
        "....######....######....",
        "...#####........#####...",
        "...####..........####...",
        "..####............####..",
        "..####............####..",
        ".####..............####.",
        ".####..............####.",
        "####................####",
        "###..................###",
    ), "#3186FF", None),
    Mascot("elevenlabs", "ElevenLabs", (
        "......####....####......",
        ".....######..######.....",
        ".....######..######.....",
        ".....##o###..###o##.....",
        ".....##o###..###o##.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
        ".....######..######.....",
    ), "#111111", "#FFFFFF"),
)
```

- [ ] **Step 4: Implement** `botpixels/derive.py`

```python
"""Derive a character's pose SVG from Clawd's finished pose SVG."""

import re

from botpixels.grid import body_path, eye_path
from botpixels.mascots import Mascot

CLAWD_COLOUR = "#D97757"

# A Clawd-orange limb group, with the comment line directly above it if there is one.
_LIMB_RE = re.compile(r'(?:\n[ ]*<!--[^\n]*-->)?\n[ ]*<g fill="' + CLAWD_COLOUR + r'">.*?</g>', re.S)


def mascot_paths(m: Mascot, fill: str) -> str:
    rows = list(m.grid)
    out = f'<path d="{body_path(rows)}" fill="{fill}"/>'
    eyes = eye_path(rows)
    if m.eye and eyes:
        out += f'\n    <path d="{eyes}" fill="{m.eye}"/>'
    return out


def base_svg(title: str, path_elements: str) -> str:
    return (
        '<svg width="128" height="128" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">\n'
        f'  <title>{title}</title>\n'
        '  <g transform="translate(16,14) scale(4)">\n'
        f'    {path_elements}\n'
        '  </g>\n'
        '</svg>\n'
    )


def derive_pose(clawd_svg: str, m: Mascot, pose: str, base_path: str) -> str:
    body_re = re.compile(
        r'<path clip-rule="evenodd" d="' + re.escape(base_path)
        + r'" fill="(#[0-9A-Fa-f]{6})" fill-rule="evenodd"/>'
    )

    def swap(match: re.Match) -> str:
        colour = match.group(1)
        return mascot_paths(m, m.body if colour.upper() == CLAWD_COLOUR else colour)

    out = body_re.sub(swap, clawd_svg)
    out = _LIMB_RE.sub("", out)
    out = out.replace(CLAWD_COLOUR, m.body)

    if pose in m.nudges:
        dx, dy = m.nudges[pose]
        body_end = out.index("</g>") + len("</g>")
        svg_end = out.rindex("</svg>")
        overlay = out[body_end:svg_end].rstrip("\n")
        out = (out[:body_end] + f'\n  <g transform="translate({dx},{dy})">'
               + overlay + "\n  </g>\n" + out[svg_end:])
    return out
```

- [ ] **Step 5: Run to verify pass.** `python3 -m unittest tests.test_derive -v`. Expected: 12 tests OK. Note `import generate_icons` must not write files on import; that holds once Task 3 lands. Until then, importing it writes `icons/` in place, which is harmless because the bytes are identical; Claude checks `git status` shows no change under `icons/` after the run.

- [ ] **Step 6: Commit** (Claude): `feat: add character table and pose derivation; Task 2 of botpixels kits`.

---

### Task 3: Wire the generator and pin Clawd to upstream

**Files:**
- Create: `tests/fixtures/upstream/` (Claude copies it: `git archive cb073fb icons | tar -x -C tests/fixtures/upstream --strip-components=1`)
- Modify: `generate_icons.py` from the line `# Output directory` to the end of file, plus imports at the top
- Test: `tests/test_generate.py`

**Interfaces:**
- Consumes: `MASCOTS`, `Mascot` (Task 2), `validate_grid`, `GridError` (Task 1), `derive_pose`, `base_svg`, `mascot_paths` (Task 2).
- Produces:
  - `ROOT: str`, the directory containing `generate_icons.py`.
  - `clawd_files() -> dict[str, str]` (file name to content, 67 entries)
  - `kit_files(m: Mascot) -> dict[str, str]` (67 entries)
  - `main(root: str = ROOT, mascots: tuple[Mascot, ...] = MASCOTS) -> int` (0 on success, 1 on a bad grid, writing nothing in that case)

- [ ] **Step 1: Write the failing tests** in `tests/test_generate.py`

```python
import os
import re
import tempfile
import unittest
import xml.etree.ElementTree as ET

import generate_icons as g
from botpixels.mascots import MASCOTS, Mascot

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures", "upstream")
POSES = sorted(n.removeprefix("clawd_") for n in g.icons)
SVG_NS = "{http://www.w3.org/2000/svg}"


class Clawd(unittest.TestCase):
    def test_byte_identical_to_upstream(self):
        files = g.clawd_files()
        self.assertEqual(sorted(files), sorted(os.listdir(FIXTURES)))
        for name, content in files.items():
            with open(os.path.join(FIXTURES, name)) as f:
                self.assertEqual(content, f.read(), name)

    def test_root_is_script_dir(self):
        self.assertEqual(g.ROOT, os.path.dirname(os.path.abspath(g.__file__)))


class Kits(unittest.TestCase):
    def test_same_poses_plus_base_and_preview(self):
        self.assertEqual(len(POSES), 65)
        for m in MASCOTS:
            expected = {f"{m.id}_{p}.svg" for p in POSES} | {f"{m.id}.svg", "preview.html"}
            self.assertEqual(set(g.kit_files(m)), expected, m.id)

    def test_svgs_parse_with_body_colour(self):
        for m in MASCOTS:
            for name, content in g.kit_files(m).items():
                if not name.endswith(".svg"):
                    continue
                root = ET.fromstring(content)
                self.assertEqual(root.get("viewBox"), "0 0 128 128", name)
                fills = [p.get("fill") for p in root.iter(f"{SVG_NS}path")]
                self.assertIn(m.body, fills, name)

    def test_no_clawd_orange_in_kits(self):
        for m in MASCOTS:
            for name, content in g.kit_files(m).items():
                self.assertNotIn("#D97757", content, f"{m.id}/{name}")

    def test_no_clawd_path_in_kits(self):
        for m in MASCOTS:
            for name, content in g.kit_files(m).items():
                self.assertNotIn(g.BASE_PATH, content, f"{m.id}/{name}")

    def test_preview_links_resolve(self):
        for m in MASCOTS:
            files = g.kit_files(m)
            self.assertIn(f"{m.title} Icon Set", files["preview.html"])
            self.assertNotIn("Clawd", files["preview.html"])
            for src in re.findall(r'src="([^"]+)"', files["preview.html"]):
                self.assertIn(src, files, f"{m.id}: {src}")


class Main(unittest.TestCase):
    def test_writes_every_kit(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(g.main(root=tmp), 0)
            self.assertEqual(len(os.listdir(os.path.join(tmp, "icons"))), 67)
            for m in MASCOTS:
                self.assertEqual(len(os.listdir(os.path.join(tmp, "kits", m.id))), 67)

    def test_rerun_is_idempotent(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            g.main(root=a)
            g.main(root=b)
            g.main(root=b)
            for dirpath, _, names in os.walk(a):
                for n in names:
                    pa = os.path.join(dirpath, n)
                    pb = os.path.join(b, os.path.relpath(pa, a))
                    with open(pa) as fa, open(pb) as fb:
                        self.assertEqual(fa.read(), fb.read(), pa)

    def test_bad_grid_writes_nothing(self):
        bad = Mascot("bad", "Bad", ("#" * 23,), "#000000", None)
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(g.main(root=tmp, mascots=MASCOTS + (bad,)), 1)
            self.assertEqual(os.listdir(tmp), [])
```

- [ ] **Step 2: Copy the upstream fixtures** (Claude): `mkdir -p tests/fixtures/upstream && git archive cb073fb icons | tar -x -C tests/fixtures/upstream --strip-components=1`. Expect 67 files.

- [ ] **Step 3: Run to verify failure.** `python3 -m unittest tests.test_generate -v`. Expected: AttributeError, no `clawd_files`.

- [ ] **Step 4: Implement.** At the top of `generate_icons.py`, after `import os`, add:

```python
import sys

from botpixels.derive import base_svg, derive_pose, mascot_paths
from botpixels.grid import GridError, validate_grid
from botpixels.mascots import MASCOTS

ROOT = os.path.dirname(os.path.abspath(__file__))
```

Delete these blocks, which write files at import time: the `# Output directory` line, `OUT = 'icons'`, and the `for name, content in icons.items():` write loop directly after it; and at the end of the file the `with open(os.path.join(OUT, 'preview.html'), 'w')` block and the two `print` lines after it. Keep the module-level `preview` string construction exactly as it is. Then append:

```python
CLAWD_BASE = base_svg('Clawd', f'<path clip-rule="evenodd" d="{BASE_PATH}" fill="{MASCOT}" fill-rule="evenodd"/>')


def clawd_files():
    files = {f'{name}.svg': content for name, content in icons.items()}
    files['clawd.svg'] = CLAWD_BASE
    files['preview.html'] = preview
    return files


def kit_files(m):
    files = {}
    for name, content in icons.items():
        pose = name.removeprefix('clawd_')
        files[f'{m.id}_{pose}.svg'] = derive_pose(content, m, pose, BASE_PATH)
    files[f'{m.id}.svg'] = base_svg(m.title, mascot_paths(m, m.body))
    files['preview.html'] = (preview.replace('Clawd Icon Set', f'{m.title} Icon Set')
                             .replace('clawd_', f'{m.id}_'))
    return files


def _write(out_dir, files):
    os.makedirs(out_dir, exist_ok=True)
    for name, content in files.items():
        with open(os.path.join(out_dir, name), 'w') as f:
            f.write(content)


def main(root=ROOT, mascots=MASCOTS):
    try:
        for m in mascots:
            validate_grid(list(m.grid), m.id)
    except GridError as e:
        print(f'error: {e}', file=sys.stderr)
        return 1
    _write(os.path.join(root, 'icons'), clawd_files())
    for m in mascots:
        _write(os.path.join(root, 'kits', m.id), kit_files(m))
    print(f'Wrote icons/ and {len(mascots)} kits under {root}: {len(icons)} poses each')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

- [ ] **Step 5: Run the full suite.** `python3 -m unittest -v`. Expected: all tests in all three files OK.

- [ ] **Step 6: Generate for real** (Claude): `cd /tmp && python3 <repo>/generate_icons.py` (from outside the repo, to prove ROOT works), then `git status`. Expected: no change under `icons/`; new `kits/` with four folders of 67 files.

- [ ] **Step 7: Commit** (Claude): `feat: generate four character kits; Clawd pinned byte-identical to upstream`. Commit `kits/` too, since the build kit vendors from it.

---

### Task 4: Contact-sheet review and nudges (Claude)

**Files:**
- Modify: `botpixels/mascots.py` (nudge entries only, a few lines)
- Modify: `kits/` (regenerated)

- [ ] **Step 1:** Copy `kits/` to Zo scratch, render each SVG to PNG with ImageMagick `convert`, and `montage` one sheet per character.
- [ ] **Step 2:** View each sheet. For every pose where a prop floats off the character or overlaps its face, record `(dx, dy)` in that character's `nudges`.
- [ ] **Step 3:** Regenerate, rerun the suite, re-render only the nudged poses, confirm.
- [ ] **Step 4:** Commit `fix: nudge props for <n> poses after contact-sheet review`. Show Ted the four sheets.

---

### Task 5: Docs and PR (Claude)

**Files:**
- Modify: `README.md` (8-section protocol: what and why, constraints, setup, usage, how it works, config, troubleshooting, legend), clawdicons credit at the top, a preview strip per character.
- Modify: `LICENSE` (keep wangzhaode's notice, add `Copyright (c) 2026 Ted Sandico` for new work).
- Modify: `SPRINT.md` (phases ticked, Next, Human).

- [ ] **Step 1:** Write the README, LICENSE line, and SPRINT update.
- [ ] **Step 2:** Run the suite once more.
- [ ] **Step 3:** Commit, push `feat/botpixels-kits`, open the PR against `main` for Ted to merge.

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

# botpixels: pixel pose kits for the AI agents in our videos

Date: 2026-10-15. Status: design approved in chat by Ted; spec awaiting his review.

## 1. Goal

Clawd has 65 pixel poses from clawdicons, and the /commands build kit cameos them in episodes. Grok Bot,
Gemini, Antigravity and ElevenLabs show up in our series too, but have no pose kits. botpixels gives each
of them the same 65 poses, in the same 128px SVG format, so the build kit can cameo them with no change
to how poses are consumed.

Success means: one command regenerates every kit; each non-Clawd kit has all 65 poses plus a base icon;
Clawd's output is unchanged from upstream; Ted signs off one contact sheet per character.

## 2. Settled decisions (do not reopen)

| Decision | Ruling | When |
|---|---|---|
| Target | Pose kits for the other mascots; animation tooling is out of scope | Ted, 2026-10-14 |
| Brand line | Original look-alikes in brand colours, never traced or altered official marks | Ted, 2026-10-14 |
| Roster | Grok Bot ghost, Gemini sparkle, Antigravity arch, ElevenLabs bars | Ted, 2026-10-15 |
| Approach | Fork wangzhaode/clawdicons and make the body a parameter | Ted, 2026-10-14 |
| Repo | Public, tedico/botpixels, MIT, upstream attribution kept | Ted, 2026-10-15 |

Brand rationale: xAI and Google both forbid altering their marks. Characters drawn in our own pixel style
that evoke the brand are not the marks, so the kit can stay public. Official SVGs remain usable only
as unaltered badges, which is the build kit's existing rule.

## 3. Characters

Grids are 24 columns wide, matching Clawd's 24-unit body. `#` is body, `o` is an eye cell, `.` is empty.
Every grid is bottom-aligned so its last row sits on Clawd's feet line (unit y = 20), which keeps hats,
held tools and badges in the places the overlays already expect.

| Id | Title | Body | Eye cells | Grid rows |
|---|---|---|---|---|
| grokbot | Grok Bot | #E6ECF5 | Filled pixels, #0F1115 | 15 |
| gemini | Gemini | #969DFF | Holes, like Clawd | 16 |
| antigravity | Antigravity | #3186FF | Holes, like Clawd | 16 |
| elevenlabs | ElevenLabs | #111111 | Filled pixels, #FFFFFF | 16 |

Colours come from the kits Ted supplied in ~/Desktop/LLMAssets. Gemini takes the midpoint of its own
blue-to-lavender gradient because both Google kits share one palette and would otherwise be twins.
The ghost is off-white because pure white vanishes on light frames.

### grokbot
```
........########........
......############......
.....#########o####.....
....#####o######o###....
....######o#########....
...########o#########...
...##################...
...##################...
...##################...
...##################...
....################....
....################....
.....##############.....
......############......
........########........
```

### gemini
```
...........##...........
...........##...........
..........####..........
..........####..........
.........#o##o#.........
........##o##o##........
......############......
########################
########################
......############......
........########........
.........######.........
..........####..........
..........####..........
...........##...........
...........##...........
```

### antigravity
```
.........######.........
.......##########.......
......############......
.....####o####o####.....
.....####o####o####.....
....################....
....################....
....######....######....
...#####........#####...
...####..........####...
..####............####..
..####............####..
.####..............####.
.####..............####.
####................####
###..................###
```

### elevenlabs
```
......####....####......
.....######..######.....
.....######..######.....
.....##o###..###o##.....
.....##o###..###o##.....
.....######..######.....
.....######..######.....
.....######..######.....
.....######..######.....
.....######..######.....
.....######..######.....
.....######..######.....
.....######..######.....
.....######..######.....
.....######..######.....
.....######..######.....
```

## 4. Generator

One script, `generate_icons.py`, refactored in place.

- **Mascot table.** Each entry holds: id, title, body (a grid or, for Clawd only, the original path
  string), body colour, eye style (`hole` or `pixel` plus colour), and an optional nudge table.
- **Clawd is entry zero** and keeps its hand-written path, so its output stays byte-identical.
- **Grid to path.** Each row becomes one horizontal run per contiguous `#` span. `o` cells are left out
  of the body path. Pixel-eye mascots get a second path for the `o` cells in the eye colour.
- **Overlays stay shared.** The 65 pose overlays are written once. Coordinates are unchanged.
- **Base icon.** Each mascot also gets `<id>.svg`: the body alone, centred with
  `translate(16,14) scale(4)`. For Clawd this must equal the committed `icons/clawd.svg`.
- **Mini badge.** The agent pose embeds a small copy of the body (`translate(84,6) scale(1.6)`). It uses
  the same mascot's body, not Clawd's.
- **Nudges.** A per-mascot table of pose name to `(dx, dy)` shifts that pose's overlay group. It starts
  empty and is filled once after the contact-sheet review.
- **Output.** Clawd keeps writing to `icons/` with the `clawd_` prefix, exactly as upstream. Every other
  mascot writes to `kits/<id>/` with the prefix `<id>_`, plus its own `preview.html`. The script creates
  its output folders; upstream crashed when `icons/` was missing.
- **Validation.** Before writing anything, every grid is checked: all rows 24 wide, 1 to 16 rows, only
  `#`, `o` and `.` used, at least one `#`. A bad grid prints the mascot id and row number and exits
  non-zero. This is a build-time tool, not an automation, so failure is a non-zero exit, not an alert.
- **Standard library only.** No new dependencies.

### Clawd-coloured limbs

Four poses add arms or legs in Clawd orange: dance, run, success and wave.

[NEEDS CLARIFICATION] What the other characters do in those four poses. Options: (a) recolour the limbs
to the mascot's body colour; (b) drop the limbs for non-Clawd mascots and keep only props and motion
lines; (c) per-mascot hand-drawn limb overlays. Recommendation: (b), since a sparkle or ghost with crab
legs reads as wrong and (c) is art work that can wait for a real need.

The run pose also tilts and shrinks the body. Non-Clawd mascots get the same transform.

## 5. Contact sheets

A script-free step on Zo, where ImageMagick already rendered the Clawd sheet: copy `kits/<id>/` up,
render each SVG to PNG, montage one sheet per mascot, and review it. Findings go into the nudge table,
then the generator reruns once. Sheets are review artifacts and are not committed.

## 6. Tests

`tests/test_generate.py`, standard-library `unittest`, run with `python3 -m unittest`.

| Test | What it proves |
|---|---|
| Clawd's 65 poses and preview are byte-identical to upstream commit cb073fb | The refactor changed nothing it should not have |
| Generated Clawd base equals committed `icons/clawd.svg` | The base-icon path is right |
| Every mascot emits the same 65 pose names plus its base | No pose silently dropped |
| Every SVG parses, has viewBox `0 0 128 128`, and at least one path in the mascot body colour | Files are usable by the build kit |
| No `#D97757` in any non-Clawd file | No colour leak from overlays or limbs |
| The validator rejects a ragged row, an unknown character, 17 rows, and an empty grid | Bad art fails loudly |
| A known 3-row grid converts to the expected path string | Grid-to-path is correct |

The upstream baseline is captured once into `tests/fixtures/upstream/` from cb073fb.

## 7. Repo housekeeping

- README rewritten to Ted's 8-section protocol, keeping clawdicons credit at the top.
- `LICENSE` keeps wangzhaode's MIT notice and adds tedico's copyright line for the new work.
- `SPRINT.md` added from the build-briefing template.
- Work lands by pull request; Ted merges.

## 8. Out of scope

- Animation, GIF export, or a prompt-to-animation skill.
- Vendoring kits into the Rue Athena /commands build kit. That is a separate bounded change: copy each
  `kits/<id>/` beside the Clawd poses with the licence, and give the staging function a mascot parameter.
- New poses beyond upstream's 65.
- Any use of official logo artwork inside the characters.

## 9. Who builds it

Code goes to the Cursor agent from a no-shell brief, per the workhorse rule in force until 2026-11-04.
Claude writes the brief, reads the diff, runs the suite, commits, and opens the PR. The spec and README
are prose and stay with Claude.

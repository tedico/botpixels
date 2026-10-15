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

    def test_wave_has_hand(self):
        out = d("wave")
        self.assertIn("<!-- waving hand -->", out)
        self.assertIn(f'<g fill="{GHOST.body}">', out)
        self.assertIn('<path d="M96,30 Q110,20 124,30"/>', out)

    def test_wave_differs_from_base(self):
        body = d("read").split("<g ", 1)[1].split("</g>", 1)[0]
        self.assertNotEqual(d("wave").split("</g>", 1)[1].strip(), "</svg>")
        self.assertIn(body, d("wave"))

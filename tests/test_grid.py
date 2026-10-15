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

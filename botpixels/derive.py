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

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

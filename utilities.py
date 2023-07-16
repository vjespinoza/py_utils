import re
from re import Match
from typing import Any


def patter_match(pattern: str, strings: str) -> Match[Any] | None:
    comp_pattern = re.search(pattern, strings)
    return comp_pattern

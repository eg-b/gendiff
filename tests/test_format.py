from gendiff.generate_diff import generate_diff, format_diff
from fixtures.content import BEFORE, AFTER, NOTHING, intersections, differences, result, result_common, result_different
import json, os

def test_result_format():
    format_diff(
        dict(sorted(BEFORE.items())), dict(sorted(AFTER.items())),
        set(sorted(intersections)), set(sorted(differences))
    ) == result


def test_all_common_result_format():
    format_diff(
        dict(sorted(BEFORE.items())), dict(sorted(BEFORE.items())),
        set(sorted(intersections)), set(sorted(differences))
    ) == result_common


def test_all_different_result_format():
    format_diff(
        dict(sorted(NOTHING.items())), dict(sorted(AFTER.items())),
        set(sorted(intersections)), set(sorted(differences))
    ) == result_different
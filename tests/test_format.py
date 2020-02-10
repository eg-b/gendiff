from gendiff.generate_diff import generate_diff, format_diff
from fixtures.content import BEFORE, AFTER, NOTHING, intersections, removed_items, added_items, result, result_all_common, result_all_different
import json, os

def test_result_format():
    assert format_diff(
        dict(sorted(BEFORE.items())), dict(sorted(AFTER.items())),
        sorted(set(intersections)), sorted(set(removed_items)), sorted(set(added_items))
    ) == result


def test_all_common_result_format():
    assert format_diff(
        dict(sorted(BEFORE.items())), dict(sorted(BEFORE.items())),
        sorted(set(BEFORE.keys())), set(), set()
    ) == result_all_common


def test_all_different_result_format():
    assert format_diff(
        dict(sorted(NOTHING.items())), dict(sorted(AFTER.items())),
        set(), set(), sorted(set(AFTER.keys()))
    ) == result_all_different

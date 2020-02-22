from gendiff.generate_diff import format_diff
from test_data import content

def test_result_format():
    assert format_diff(
        dict(sorted(content.BEFORE.items())), dict(sorted(content.AFTER.items())), content.diff) == content.result


def test_all_common_result_format():
    assert format_diff(
        dict(sorted(content.BEFORE.items())), dict(sorted(content.BEFORE.items())),
         content.diff_all_common
    ) == content.result_all_common


def test_all_different_result_format():
    assert format_diff(
        content.NOTHING, dict(sorted(content.AFTER.items())), content.diff_all_different
    ) == content.result_all_different

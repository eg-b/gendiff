from gendiff.generate_diff import format_diff
from test_data import content


def test_result_format():
    indent_lvl = 1
    assert format_diff(content.diff, indent_lvl) == content.result


def test_all_common_result_format():
    indent_lvl = 1
    assert format_diff(content.diff_all_common, indent_lvl) == content.result_all_common


def test_all_different_result_format():
    indent_lvl = 1
    assert format_diff(content.diff_all_different, indent_lvl) == content.result_all_different

def test_recursive_diff():
    indent_lvl = 1
    assert format_diff(content.diff_recursive, indent_lvl) == content.result_recursive_diff

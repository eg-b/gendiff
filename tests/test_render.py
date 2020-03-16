from gendiff.formatters import jsonlike, plain
from test_data import content


def test_json_format():
    indent_lvl = 1
    assert jsonlike.render_diff(content.diff_recursive, indent_lvl) == content.result_recursive_diff


def test_plain_format():
    indent_lvl = 1
    assert plain.render_diff(content.diff_recursive_plain) == content.result_recursive_diff_plain
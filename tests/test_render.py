from gendiff.formatters import jsontxt, plain, json
from test_data import content


def test_jsontxt_format():
    indent_lvl = 1
    assert jsontxt.render_diff(content.diff_recursive, indent_lvl) == content.result_recursive_diff


def test_plain_format():
    assert plain.render_diff(content.diff_recursive_plain) == content.result_recursive_diff_plain


def test_json_format():
    assert json.render_diff(content.diff_recursive_plain) == content.result_json_diff
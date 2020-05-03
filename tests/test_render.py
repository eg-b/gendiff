from gendiff.formatters import jsontxt, plain, json
from tests.test_data import content


def test_jsontxt_format():
    assert jsontxt.render_diff(content.DIFF_RECURSIVE) == content.RESULT_RECURSIVE_DIFF


def test_plain_format():
    assert plain.render_diff(content.DIFF_RECURSIVE) == content.RESULT_RECURSIVE_DIFF_PLAIN


def test_json_format():
    assert json.render_diff(content.DIFF_RECURSIVE) == content.RESULT_JSON_DIFF

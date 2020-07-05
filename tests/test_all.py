from gendiff.build import compare, generate_diff, \
    UNKNOWN_FILE_FORMAT_ERROR, UNKNOWN_OUTPUT_FORMAT_ERROR
from gendiff.formatters import jsontxt, plain
from tests import input_data as test
import json
import os
import pytest


JSON_1 = 'tests/fixtures/1.json'
JSON_2 = 'tests/fixtures/2.json'
YAML_1 = 'tests/fixtures/1.yaml'
YAML_2 = 'tests/fixtures/2.yaml'
JSONTXT_RESULT = 'tests/fixtures/exp_result_jsontxt_diff'
JSON_RESULT = 'tests/fixtures/exp_result_json_diff.json'


class TestCompare:

    @pytest.mark.parametrize("data1,data2,exp_result",
                             [(test.BEFORE, test.AFTER, test.DIFF),
                              (test.BEFORE2, test.AFTER2, test.DIFF2)])
    def test_compare(self, data1, data2, exp_result):
        diff = compare(data1, data2)
        assert diff == exp_result


class TestPaths:

    def test_relpath(self):
        assert generate_diff(plain.render, JSON_1, JSON_2)\
               == "Property 'timeout' was removed"

    def test_abspath(self):
        assert generate_diff(
            plain.render, os.path.abspath(YAML_2), os.path.abspath(YAML_1))\
               == "Property 'timeout' was added with value: '50'"

    def test_abs_and_rel_path(self):
        assert generate_diff(plain.render, JSON_2, os.path.abspath(JSON_1))\
               == "Property 'timeout' was added with value: '50'"

    def test_json_and_yaml(self):
        assert generate_diff(plain.render, YAML_2, JSON_1)\
               == "Property 'timeout' was added with value: '50'"

    def test_yml_and_yaml(self):
        assert generate_diff(plain.render, YAML_1, YAML_2)\
               == "Property 'timeout' was removed"

    def test_wrong_format(self):
        assert generate_diff(plain.render, JSON_1, '1.txt')\
            == UNKNOWN_FILE_FORMAT_ERROR


class TestRender:

    def test_jsontxt_format(self):
        expected_result = get_content(JSONTXT_RESULT)
        assert jsontxt.render(test.DIFF) == expected_result

    def test_json_format(self):
        expected_result = json.load(open(os.path.realpath(JSON_RESULT)))
        assert compare(test.BEFORE, test.AFTER) == expected_result

    def test_wrong_format(self):
        assert generate_diff(None, JSON_1, JSON_2)\
        == UNKNOWN_OUTPUT_FORMAT_ERROR


def get_content(file):
    with open(file, "r") as content:
        return content.read()

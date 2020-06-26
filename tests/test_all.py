from gendiff.constructor import compare, generate_diff
from gendiff.formatters import jsontxt, plain
from tests import test_data
import json
import os


JSON_1 = 'tests/fixtures/1.json'
JSON_2 = 'tests/fixtures/2.json'
YAML_1 = 'tests/fixtures/1.yaml'
YAML_2 = 'tests/fixtures/2.yaml'


class TestCompare:

    def test_compare(self):
        diff = compare(test_data.BEFORE, test_data.AFTER)
        assert diff == test_data.DIFF


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
            == "Wrong file format. Try these: '.yaml', '.yml', '.json'"


class TestRender:

    def test_jsontxt_format(self):
        expected_result = get_content('tests/fixtures/exp_result_diff')
        assert jsontxt.render(test_data.DIFF) == expected_result

    def test_plain_format(self):
        expected_result = get_content('tests/fixtures/exp_result_plain_diff')
        assert plain.render(test_data.DIFF) == expected_result

    def test_json_format(self):
        expected_result = get_content('tests/fixtures/exp_result_json_diff')
        assert json.dumps(test_data.DIFF) == expected_result

    def test_wrong_format(self):
        assert generate_diff(None, JSON_1, JSON_2)\
        == "Wrong output format. Try these: 'jsontxt', 'json', 'plain'"


def get_content(file):
    with open(file, "r") as content:
        return content.read()

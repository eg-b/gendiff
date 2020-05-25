from gendiff.generate_diff import compare
from gendiff.generate_diff import generate_diff
from gendiff.formatters.plain import render_diff as render
import os
from gendiff.formatters import jsontxt, plain, json
from tests.test_data import content



class TestCompare:

    def test_compare(self):
        diff = compare(content.BEFORE, content.AFTER)
        assert diff == content.DIFF


class TestPaths:

    def test_relpath(self):
        assert generate_diff(render, 'tests/fixtures/1.json',
                             'tests/fixtures/2.json') == "Property 'timeout' was removed"

    def test_abspath(self):
        assert generate_diff(render,
                             os.path.abspath('tests/fixtures/2.yaml'),
                             os.path.abspath('tests/fixtures/1.yaml')
                             ) == "Property 'timeout' was added with value: '50'"

    def test_abs_and_rel_path(self):
        assert generate_diff(render, 'tests/fixtures/2.json', os.path.abspath('tests/fixtures/1.json')
                             ) == "Property 'timeout' was added with value: '50'"

    def test_json_and_yaml(self):
        assert generate_diff(render,
                             'tests/fixtures/2.yaml',
                             'tests/fixtures/1.json'
                             ) == "Property 'timeout' was added with value: '50'"

    def test_yml_and_yaml(self):
        assert generate_diff(render,
                             'tests/fixtures/1.yaml',
                             'tests/fixtures/2.yml'
                             ) == "Property 'timeout' was removed"


class TestRender:

    def test_jsontxt_format(self):
        assert jsontxt.render_diff(content.DIFF) == content.RESULT_DIFF

    def test_plain_format(self):
        assert plain.render_diff(content.DIFF) == content.RESULT_DIFF_PLAIN

    def test_json_format(self):
        assert json.render_diff(content.DIFF) == content.RESULT_JSON_DIFF
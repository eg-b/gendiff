from gendiff.generate_diff import generate_diff
from gendiff.formatters.plain import render_diff as render
import os

def test_relpath():
    assert generate_diff(render, 'tests/fixtures/1.json', 'tests/fixtures/2.json') == "Property 'timeout' was removed"



def test_abspath():
    assert generate_diff(render,
        os.path.abspath('tests/fixtures/2.yaml'),
        os.path.abspath('tests/fixtures/1.yaml')
    ) == "Property 'timeout' was added with value: '50'"


def test_abs_and_rel_path():
    assert generate_diff(render, 'tests/fixtures/2.json', os.path.abspath('tests/fixtures/1.json')
    ) == "Property 'timeout' was added with value: '50'"


def test_json_and_yaml():
    assert generate_diff(render,
                         'tests/fixtures/2.yaml',
                         'tests/fixtures/1.json'
                         ) == "Property 'timeout' was added with value: '50'"


def test_yml_and_yaml():
    assert generate_diff(render,
                         'tests/fixtures/1.yaml',
                         'tests/fixtures/2.yml'
                         ) == "Property 'timeout' was removed"

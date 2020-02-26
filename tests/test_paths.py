from gendiff.generate_diff import generate_diff
import os

def test_relpath_json():
    assert generate_diff('fixtures/1.json', 'fixtures/2.json') == '{\n    host: hexlet.io\n   - timeout: 50\n}'


def test_relpath_yaml():
    assert generate_diff('fixtures/1.yaml', 'fixtures/2.yaml') == '{\n    host: hexlet.io\n   - timeout: 50\n}'


def test_abspath_json():
    assert generate_diff(
        os.path.abspath('./fixtures/2.json'),
        os.path.abspath('./fixtures/1.json')
    ) == '{\n    host: hexlet.io\n   + timeout: 50\n}'


def test_abspath_yaml():
    assert generate_diff(
        os.path.abspath('./fixtures/2.yaml'),
        os.path.abspath('./fixtures/1.yaml')
    ) == '{\n    host: hexlet.io\n   + timeout: 50\n}'


def test_both_path_json():
    assert generate_diff(
        'fixtures/2.json',
        os.path.abspath('fixtures/1.json')
    ) == '{\n    host: hexlet.io\n   + timeout: 50\n}'


def test_both_path_yaml():
    assert generate_diff(
        'fixtures/2.yaml',
        os.path.abspath('fixtures/1.yaml')
    ) == '{\n    host: hexlet.io\n   + timeout: 50\n}'

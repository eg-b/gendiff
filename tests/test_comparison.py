from gendiff.generate_diff import compare
from tests.test_data import content



def test_common_items():
    diff = compare(content.BEFORE, content.AFTER)
    assert diff['identical'] == {"host": "hexlet.io"}


def test_updated_items():
    diff = compare(content.BEFORE, content.AFTER)
    assert diff['updated_old'] == {"timeout": 50}
    assert diff['updated_new'] == {"timeout": 20}


def test_removed_items():
    diff = compare(content.BEFORE, content.AFTER)
    assert diff['removed'] == {"proxy": "123.234.53.22"}


def test_added_items():
    diff = compare(content.BEFORE, content.AFTER)
    assert diff['added'] == {"verbose": True}


def test_no_common_items():
    diff = compare(content.NOTHING, content.AFTER)
    assert diff['identical'] == {}
    assert diff['added'] == {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}


def test_no_different_items():
    diff = compare(content.AFTER, content.AFTER)
    assert diff['identical'] == {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}
    assert diff['removed'] == {}
    assert diff['added'] == {}
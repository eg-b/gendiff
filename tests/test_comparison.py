from gendiff.generate_diff import compare
from test_data import content


def test_common_items():
    diff = compare(content.BEFORE, content.AFTER)
    identical, updated_old, updated_new, removed, added = diff
    assert identical == {"host": "hexlet.io"}


def test_updated_items():
    diff = compare(content.BEFORE, content.AFTER)
    identical, updated_old, updated_new, removed, added = diff
    assert updated_old == {"timeout": 50}
    assert updated_new == {"timeout": 20}


def test_removed_items():
    diff = compare(content.BEFORE, content.AFTER)
    identical, updated_old, updated_new, removed, added = diff
    assert removed == {"proxy": "123.234.53.22"}


def test_added_items():
    diff = compare(content.BEFORE, content.AFTER)
    identical, updated_old, updated_new, removed, added = diff
    assert added == {"verbose": True}


def test_no_common_items():
    diff = compare(content.NOTHING, content.AFTER)
    identical, updated_old, updated_new, removed, added = diff
    assert identical == {} and added == {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}


def test_no_different_items():
    diff = compare(content.AFTER, content.AFTER)
    identical, updated_old, updated_new, removed, added = diff
    assert identical == {'host': 'hexlet.io', 'timeout': 20, 'verbose': True} and removed == {} and added == {}
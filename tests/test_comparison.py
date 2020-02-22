from gendiff.generate_diff import compare
from test_data import content


def test_common_items():
    diff = compare(content.BEFORE, content.AFTER)
    common = diff[0]
    assert common == {'host'}


def test_updated_items():
    diff = compare(content.BEFORE, content.AFTER)
    updated = diff[1]


def test_removed_items():
    diff = compare(content.BEFORE, content.AFTER)
    removed = diff[2]
    assert removed == {'proxy'}


def test_added_items():
    diff = compare(content.BEFORE, content.AFTER)
    added = diff[3]
    assert added == {'verbose'}


def test_no_common_items():
    diff = compare(content.NOTHING, content.AFTER)
    common = diff[0]
    added = diff[3]
    assert common == set() and added == {'host', 'timeout', 'verbose'}


def test_no_different_items():
    diff = compare(content.AFTER, content.AFTER)
    common = diff[0]
    removed = diff[2]
    added = diff[3]
    assert common == {'host', 'timeout', 'verbose'} and removed == set() and added == set()
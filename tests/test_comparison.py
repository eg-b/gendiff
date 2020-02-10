from gendiff.generate_diff import make_compare, generate_diff
from fixtures import content
import json, os


def test_common_items():
    common = (make_compare(content.BEFORE, content.AFTER))[0]
    assert common == {'host', 'timeout'}


def test_removed_items():
    removed = (make_compare(content.BEFORE, content.AFTER))[1]
    assert removed == {'proxy'}


def test_added_items():
    added = (make_compare(content.BEFORE, content.AFTER))[2]
    assert added == {'verbose'}


def test_no_common_items():
    common, removed, added = make_compare(content.NOTHING, content.AFTER)
    assert common == set() and added == {'host', 'timeout', 'verbose'}


def test_no_different_items():
    common, removed, added = make_compare(content.AFTER, content.AFTER)
    assert common == {'host', 'timeout', 'verbose'} and removed == set() and added == set()
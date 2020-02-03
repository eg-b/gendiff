from gendiff.generate_diff import make_compare, generate_diff
from fixtures import content
import json, os


def test_common_items():
    common = (make_compare(content.BEFORE, content.AFTER))[0]
    assert common == {'host': 'hexlet.io'},{'timeout': 20, 'proxy': '123.234.53.22', 'verbose': True}



def test_different_items():
    difference = make_compare(content.BEFORE, content.AFTER)[1]
    assert difference == {'timeout': 20, 'proxy': '123.234.53.22', 'verbose': True}


def test_no_common_items():
    common, difference = make_compare(content.NOTHING, content.AFTER)
    assert common == {} and difference == {'host': 'hexlet.io', 'timeout': 20, 'verbose': True}


def test_no_different_items():
    common, difference = make_compare(content.AFTER, content.AFTER)
    assert common == {'host': 'hexlet.io', 'timeout': 20, 'verbose': True} and difference == {}
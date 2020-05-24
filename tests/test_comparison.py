from gendiff.generate_diff import compare
from tests.test_data import content



def test_compare():
    diff = compare(content.BEFORE, content.AFTER)
    assert diff == content.DIFF
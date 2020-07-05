BEFORE = {
    "common": {
        "setting1": "Value 1",
        "setting2": "200",
        "setting3": True,
        "setting6": {
            "key": "value"
            }
        },
    "group1": {
        "baz": "bas",
        "foo": "bar"
        },
    "group2": {
        "abc": "12345"
        }
    }

AFTER = {
    "common": {
        "setting1": "Value 1",
        "setting3": True,
        "setting4": "blah blah",
        "setting5": {
            "key5": "value5"
            }
        },
    "group1": {
        "foo": "bar",
        "baz": "bars"
        },
    "group3": {
        "fee": "100500"
        }
}

DIFF = {'group2': {'value': {'abc': {'value': '12345'}}, 'status': 'removed'},
        'group3': {'value': {'fee': {'value': '100500'}}, 'status': 'added'},
        'group1': {'value': 'complex value', 'status': 'changed', 'children': [
            {'baz': {'old_value': 'bas', 'new_value': 'bars', 'status': 'changed'},
             'foo': {'value': 'bar', 'status': 'unchanged'}}]},
        'common': {'value': 'complex value', 'status': 'changed', 'children': [
            {'setting2': {'value': '200', 'status': 'removed'},
             'setting6': {'value': {'key': {'value': 'value'}}, 'status': 'removed'},
             'setting4': {'value': 'blah blah', 'status': 'added'},
             'setting5': {'value': {'key5': {'value': 'value5'}}, 'status': 'added'},
             'setting1': {'value': 'Value 1', 'status': 'unchanged'},
             'setting3': {'value': True, 'status': 'unchanged'}}]}}


BEFORE2 = {"a": {"b": {"c": 42}, "d": {"f": {"g": {"e": 'enough'}}}}}
AFTER2 = {}

DIFF2 = {'a': {'value': {
    'b': {'value': {
        'c': {'value': 42}}},
    'd': {'value': {
        'f': {'value': {
            'g': {'value': {
                'e': {'value': 'enough'}}}}}}}},
    'status': 'removed'}}

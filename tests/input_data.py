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

DIFF = {
    'common': {'status': 'complex value',
               'value': {
                   'setting1': {'status': 'unchanged', 'value': 'Value 1'},
                   'setting2': {'status': 'removed', 'value': '200'},
                   'setting3': {'status': 'unchanged', 'value': True},
                   'setting4': {'status': 'added', 'value': 'blah blah'},
                   'setting5': {'status': 'added',
                                'value': {'key5': {'value': 'value5'}}},
                   'setting6': {'status': 'removed',
                                'value': {'key': {'value': 'value'}}}}},
    'group1': {'status': 'complex value',
               'value': {'baz': {'new_value': 'bars',
                                 'old_value': 'bas',
                                 'status': 'changed'},
                         'foo': {'status': 'unchanged', 'value': 'bar'}}},
    'group2': {'status': 'removed',
               'value': {'abc': {'value': '12345'}}},
    'group3': {'status': 'added',
               'value': {'fee': {'value': '100500'}}}}


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

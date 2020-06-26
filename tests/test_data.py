BEFORE = {
    "common": {
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

DIFF = {'common': {'children': [
    {'setting2': {'status': 'removed', 'value': '200'},
     'setting3': {'status': 'unchanged', 'value': True},
     'setting4': {'status': 'added', 'value': 'blah blah'},
     'setting5': {'status': 'added', 'value': {'key5': {'value': 'value5'}}},
     'setting6': {'status': 'removed', 'value': {'key': {'value': 'value'}}}}
    ], 'status': 'changed', 'value': 'complex value'},
    'group1': {'children': [
        {'baz': {'new_value': 'bars', 'old_value': 'bas', 'status': 'changed'},
         'foo': {'status': 'unchanged', 'value': 'bar'}}
    ], 'status': 'changed', 'value': 'complex value'},
    'group2': {'status': 'removed', 'value': {'abc': {'value': '12345'}}},
    'group3': {'status': 'added', 'value': {'fee': {'value': '100500'}}}}


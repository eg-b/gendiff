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

DIFF = {'group2': {'value': {'abc': {'value': '12345', 'status': 'removed'}}, 'status': 'removed'},
        'group3': {'value': {'fee': {'value': '100500', 'status': 'added'}}, 'status': 'added'},
        'common': {'value': 'complex value', 'status': 'changed', 'children': [
            {'setting6': {'value': {'key': {'value': 'value', 'status': 'removed'}}, 'status': 'removed'},
             'setting2': {'value': '200', 'status': 'removed'},
             'setting5': {'value': {'key5': {'value': 'value5', 'status': 'added'}}, 'status': 'added'},
             'setting4': {'value': 'blah blah', 'status': 'added'},
             'setting3': {'value': True, 'status': 'unchanged'}}]},
        'group1': {'value': 'complex value', 'status': 'changed', 'children': [
            {'foo': {'value': 'bar', 'status': 'unchanged'},
             'baz': {'old_value': 'bas', 'new_value': 'bars', 'status': 'changed'}}]}}


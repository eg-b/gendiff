def compare(old_data, new_data):
    diff = {}
    old_keys, new_keys = old_data.keys(), new_data.keys()
    for k in (old_keys - new_keys):
        diff.update({k: dict(value=old_data[k], status="removed")})
    for k in (new_keys - old_keys):
        diff.update({k: dict(value=new_data[k], status="added")})
    for k in old_keys & new_keys:
        if old_data[k] == new_data[k]:
            diff.update({k: dict(value=new_data[k], status="unchanged")})
        else:
            if type(old_data[k]) == dict and type(new_data[k]) == dict:
                children = compare(old_data[k], new_data[k])
                diff.update({k: dict(value='complex_value', status="changed")})
                diff.update(children)
            else:
                diff.update({k:dict(old_value=old_data[k],
                                  new_value=new_data[k],
                                  status="changed_from_to")})
    get_keys(diff):
        for k, v in diff:
            value = v['value']
            status = v['status']
            if type(value) == dict:
                for key, val in value:
                    diff.update({key: })
    return diff


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

print(compare(BEFORE, AFTER))

{'group2': {'value': {'abc': '12345'}, 'status': 'removed'},
 'group3': {'value': {'fee': '100500'}, 'status': 'added'},
 'common': {'value': 'complex_value', 'status': 'changed'},
 'setting2': {'value': '200', 'status': 'removed'},
 'setting6': {'value': {'key': 'value'}, 'status': 'removed'},
 'setting5': {'value': {'key5': 'value5'}, 'status': 'added'},
 'setting4': {'value': 'blah blah', 'status': 'added'},
 'setting3': {'value': True, 'status': 'unchanged'},
 'group1': {'value': 'complex_value', 'status': 'changed'},
 'foo': {'value': 'bar', 'status': 'unchanged'},
 'baz': {'old_value': 'bas', 'new_value': 'bars', 'status': 'changed_from_to'}}


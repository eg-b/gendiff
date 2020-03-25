BEFORE = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22"
}

AFTER = {
  "host": "hexlet.io",
  "timeout": 20,
  "verbose": True,
}

BEFORE_2 = {
  "common": {
    "setting1": "Value 1",
    "setting6": {
      "key": "value"
    }
  },
  "group1": {
    "baz": "bas",
  },
  "group2": {
    "abc": "12345"
  }
}

AFTER_2 = {
  "common": {
    "setting1": "Value 1",
    "setting5": {
      "key5": "value5"
    }
  },

  "group1": {
    "baz": "bars"
  },

  "group3": {
    "fee": "100500"
  }
}

diff_recursive = ({}, {'common': {'setting1': 'Value 1', 'setting6': {'key': 'value'}}, 'group1': {'baz': 'bas'}}, {'common': {'setting1': 'Value 1', 'setting5': {'key5': 'value5'}}, 'group1': {'baz': 'bars'}}, {'group2': {'abc': '12345'}}, {'group3': {'fee': '100500'}})
diff_recursive_plain = ({}, {'group1': {'baz': 'bas'}}, {'group1': {'baz': 'bars'}}, {'group2': {'abc': '12345'}}, {'group3': {'fee': '100500'}})

NOTHING = {}



result_recursive_diff = '''{
    common: {
        setting1: Value 1
      - setting6: {
            key: value
        }
      + setting5: {
            key5: value5
        }
    }
    group1: {
      - baz: bas
      + baz: bars
    }
   - group2: {
        abc: 12345
    }
   + group3: {
        fee: 100500
    }
}'''

result_recursive_diff_plain = '''\
Property 'group2' was removed
Property 'group3' was added with value: 'complex value'
Property 'group1.baz' was changed. From 'bas' to 'bars'
'''

result_json_diff = '''{"removed_values": {"group2": {"abc": "12345"}}, "added_values": {"group3": {"fee": "100500"}},\
 "updated_old_values": {"group1": {"baz": "bas"}}, "updated_new_values": {"group1": {"baz": "bars"}}}'''
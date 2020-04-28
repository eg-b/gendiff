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

AFTER_2 = {
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

DIFF_RECURSIVE = {
  'removed': {'group2': {'abc': '12345'}},
  'added': {'group3': {'fee': '100500'}},
  'identical': {},
  'updated_old': {'common': {'setting3': True, 'setting6': {'key': 'value'}}, 'group1': {'baz': 'bas', 'foo': 'bar'}},
  'updated_new': {'common': {'setting3': True,  'setting5': {'key5': 'value5'}}, 'group1': {'foo': 'bar', 'baz': 'bars'}}
}


NOTHING = {}



RESULT_RECURSIVE_DIFF = '''{
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
    common: {
      - setting6: {
            key: value
        }
      + setting5: {
            key5: value5
        }
        setting3: True
    }
    group1: {
        foo: bar
      - baz: bas
      + baz: bars
    }
}'''

RESULT_RECURSIVE_DIFF_PLAIN = '''\
Property 'group2' was removed
Property 'group3' was added with value: 'complex value'
Property 'common.setting6' was removed
Property 'common.setting5' was added with value: 'complex value'
Property 'group1.baz' was changed. From 'bas' to 'bars'\
'''

RESULT_JSON_DIFF = '''{"removed": {"group2": {"abc": "12345"}}, "added": {"group3": {"fee": "100500"}},\
 "identical": {}, "updated_old": {"common": {"setting3": true, "setting6": {"key": "value"}},\
 "group1": {"baz": "bas", "foo": "bar"}}, "updated_new": {"common": {"setting3": true, "setting5": {"key5": "value5"}},\
 "group1": {"foo": "bar", "baz": "bars"}}}'''
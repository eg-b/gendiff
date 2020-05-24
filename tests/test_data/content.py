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

DIFF = {'group1->changed':
                        {'foo->unchanged': 'bar',
                         'baz->changed_from_to': ('bas', 'bars')},
                    'common->changed':
                        {'setting2->removed': '200',
                         'setting6->removed':
                             {'key': 'value'},
                         'setting4->added': 'blah blah',
                         'setting5->added':
                             {'key5': 'value5'},
                         'setting3->unchanged': True},
                    'group2->removed':
                        {'abc': '12345'},
                    'group3->added':
                        {'fee': '100500'}}


RESULT_DIFF = '''{
    group1: {
        foo: bar
      - baz: bas
      + baz: bars
    }
    common: {
      - setting2: 200
      - setting6: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting3: True
    }
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
}'''

RESULT_DIFF_PLAIN = '''\
Property 'group1.baz' was changed. From 'bas' to 'bars'
Property 'common.setting2' was removed
Property 'common.setting6' was removed
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: 'complex value'
Property 'group2' was removed
Property 'group3' was added with value: 'complex value'\
'''

RESULT_JSON_DIFF = ('{"group1->changed": {"foo->unchanged": "bar", "baz->changed_from_to": '
 '["bas", "bars"]}, "common->changed": {"setting2->removed": "200", '
 '"setting6->removed": {"key": "value"}, "setting4->added": "blah blah", '
 '"setting5->added": {"key5": "value5"}, "setting3->unchanged": true}, '
 '"group2->removed": {"abc": "12345"}, "group3->added": {"fee": "100500"}}')
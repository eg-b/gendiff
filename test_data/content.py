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

diff = ({"host": "hexlet.io"}, {"timeout": 50}, {"timeout": 20}, {"proxy": "123.234.53.22"}, {"verbose": True})
diff_all_different = ({}, {}, {}, {}, {"host": "hexlet.io", "timeout": 20, "verbose": True})
diff_all_common = ({'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50}, {}, {}, {}, {})
diff_recursive = ({}, {'common': {'setting1': 'Value 1', 'setting6': {'key': 'value'}}, 'group1': {'baz': 'bas'}}, {'common': {'setting1': 'Value 1', 'setting5': {'key5': 'value5'}}, 'group1': {'baz': 'bars'}}, {'group2': {'abc': '12345'}}, {'group3': {'fee': '100500'}})


NOTHING = {}

result = '''{
    host: hexlet.io
   - timeout: 50
   + timeout: 20
   - proxy: 123.234.53.22
   + verbose: True
}'''

result_all_common = '''{
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''

result_all_different = '''{
   + host: hexlet.io
   + timeout: 20
   + verbose: True
}'''

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
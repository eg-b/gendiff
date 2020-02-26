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

diff = ({"host": "hexlet.io"}, {"timeout": 50}, {"timeout": 20}, {"proxy": "123.234.53.22"}, {"verbose": True})
diff_all_different = ({}, {}, {}, sorted({"host": "hexlet.io", "timeout": 20, "verbose": True}))
diff_all_common = (sorted({"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22"}), {}, {}, {}, {})

NOTHING = {}

identical = {'host'}
updated = {'timeout'}
removed_items = {'proxy'}
added_items = {'verbose'}

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

result_json_in_value = '''{
    common: {
        setting1: Value 1
      - setting2: 200
        setting3: true
      - setting6: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
    }
    group1: {
      + baz: bars
      - baz: bas
        foo: bar
    }
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
}'''
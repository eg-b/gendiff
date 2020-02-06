BEFORE = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22"
}

AFTER = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}

NOTHING = {}

intersections = {('host', 'hexlet.io')}
differences = {('timeout', 20), ('timeout', 50), ('verbose', True), ('proxy', '123.234.53.22')}

result = '''{
   host: hexlet.io
 - timeout: 50
 + timeout: 20
 + verbose: True
 - proxy: 123.234.53.22
}'''

result_common = '''{
   host: hexlet.io
   timeout: 50
   proxy: 123.234.53.22
}'''

result_different = '''{
 + host: hexlet.io
 + timeout: 20
 + verbose: True
}'''

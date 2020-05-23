before = {
  "common": {
    "setting1": "Value 1",
    "setting2": "200",
    "setting3": 'true',
    "setting6": {
      "key": "value"
    },
    "site": {
      "base": "hexlet.io",
      "base2": "hexlet.io"
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  },
  "group2": {
    "abc": "12345"
  },
  "same": {
    "abc": "12345",
    "cba": "2222"
  }
}

after = {
  "common": {
    "setting1": "Value 1",
    "setting3": 'true',
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "site": {
      "base2": "hexlet.io"
    }
  },

  "group1": {
    "foo": "bar",
    "baz": "bars"
  },

  "group3": {
    "fee": "100500"
  },
  "same": {
    "abc": "12345",
    "cba": "2222"
    }
}

def compare(file1_data, file2_data):
    diff = {}
    data1_set, data2_set = file1_data.keys(), file2_data.keys()
    unchanged, updated = set(), set()
    removed = dict.fromkeys(data1_set - data2_set)
    added = dict.fromkeys(data2_set - data1_set)

    for k in data1_set & data2_set:
        if file1_data[k] == file2_data[k]:
            unchanged.add(k)
        else:
            if type(file1_data[k]) == dict and type(file2_data[k]) == dict:
                children = compare(file1_data[k], file2_data[k])
                diff.update({k + ' changed': children})
            else:
                updated.add(k)
    for k in removed:
        value = {}
        if type(file1_data[k]) == dict:
            for key in file1_data[k]:
                value.update({f'{key} removed': file1_data[k][key]})
        else:
            value = file1_data[k]
        diff.update({k + ' removed': value})
    for k in added:
        value = {}
        if type(file2_data[k]) == dict:
            for key in file2_data[k]:
                value.update({f'{key} added': file2_data[k][key]})
        else:
            value = file2_data[k]
        diff.update({k + ' added': value})
    for k in unchanged:
        value = {}
        if type(file1_data[k]) == dict:
            for key in file1_data[k]:
                value.update({f'{key} unchanged': file1_data[k][key]})
        else:
            value = file1_data[k]
        diff.update({k + ' unchanged': value})
    for k in updated:
        diff.update(
            {k + ' changed_from_to': (file1_data[k], file2_data[k])})
    return diff

print(compare(before, after))
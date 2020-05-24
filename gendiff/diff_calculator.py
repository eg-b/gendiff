before = {
  "common": {
    "setting1": "Value 1",
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

after = {
  "common": {
    "setting1": "Value 1",
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
                diff.update({k + '->changed': children})
            else:
                updated.add(k)
    for k in removed:
        diff.update({k + '->removed': file1_data[k]})
    for k in added:
        diff.update({k + '->added': file2_data[k]})
    for k in unchanged:
        diff.update({k + '->unchanged': file2_data[k]})
    for k in updated:
        diff.update(
            {k + '->changed_from_to': (file1_data[k], file2_data[k])})
    return diff

print(compare(before, after))

'''
{'common changed':
     {'site changed':
          {'base removed': 'hexlet.io',
           'base2 unchanged': 'hexlet.io'},
      'setting2 removed': '200',
      'setting6 removed':
          {'key': 'value'},
      'setting5 added':
          {'key5': 'value5'},
      'setting4 added': 'blah blah',
      'setting1 unchanged': 'Value 1',
      'setting3 unchanged': 'true'},
 'group1 changed':
     {'foo unchanged': 'bar',
      'baz changed_from_to': ('bas', 'bars')},
 'group2 removed':
     {'abc': '12345'},
 'group3 added':
  {'fee': '100500'},
 'same unchanged':
  {'abc': '12345', 
  'cba': '2222'}} 
'''
'''
{'group1->changed':
     {'foo->unchanged': 'bar',
      'baz->changed_from_to': ('bas', 'bars')},
 'common->changed':
     {'site->changed':
          {'base->removed': 'hexlet.io',
           'base2->unchanged': 'hexlet.io'},
      'setting6->removed':
          {'key': 'value'},
      'setting2->removed': '200',
      'setting5->added': 
          {'key5': 'value5'},
      'setting4->added': 'blah blah',
      'setting1->unchanged': 'Value 1',
      'setting3->unchanged': 'true'},
 'group2->removed':
     {'abc': '12345'},
 'group3->added':
     {'fee': '100500'},
 'same->unchanged':
     {'abc': '12345',
      'cba': '2222'}}
'''
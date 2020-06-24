REMOVED = 'removed'
ADDED = 'added'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
COMPLEX_VALUE = 'complex value'


def compare(old_data, new_data):
    diff = {}
    old_keys, new_keys = old_data.keys(), new_data.keys()
    for k in (old_keys - new_keys):
        value = old_data[k]
        if type(value) == dict:
            value = (iterdict(value, REMOVED))
        diff.update({k: dict(value=value, status=REMOVED)})
    for k in (new_keys - old_keys):
        value = new_data[k]
        if type(value) == dict:
            value = (iterdict(value, ADDED))
        diff.update({k: dict(value=value, status=ADDED)})
    for k in old_keys & new_keys:
        old_value = old_data[k]
        new_value = new_data[k]
        if old_value == new_value:
            diff.update({k: dict(value=new_value, status=UNCHANGED)})
        else:
            if type(old_value) == dict and type(new_value) == dict:
                children = compare(old_value, new_value)
                diff.update({k: dict(value=COMPLEX_VALUE, status=CHANGED, children=[children])})
            else:
                diff.update({k:dict(old_value=old_value,
                                  new_value=new_value,
                                  status=CHANGED)})
    return diff

def iterdict(d, status):
  for k,v in d.items():
     if type(v) == dict:
         iterdict(v)
     else:
         return {k: {'value': v, 'status': status}}

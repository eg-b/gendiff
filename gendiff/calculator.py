REMOVED = 'removed'
ADDED = 'added'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
COMPLEX_VALUE = 'complex value'


def compare(old_data, new_data):
    diff = {}
    old_keys, new_keys = old_data.keys(), new_data.keys()
    for k in (old_keys - new_keys):
        diff.update({k: dict(value=get_value(old_data[k]), status=REMOVED)})
    for k in (new_keys - old_keys):
        diff.update({k: dict(value=get_value(new_data[k]), status=ADDED)})
    for k in old_keys & new_keys:
        old_value = old_data[k]
        new_value = new_data[k]
        if old_value == new_value:
            diff.update({k: dict(value=new_value, status=UNCHANGED)})
        else:
            if type(old_value) == dict and type(new_value) == dict:
                diff.update({k: dict(value=COMPLEX_VALUE, status=CHANGED,
                                     children=[compare(old_value,
                                                       new_value)])})
            else:
                diff.update({k: dict(old_value=old_value, new_value=new_value,
                                     status=CHANGED)})
    return diff


def get_value(node):
    if type(node) == dict:
        for k, v in node.items():
            if type(v) == dict:
                get_value(v)
            else:
                return {k: {'value': v}}
    return node

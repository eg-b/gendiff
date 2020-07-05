STATUS = 'status'
REMOVED = 'removed'
ADDED = 'added'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
COMPLEX_VALUE = 'complex value'
VALUE = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'
CHILDREN = 'children'


def compare(old_data, new_data):
    diff = {}
    old_keys = old_data.keys()
    new_keys = new_data.keys()
    for k in (old_keys - new_keys):
        diff.update({k: {VALUE: get_value(old_data[k]), STATUS: REMOVED}})
    for k in (new_keys - old_keys):
        diff.update({k: {VALUE: get_value(new_data[k]), STATUS: ADDED}})
    for k in old_keys & new_keys:
        old_value = old_data[k]
        new_value = new_data[k]
        if old_value == new_value:
            diff.update({k: {VALUE: new_value, STATUS: UNCHANGED}})
        else:
            if isinstance(old_value, dict) and isinstance(new_value, dict):
                diff.update({k: {VALUE: COMPLEX_VALUE, STATUS: CHANGED,
                                 CHILDREN: [compare(old_value,
                                                    new_value)]}})
            else:
                diff.update({k: {OLD_VALUE: old_value,
                                 NEW_VALUE: new_value,
                                 STATUS: CHANGED}})
    return diff


def get_value(node):
    if isinstance(node, dict):
        result = {}
        for k, v in node.items():
            if isinstance(v, dict):
                result.update({k: {VALUE: get_value(v)}})
            else:
                result.update({k: {VALUE: v}})
    else:
        result = node
    return result

def render_diff(diff, parent=''):
    result = []
    sep = '->'
    for key, value in diff.items():
        _key = key.split(sep)[0]
        group = key.split(sep)[1]
        if group == 'removed':
            result.append(f"Property '{parent}{_key}' was removed")
        elif group == 'added':
            if type(value) == dict:
                value = 'complex value'
            result.append(f"Property '{parent}{_key}'"
                          f" was added with value: '{value}'")
        elif group == 'changed':
            if type(value) == dict:
                parent += _key + '.'
                result.append(render_diff(value, parent))
                parent = ''
        elif group == 'changed_from_to':
            result.append(f"Property '{parent}{_key}' was changed."
                          f" From '{value[0]}'"
                          f" to '{value[1]}'")
    return ('\n'.join(result))

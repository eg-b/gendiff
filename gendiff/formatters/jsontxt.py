def render_diff(diff, indent_lvl=1):
    result = []
    indent = '    ' * indent_lvl
    indent_minus = indent[:-2] + '- '
    indent_plus = indent[:-2] + '+ '
    sep = '->'
    for key, value in diff.items():
        if len(key.split(sep)) == 1:
            new_string = f'{key}: {value}'
            result.append(indent + new_string)
        else:
            _key = key.split(sep)[0]
            group = key.split(sep)[1]
            if type(value) == dict:
                value = render_diff(value, indent_lvl + 1)
            new_string = f'{_key}: {value}'
            if group == 'unchanged':
                result.append(indent + new_string)
            elif group == 'removed':
                result.append(indent_minus + new_string)
            elif group == 'added':
                result.append(indent_plus + new_string)
            elif group == 'changed':
                if type(value) == dict:
                    value = render_diff(value, indent_lvl + 1)
                new_string = f'{_key}: {value}'
                result.append(indent + new_string)
            elif group == 'changed_from_to':
                result.append(indent_minus + f'{_key}: {value[0]}')
                result.append(indent_plus + f'{_key}: {value[1]}')
    return '{' + '\n' + ('\n'.join(result)) + '\n'\
           + '    ' * (indent_lvl - 1) + '}'

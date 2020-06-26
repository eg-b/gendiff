from gendiff.calculator import REMOVED, ADDED, CHANGED, UNCHANGED,\
    COMPLEX_VALUE


def render(diff):
    def _render(diff, indent_lvl=1):
        result = []
        indent = '    ' * indent_lvl
        indent_minus = indent[:-2] + '- '
        indent_plus = indent[:-2] + '+ '
        for k, v in diff.items():
            value = v.get('value')
            if type(value) == dict and v.get('children') is None:
                value = _render(value, indent_lvl + 1)
            status = v.get('status')
            new_string = f'{k}: {value}'
            if status is None:
                result.append(indent + new_string)
            elif status == UNCHANGED:
                result.append(indent + new_string)
            elif status == REMOVED:
                result.append(indent_minus + new_string)
            elif status == ADDED:
                result.append(indent_plus + new_string)
            elif status == CHANGED:
                if value == COMPLEX_VALUE:
                    value = _render(v.get('children')[0], indent_lvl + 1)
                    result.append(indent + f'{k}: {value}')
                else:
                    result.append(
                        indent_minus + f'{k}: {v.get("old_value")}')
                    result.append(
                        indent_plus + f'{k}: {v.get("new_value")}')
        return '{' + '\n' + ('\n'.join(result)) + '\n' \
               + '    ' * (indent_lvl - 1) + '}'
    return _render(diff)

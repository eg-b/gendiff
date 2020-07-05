from gendiff.calculate import REMOVED, ADDED, CHANGED, UNCHANGED,\
    COMPLEX_VALUE, VALUE, STATUS, OLD_VALUE, NEW_VALUE, CHILDREN


def render(diff):
    def _render(diff, indent_lvl=1):
        result = []
        indent = '    ' * indent_lvl
        indent_minus = f'{indent[:-2]}- '
        indent_plus = f'{indent[:-2]}+ '
        for k, v in sorted(diff.items()):
            value = v.get(VALUE)
            if isinstance(value, dict) and v.get(CHILDREN) is None:
                value = _render(value, indent_lvl + 1)
            status = v.get(STATUS)
            new_string = f'{k}: {value}'
            if status == UNCHANGED:
                result.append(indent + new_string)
            elif status == REMOVED:
                result.append(indent_minus + new_string)
            elif status == ADDED:
                result.append(indent_plus + new_string)
            elif status == CHANGED:
                if value == COMPLEX_VALUE:
                    value = _render(v[CHILDREN][0], indent_lvl + 1)
                    result.append(indent + f'{k}: {value}')
                else:
                    result.append(
                        indent_minus + f'{k}: {v[OLD_VALUE]}')
                    result.append(
                        indent_plus + f'{k}: {v[NEW_VALUE]}')
            else:
                result.append(indent + new_string)
        return '{' + '\n' + ('\n'.join(result)) + '\n' \
               + '    ' * (indent_lvl - 1) + '}'
    return _render(diff)

from gendiff import diff


def render(_diff):
    def _render(_diff, indent_lvl=1):
        result = []
        indent = '    ' * indent_lvl
        indent_minus = f'{indent[:-2]}- '
        indent_plus = f'{indent[:-2]}+ '
        for k, v in sorted(_diff.items()):
            value = v.get(diff.VALUE)
            status = v.get(diff.STATUS)
            if isinstance(value, dict) and status != diff.COMPLEX_VALUE:
                value = _render(value, indent_lvl + 1)
            new_string = f'{k}: {value}'
            if status == diff.UNCHANGED:
                result.append(indent + new_string)
            elif status == diff.REMOVED:
                result.append(indent_minus + new_string)
            elif status == diff.ADDED:
                result.append(indent_plus + new_string)
            elif status == diff.CHANGED:
                result.append(
                    f'{indent_minus}{k}: {v[diff.OLD_VALUE]}')
                result.append(
                    f'{indent_plus}{k}: {v[diff.NEW_VALUE]}')
            elif status == diff.COMPLEX_VALUE:
                value = _render(value, indent_lvl + 1)
                result.append(f'{indent}{k}: {value}')
            else:
                result.append(indent + new_string)
        return '{' + '\n' + ('\n'.join(result)) + '\n' \
               + '    ' * (indent_lvl - 1) + '}'
    return _render(_diff)

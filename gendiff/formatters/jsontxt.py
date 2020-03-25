from gendiff.diff_calculator import compare


def render_diff(diff, indent_lvl=1):
    identical, updated_old, updated_new, removed, added = diff
    diff = identical, updated_new, removed, added
    result = ''
    for group in diff:
        for key in group.keys():
            if type(group[key]) == dict:
                inner_result = ''
                for k, v in group[key].items():
                    inner_result += (
                        '\n' + '    ' * (indent_lvl + 1)
                        + '{}: {}'.format(k, v)
                    )
                value = '{' + inner_result + '\n' + '    ' * (indent_lvl) + '}'
            else:
                value = group[key]
            if key in identical:
                result += (
                    '\n' + '    ' * indent_lvl + '{}: {}'.format(key, value)
                )
            if key in updated_new:
                if (
                    type(updated_old[key]) == dict
                    and type(updated_new[key]) == dict
                ):
                    child = compare(updated_old[key], updated_new[key])
                    value = render_diff(child, indent_lvl + 1)
                    result += (
                        '\n' + '    ' * indent_lvl +
                        '{}: {}'.format(key, value)
                    )
                else:
                    result += (
                        '\n' + '   ' * indent_lvl +
                        '- {}: {}'.format(key, updated_old[key])
                    )
                    result += (
                        '\n' + '   ' * indent_lvl +
                        '+ {}: {}'.format(key, value)
                    )
            if key in removed:
                result += (
                    '\n' + '   ' * indent_lvl +
                    '- {}: {}'.format(key, value)
                )
            if key in added:
                result += (
                    '\n' + '   ' * indent_lvl +
                    '+ {}: {}'.format(key, value)
                )
    return '{' + result + '\n' + '    ' * (indent_lvl - 1) + '}'

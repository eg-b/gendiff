from gendiff.diff_calculator import compare


def render_diff(diff, indent_lvl=1):
    result = []
    indent = '    ' * indent_lvl
    indent_minus = indent[:-2] + '- '
    indent_plus = indent[:-2] + '+ '
    for group, content in diff.items():
        for key, value in content.items():
            if type(value) == dict:
                inner_result = ''
                for k, v in value.items():
                    inner_result += (
                            '    ' * (indent_lvl + 1)
                            + f'{k}: {v}'
                    )
                diff_value = '{' + '\n' + inner_result + '\n' + indent + '}'
            else:
                diff_value = value
            new_string = f'{key}: {diff_value}'
            if group == 'identical':
                result.append(indent + new_string)
            elif group == 'removed':
                result.append(indent_minus + new_string)
            elif group == 'added':
                result.append(indent_plus + new_string)
            elif group == 'updated_new':
                if (
                    type(value) == dict
                    and type(diff['updated_old'][key]) == dict
                ):
                    child = compare(diff['updated_old'][key], value)
                    diff_value = render_diff(child, indent_lvl + 1)
                    result.append(indent + f'{key}: {diff_value}')
                else:
                    result.append(indent_minus
                                  + f"{key}: {diff['updated_old'][key]}")
                    result.append(indent_plus + new_string)
    return '{' + '\n' + ('\n'.join(result)) + '\n'\
           + '    ' * (indent_lvl - 1) + '}'

from gendiff.diff_calculator import compare


def render_diff(diff, parent=''):
    result = []
    for group, content in diff.items():
        for key, value in content.items():
            if type(value) == dict:
                diff_value = 'complex value'
            else:
                diff_value = value
            if group == 'removed':
                result.append(f"Property '{parent}{key}' was removed")
            elif group == 'added':
                result.append(f"Property '{parent}{key}'"
                              f" was added with value: '{diff_value}'")
            elif group == 'updated_new':
                if (
                        type(diff['updated_old'][key]) == dict
                        and type(value) == dict
                ):
                    parent += key + '.'
                    child = compare(diff['updated_old'][key], value)
                    result.append(render_diff(child, parent))
                    parent = ''
                else:
                    result.append(f"Property '{parent}{key}' was changed."
                                  f" From '{diff['updated_old'][key]}'"
                                  f" to '{value}'")
    return ('\n'.join(result))

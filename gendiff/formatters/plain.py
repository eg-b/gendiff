from gendiff.diff_calculator import compare


def render_diff(diff, parent=''):
    identical, updated_old, updated_new, removed, added = diff
    diff = identical, removed, added, updated_new
    result = ''
    for group in diff:
        for key in group.keys():
            if type(group[key]) == dict:
                value = 'complex value'
            else:
                value = group[key]
            if key in removed:
                result += (
                    "Property '{}{}' was removed".format(parent, key) + '\n'
                )
            if key in added:
                result += (
                    "Property '{}{}' was added with value: '{}'"
                    .format(parent, key, value) + '\n'
                )
            if key in updated_new:
                if (
                        type(updated_old[key]) == dict
                        and type(updated_new[key]) == dict
                ):
                    parent += key + '.'
                    child = compare(updated_old[key], updated_new[key])
                    result += render_diff(child, parent)
                    parent = ''
                else:
                    result += (
                            "Property '{}{}' was changed. From '{}' to '{}'"
                            .format(
                                parent, key, updated_old[key], updated_new[key]
                                ) + '\n'
                    )
    return result

from gendiff.diff_calculator import REMOVED, ADDED, CHANGED, COMPLEX_VALUE


def render_diff(diff):
    def render(diff, parent=''):
        result = []
        for k, v in diff.items():
            value = v.get('value')
            status = v.get('status')
            if status == REMOVED:
                result.append(f"Property '{parent}{k}' was removed")
            elif status == ADDED:
                if type(value) == dict:
                    value = COMPLEX_VALUE
                result.append(f"Property '{parent}{k}'"
                              f" was added with value: '{value}'")
            elif status == CHANGED:
                if value == COMPLEX_VALUE:
                    parent += k + '.'
                    result.append(render(v.get('children')[0], parent))
                    parent = ''
                else:
                    result.append(f"Property '{parent}{k}' was changed."
                                  f" From \'{v.get('old_value')}\'"
                                  f" to \'{v.get('new_value')}\'")
        return ('\n'.join(result))
    return(render(diff))

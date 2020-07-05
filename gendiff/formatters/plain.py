from gendiff.calculate import REMOVED, ADDED, CHANGED, COMPLEX_VALUE, \
    NEW_VALUE, OLD_VALUE, CHILDREN, STATUS, VALUE


def render(diff):
    def _render(diff, parent=''):
        result = []
        for k, v in sorted(diff.items()):
            value = v.get(VALUE)
            status = v.get(STATUS)
            if status == REMOVED:
                result.append(f"Property '{parent}{k}' was removed")
            elif status == ADDED:
                if isinstance(value, dict):
                    value = COMPLEX_VALUE
                result.append(f"Property '{parent}{k}'"
                              f" was added with value: '{value}'")
            elif status == CHANGED:
                if value == COMPLEX_VALUE:
                    parent += k + '.'
                    result.append(_render(v[CHILDREN][0], parent))
                    parent = ''
                else:
                    result.append(f"Property '{parent}{k}' was changed. "
                                  f"From \'{v[OLD_VALUE]}\' "
                                  f"to \'{v[NEW_VALUE]}\'")
        return ('\n'.join(result))
    return(_render(diff))

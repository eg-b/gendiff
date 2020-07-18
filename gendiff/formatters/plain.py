from gendiff import diff


def render(_diff):
    def _render(_diff, parent=''):
        result = []
        for k, v in sorted(_diff.items()):
            value = v.get(diff.VALUE)
            status = v.get(diff.STATUS)
            if status == diff.REMOVED:
                result.append(f"Property '{parent}{k}' was removed")
            elif status == diff.ADDED:
                if isinstance(value, dict):
                    value = diff.COMPLEX_VALUE
                result.append(f"Property '{parent}{k}'"
                              f" was added with value: '{value}'")
            elif status == diff.CHANGED:
                result.append(f"Property '{parent}{k}' was changed. "
                              f"From \'{v[diff.OLD_VALUE]}\' "
                              f"to \'{v[diff.NEW_VALUE]}\'")
            elif status == diff.COMPLEX_VALUE:
                parent += k + '.'
                result.append(_render(value, parent))
                parent = ''
        return ('\n'.join(result))
    return(_render(_diff))

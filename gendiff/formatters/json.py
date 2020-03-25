import json


def render_diff(diff):
    identical, updated_old, updated_new, removed, added = diff
    result = {}
    result["removed_values"] = removed
    result["added_values"] = added
    result["updated_old_values"] = updated_old
    result["updated_new_values"] = updated_new
    result = json.dumps(result)
    return result

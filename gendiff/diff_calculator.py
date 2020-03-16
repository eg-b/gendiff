def compare(file1_data, file2_data):
    data1_set, data2_set = set(file1_data.keys()), set(file2_data.keys())
    identical, updated = set(), set()
    for k in data1_set.intersection(data2_set):
        if file1_data[k] == file2_data[k]:
            identical.add(k)
        else:
            updated.add(k)
    removed = data1_set.difference(data2_set)
    added = data2_set.difference(data1_set)
    identical, updated_old, updated_new, removed, added = (
        dict.fromkeys(identical),
        dict.fromkeys(updated),
        dict.fromkeys(updated),
        dict.fromkeys(removed),
        dict.fromkeys(added)
    )
    for k in identical:
        identical[k] = file1_data[k]
    for k in updated_old:
        updated_old[k] = file1_data[k]
    for k in updated_new:
        updated_new[k] = file2_data[k]
    for k in removed:
        removed[k] = file1_data[k]
    for k in added:
        added[k] = file2_data[k]
    diff = identical, updated_old, updated_new, removed, added
    return diff

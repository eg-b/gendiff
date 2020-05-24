def compare(file1_data, file2_data):
    diff = {}
    data1_set, data2_set = file1_data.keys(), file2_data.keys()
    unchanged, updated = set(), set()
    removed = dict.fromkeys(data1_set - data2_set)
    added = dict.fromkeys(data2_set - data1_set)
    for k in data1_set & data2_set:
        if file1_data[k] == file2_data[k]:
            unchanged.add(k)
        else:
            if type(file1_data[k]) == dict and type(file2_data[k]) == dict:
                children = compare(file1_data[k], file2_data[k])
                diff.update({k + '->changed': children})
            else:
                updated.add(k)
    for k in removed:
        diff.update({k + '->removed': file1_data[k]})
    for k in added:
        diff.update({k + '->added': file2_data[k]})
    for k in unchanged:
        diff.update({k + '->unchanged': file2_data[k]})
    for k in updated:
        diff.update(
            {k + '->changed_from_to': (file1_data[k], file2_data[k])})
    return diff

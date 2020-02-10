from gendiff.parsers import parse_files


def generate_diff(path_to_file1, path_to_file2):
    file1_data, file2_data = parse_files(path_to_file1, path_to_file2)
    intersection, removed, added = make_compare(file1_data, file2_data)
    result = format_diff(file1_data, file2_data, intersection, removed, added)
    return result


def make_compare(file1_data, file2_data):
    data1_set, data2_set = set(file1_data.keys()), set(file2_data.keys())
    intersection = data1_set.intersection(data2_set)
    removed = data1_set.difference(data2_set)
    added = data2_set.difference(data1_set)
    difference = data1_set.symmetric_difference(data2_set)
    return intersection, removed, added


def format_diff(file1_data, file2_data, intersection, removed, added):
    result = ''
    for k in intersection:
        if file1_data[k] != file2_data[k]:
            result += ('\n - ' + '{}: {}'.format(k, file1_data[k]))
            result += ('\n + ' + '{}: {}'.format(k, file2_data[k]))
        else: result += ('\n   {}: {}'.format(k, file2_data[k]))
    for k in removed:
        result += ('\n - ' + '{}: {}'.format(k, file1_data[k]))
    for k in added:
        result += ('\n + ' + '{}: {}'.format(k, file2_data[k]))
    return '{' + result + '\n}'

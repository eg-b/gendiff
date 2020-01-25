import json
import os


def generate_diff(path_to_file1, path_to_file2):
      
    first_data, second_data = (json.load(open(os.path.realpath(path_to_file1))),
                               json.load(open(os.path.realpath(path_to_file2)))
                            )
    first_data_set, second_data_set = set(first_data.items()), set(second_data.items())
    intersection = dict(first_data_set.intersection(second_data_set))
    difference = dict(first_data_set.symmetric_difference(second_data_set))
    result = '\n'.join('  {}: {}'.format(k, v) for k, v in intersection.items())
    for k, v in difference.items():
        if k not in second_data.keys():
            result += ('\n - ' + '{}: {}'.format(k, v))
        elif k not in first_data.keys():
            result += ('\n + ' + '{}: {}'.format(k, v))
        else:
            result += ('\n - ' + '{}: {}'.format(k, first_data[k]))
            result += ('\n + ' + '{}: {}'.format(k, second_data[k]))
    return '{' + result + '\n}'

    
#print(generate_diff('/home/eg/Documents/before.json', '/home/eg/Documents/after.json'))
import json
import os


def generate_diff(path_to_file1, path_to_file2):
      
    first_data, second_data = (json.load(open(os.path.realpath(path_to_file1))),
                               json.load(open(os.path.realpath(path_to_file2)))
                            )
    first_data_set, second_data_set = set(first_data.items()), set(second_data.items())
    intersection = dict(first_data_set.intersection(second_data_set))
    difference = dict(first_data_set.symmetric_difference(second_data_set))
    answer = '\n'.join('   {}: {}'.format(k, v) for k, v in intersection.items())
    for k, v in difference.items():
        if k not in second_data.keys():
            answer += ('\n - ' + '{}: {}'.format(k, v))
        elif k not in first_data.keys():
            answer += ('\n + ' + '{}: {}'.format(k, v))
        else:
            answer += ('\n - ' + '{}: {}'.format(k, first_data[k]))
            answer += ('\n + ' + '{}: {}'.format(k, v))
    return answer

    
print(generate_diff('/home/eg/Documents/before.json', '/home/eg/Documents/after.json'))
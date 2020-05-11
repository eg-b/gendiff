diff = {'common changed':
     {'site changed':
          {'base removed': 'hexlet.io',
           'base2 unchanged': 'hexlet.io'},
      'setting2 removed': '200',
      'setting6 removed': {'key removed': 'value'},
      'setting5 added': {'key5 added': 'value5'},
      'setting4 added': 'blah blah',
      'setting1 unchanged': 'Value 1',
      'setting3 unchanged': 'true'},
 'group1 changed':
     {'foo unchanged': 'bar',
      'baz changed_from_to': ('bas', 'bars')},
 'group2 removed': {'abc removed': '12345'},
 'group3 added': {'fee added': '100500'}}

def render_diff(diff, indent_lvl=1):
    result = []
    indent = '    ' * indent_lvl
    indent_minus = indent[:-2] + '- '
    indent_plus = indent[:-2] + '+ '
    for key, value in diff.items():
        key_ = key.split(' ')[0]
        group = key.split(' ')[1]
        diff_value = value
        if group != 'changed_from_to' and type(value) == dict:
            diff_value == render_diff(value, indent_lvl)
        new_string = f'{key_}: {diff_value}'
        if group == 'unchanged':
            result.append(indent + new_string)
        elif group == 'removed':
            result.append(indent_minus + new_string)
        elif group == 'added':
            result.append(indent_plus + new_string)
        elif group == 'changed':
            if type(value) == dict:
                diff_value = render_diff(value, indent_lvl + 1)
            new_string = f'{key_}: {diff_value}'
            result.append(indent + new_string)
        elif group == 'changed_from_to':
            result.append(indent_minus + f'{key_}: {diff_value[0]}')
            result.append(indent_plus + f'{key_}: {diff_value[1]}')
    return '{' + '\n' + ('\n'.join(result)) + '\n'\
           + '    ' * (indent_lvl - 1) + '}'

print(render_diff(diff))
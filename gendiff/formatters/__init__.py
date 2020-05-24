from gendiff.formatters import jsontxt
from gendiff.formatters import plain
from gendiff.formatters import json


FORMATTERS = {'json': json.render_diff,
              'jsontxt': jsontxt.render_diff,
              'plain': plain.render_diff}

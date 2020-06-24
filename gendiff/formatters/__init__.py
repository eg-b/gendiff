from gendiff.formatters import jsontxt
from gendiff.formatters import plain
import json


FORMATTERS = {'json': json.dumps,
              'jsontxt': jsontxt.render_diff,
              'plain': plain.render_diff}

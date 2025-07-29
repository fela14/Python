mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(str(mapping))

import json
pretty = json.dumps(mapping, indent=4, sort_keys=True)
print(pretty)

mapping['d'] = {1,2,3}
# pretty = json.dumps(mapping, indent=4, sort_keys=True)
# print(pretty)     # TypeError: Object of type set is not JSON serializable

import pprint
pprint.pprint(mapping)
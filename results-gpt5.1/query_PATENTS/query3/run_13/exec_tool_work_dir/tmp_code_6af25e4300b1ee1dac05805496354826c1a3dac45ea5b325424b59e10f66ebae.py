code = """import json, re, pandas as pd
from collections import defaultdict

# load full publication records
path = var_call_vKCNsx6vDCWv5DoIjkFgCjv1
with open(path, 'r') as f:
    pubs = json.load(f)

# helper to extract publication_number from Patents_info
pubnum_re = re.compile(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A0-9]+)')

target_pubnums = set()
for rec in pubs:
    m = pubnum_re.search(rec.get('Patents_info',''))
    if m:
        target_pubnums.add(m.group(1))

# now search whole publication db for citations to these pub numbers
result = json.dumps({"target_pubnums": sorted(list(target_pubnums))[:50]})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Xfm7TzrGIJhB7HxYCnc4fUnE': [], 'var_call_vKCNsx6vDCWv5DoIjkFgCjv1': 'file_storage/call_vKCNsx6vDCWv5DoIjkFgCjv1.json'}

exec(code, env_args)

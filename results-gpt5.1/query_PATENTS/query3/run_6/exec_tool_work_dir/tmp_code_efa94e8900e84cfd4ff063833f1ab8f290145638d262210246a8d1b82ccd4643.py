code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_8FYofJPm9ETW7aZJWS67e67B
with open(path, 'r') as f:
    records = json.load(f)

# extract publication_number from Patents_info
pubnum_re = re.compile(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)')

uc_pubnums = set()
for r in records:
    m = pubnum_re.search(r['Patents_info'])
    if m:
        uc_pubnums.add(m.group(1))

# Now find all publications that cite these UC publications
# We'll query DB in a second step, so prepare list
uc_pubnums_list = sorted(uc_pubnums)

result = json.dumps(uc_pubnums_list)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_1K5l7r0nYbvnrpxZajkCjJDT': [], 'var_call_8FYofJPm9ETW7aZJWS67e67B': 'file_storage/call_8FYofJPm9ETW7aZJWS67e67B.json'}

exec(code, env_args)

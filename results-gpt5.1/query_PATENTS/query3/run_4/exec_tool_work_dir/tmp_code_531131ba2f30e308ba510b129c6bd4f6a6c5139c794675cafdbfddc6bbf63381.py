code = """import json, re, pandas as pd, os
from collections import defaultdict

path = var_call_qcTaQmDKZigyj5QSd4cEBbja
with open(path, 'r') as f:
    data = json.load(f)

# Extract UNIV CALIFORNIA publication numbers from Patents_info
uc_pub_numbers = set()
for rec in data:
    info = rec.get('Patents_info','')
    m = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A0-9]+)', info)
    if m:
        uc_pub_numbers.add(m.group(1))

# Now find all records (any assignee) that cite these publication numbers

print('__RESULT__:')
print(json.dumps({'uc_pub_numbers': sorted(uc_pub_numbers)}))"""

env_args = {'var_call_2aKUeaeoMlUw4LnDszGEQP0C': [], 'var_call_S1GppfcZWFEYgjPqeLp8saMe': ['cpc_definition'], 'var_call_qcTaQmDKZigyj5QSd4cEBbja': 'file_storage/call_qcTaQmDKZigyj5QSd4cEBbja.json'}

exec(code, env_args)

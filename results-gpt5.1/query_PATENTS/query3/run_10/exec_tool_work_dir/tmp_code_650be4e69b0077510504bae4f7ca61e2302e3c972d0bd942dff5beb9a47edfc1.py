code = """import json, pandas as pd
from itertools import chain

file_path = var_call_Lqv56Itie8BklYl60TVdMiwb
with open(file_path, 'r') as f:
    data = json.load(f)

rows = []
for rec in data:
    info = rec.get('Patents_info','')
    if 'owned by' in info or 'assigned to' in info or 'holds the' in info:
        # extract assignee between 'owned by ' and ' and has' etc.
        lower = info.lower()
        if 'owned by ' in lower:
            start = lower.index('owned by ') + len('owned by ')
        elif 'assigned to ' in lower:
            start = lower.index('assigned to ') + len('assigned to ')
        elif 'holds the' in lower:
            start = lower.index('holds the') - 1
        else:
            start = 0
        assignee = info[start:].split(' and has')[0].split(' with pub.')[0].strip().strip(',')
        cpc_list = json.loads(rec.get('cpc','[]'))
        primary_codes = {e['code'] for e in cpc_list if e.get('first')}
        rows.append({'assignee': assignee, 'cpc_codes': list(primary_codes)})

# deduplicate assignee-code pairs
pairs = set((r['assignee'], code) for r in rows for code in r['cpc_codes'])

# filter to UNIV CALIFORNIA assignee only (patents assigned to it)
uc_codes = sorted({code for a, code in pairs if 'UNIV CALIFORNIA' in a.upper()})

result = json.dumps({'uc_primary_cpc_codes': uc_codes})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ey6x7kt5CAqheeiKX8NlvEDJ': [], 'var_call_Lqv56Itie8BklYl60TVdMiwb': 'file_storage/call_Lqv56Itie8BklYl60TVdMiwb.json'}

exec(code, env_args)

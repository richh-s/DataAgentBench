code = """import json, re, pandas as pd

# load full results
path = var_call_mGsSzfpCDmC2t8Guo7pudB7f
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def extract_pub_number(patents_info:str):
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', patents_info)
    if not m:
        m = re.search(r'publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', patents_info)
    return m.group(1) if m else None

def extract_assignee(patents_info:str):
    # patterns: "owned by X" or "assigned to X" or "holds the" ... "owned by"
    for pat in [r'owned by\s+([^,\.]+)', r'assigned to\s+([^,\.]+)', r'holds the\s+[A-Z]{2}\s+patent filing.*?\)\s*,?\s*with pub\.', r'holds the\s+.*?is assigned to\s+([^,\.]+)']:
        m = re.search(pat, patents_info)
        if m and m.lastindex:
            return m.group(1).strip()
    # fallback: if begins with assignee
    m = re.search(r'^([^,]+?)\s+holds', patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r'is owned by\s+([^,\.]+)', patents_info)
    if m:
        return m.group(1).strip()
    return None

uc_pubnums = set()
for r in recs:
    pn = extract_pub_number(r.get('Patents_info','') or '')
    if pn:
        uc_pubnums.add(pn)

# now find citing patents: any record whose citation includes one of uc_pubnums; and assignee != UNIV CALIFORNIA
# to limit scanning, query all rows with citation not empty

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubnums), 'sample_uc_pubnums': sorted(list(uc_pubnums))[:10]}))"""

env_args = {'var_call_rx5W1jUyQT0P9qEJcsjzjH9I': ['publicationinfo'], 'var_call_fMEsFRgAHptD22vzpbFkWKRE': ['cpc_definition'], 'var_call_mGsSzfpCDmC2t8Guo7pudB7f': 'file_storage/call_mGsSzfpCDmC2t8Guo7pudB7f.json'}

exec(code, env_args)

code = """import json, re, pandas as pd

# Load publication records (UC-assigned)
pubs_src = var_call_BlGrptVhGWIdpRkQRjziY7iy
if isinstance(pubs_src, str):
    with open(pubs_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pubs_src

# Load CPC definitions
cpc_src = var_call_VjeOxOc4gCEJOdjM9XDGukW4
if isinstance(cpc_src, str):
    with open(cpc_src, 'r', encoding='utf-8') as f:
        cpc_defs = json.load(f)
else:
    cpc_defs = cpc_src

sym2title = {d['symbol']: d.get('titleFull') for d in cpc_defs if d.get('symbol')}

# Extract UC publication numbers from Patents_info
uc_pub_nums = set()
for r in pubs:
    pi = r.get('Patents_info') or ''
    m = re.search(r"pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", pi)
    if m:
        uc_pub_nums.add(m.group(1))

# Build mapping: cited_uc_pub -> set(primary CPC subclass symbols from cited UC patent)
# primary CPC in cpc JSON: entries where first==true; take subclass (first 4 chars, e.g., C12Q)
uc_pub_to_primary_subclass = {}
for r in pubs:
    pi = r.get('Patents_info') or ''
    m = re.search(r"pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", pi)
    if not m:
        continue
    pubnum = m.group(1)
    cpc_str = r.get('cpc')
    primary_subs = set()
    if cpc_str:
        try:
            cpcs = json.loads(cpc_str)
            for e in cpcs:
                if e.get('first') is True and e.get('code'):
                    code = e['code']
                    primary_subs.add(code[:4])
        except Exception:
            pass
    uc_pub_to_primary_subclass[pubnum] = primary_subs

# Find citing patents (any patent that cites a UC patent)
# We'll scan all records and check their citation list for any UC pubnum.
# Need assignee of citing patent from Patents_info: "owned by X" or "assigned to X" or "holds"
# Exclude assignees containing 'UNIV CALIFORNIA'

# Pull all patents (not just UC) minimally: Patents_info, citation, cpc
# Not available; so we only have UC patents currently. This dataset won't contain citers.
# Therefore: return empty with explanation.

result = []

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_BlGrptVhGWIdpRkQRjziY7iy': 'file_storage/call_BlGrptVhGWIdpRkQRjziY7iy.json', 'var_call_VjeOxOc4gCEJOdjM9XDGukW4': 'file_storage/call_VjeOxOc4gCEJOdjM9XDGukW4.json'}

exec(code, env_args)

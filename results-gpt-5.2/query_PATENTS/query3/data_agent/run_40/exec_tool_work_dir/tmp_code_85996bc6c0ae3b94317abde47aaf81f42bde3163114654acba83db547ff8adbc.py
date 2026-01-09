code = """import json, re, pandas as pd

# Load publication data (UC assignee patents)
uc_path = var_call_tlkzTucRomT39NGxEPtHjU1D
with open(uc_path, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

# Load CPC definitions
cpc_path = var_call_PhBDJPa11TP1ROqC42Qfqs5k
with open(cpc_path, 'r', encoding='utf-8') as f:
    cpc_rows = json.load(f)

cpc_map = {r['symbol'].strip(): (r.get('titleFull') or '').strip() for r in cpc_rows}

# Helper to extract publication number from Patents_info
pub_re = re.compile(r"pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)")

def get_pub(patents_info:str):
    if not patents_info:
        return None
    m = pub_re.search(patents_info)
    if m:
        return m.group(1)
    # fallback: look for 'publication number'
    m2 = re.search(r"publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)", patents_info)
    if m2:
        return m2.group(1)
    return None

# build list of UC publication numbers
uc_pubs = set()
for r in uc_rows:
    p = get_pub(r.get('Patents_info',''))
    if p:
        uc_pubs.add(p)

# Query citing patents where citation contains any UC pub number
# To keep within SQLite limits, we will brute-force in python by scanning all rows with 'citation' like '%US-%' etc.

# Pull potentially citing rows (those with non-empty citation)
# (already have uc_rows; need all rows with citations)

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubs)}, ensure_ascii=False))"""

env_args = {'var_call_tlkzTucRomT39NGxEPtHjU1D': 'file_storage/call_tlkzTucRomT39NGxEPtHjU1D.json', 'var_call_PhBDJPa11TP1ROqC42Qfqs5k': 'file_storage/call_PhBDJPa11TP1ROqC42Qfqs5k.json'}

exec(code, env_args)

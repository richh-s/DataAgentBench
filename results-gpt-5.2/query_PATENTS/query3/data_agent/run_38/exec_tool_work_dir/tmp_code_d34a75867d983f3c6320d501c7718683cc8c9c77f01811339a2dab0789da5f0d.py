code = """import json, re, pandas as pd

# load UC-assignee publications rows
rows = var_call_HPGrAYsdLHl5CfJGN6CGzNQN
if isinstance(rows, str):
    with open(rows, 'r', encoding='utf-8') as f:
        rows = json.load(f)

# helper: extract publication number from Patents_info
pub_re = re.compile(r'pub\. number\s+([^\s\.]+)')

def get_pub(patents_info:str):
    if not patents_info:
        return None
    m = pub_re.search(patents_info)
    return m.group(1) if m else None

uc_pubs = set()
for r in rows:
    p = get_pub(r.get('Patents_info',''))
    if p:
        uc_pubs.add(p)

# now find citing publications: those whose citation list contains any of uc_pubs
# brute force by scanning all publicationinfo
# Use incremental SQL: fetch Patents_info,cpc,citation for all rows with non-empty citation
# (SQLite has no good JSON search here)

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubs), 'sample_uc_pubs': sorted(list(uc_pubs))[:20]}))"""

env_args = {'var_call_Tos0p1lnlN2ubDRTAIwKJNro': ['publicationinfo'], 'var_call_ZFmIV1fFavMFSIv2jon6hg0O': ['cpc_definition'], 'var_call_Cp4L2jTAkxznf31PFHsbbte3': [], 'var_call_HPGrAYsdLHl5CfJGN6CGzNQN': 'file_storage/call_HPGrAYsdLHl5CfJGN6CGzNQN.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

# load full UC-assigned publications
path = var_call_uMQByuYhjtuOxhdCT5ngThYN
with open(path, 'r', encoding='utf-8') as f:
    uc_recs = json.load(f)

def extract_pub_number(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r"pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", patents_info)
    if m:
        return m.group(1)
    m = re.search(r"publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", patents_info)
    if m:
        return m.group(1)
    return None

uc_pub_nums = set()
for r in uc_recs:
    pn = extract_pub_number(r.get('Patents_info',''))
    if pn:
        uc_pub_nums.add(pn)

# map cited publication -> set(of citing pub numbers) using all rows in table (scan all citations)
# pull only Patents_info and citation for entire table in chunks not supported; do full query

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pub_nums)}))"""

env_args = {'var_call_k78O5d6VNqdn0Sfz6lA2VsNN': ['publicationinfo'], 'var_call_UHXYP2c9u4mFCPdfMa4PRvxZ': ['cpc_definition'], 'var_call_uMQByuYhjtuOxhdCT5ngThYN': 'file_storage/call_uMQByuYhjtuOxhdCT5ngThYN.json'}

exec(code, env_args)

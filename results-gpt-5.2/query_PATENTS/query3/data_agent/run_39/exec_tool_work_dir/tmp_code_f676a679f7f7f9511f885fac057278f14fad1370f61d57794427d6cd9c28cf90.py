code = """import json, re
import pandas as pd

# Load publications assigned to UNIV CALIFORNIA (sampled rows from SQL limit)
path = var_call_wTbCIalUEZlRAiBaa3Xgsl3U
with open(path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Extract cited publication_numbers
cited_nums = set()
for r in pubs:
    cit = r.get('citation')
    if not cit:
        continue
    try:
        cits = json.loads(cit)
    except Exception:
        continue
    for c in cits:
        pn = (c or {}).get('publication_number')
        if pn:
            cited_nums.add(pn)

cited_nums = sorted(cited_nums)
print('__RESULT__:')
print(json.dumps({'cited_publication_numbers': cited_nums, 'n': len(cited_nums)}))"""

env_args = {'var_call_yKDWn9fEaaty0jZ9Ws0dcTn8': ['publicationinfo'], 'var_call_ttsOsaKfjgcL9gGDVwvMGFVe': ['cpc_definition'], 'var_call_wTbCIalUEZlRAiBaa3Xgsl3U': 'file_storage/call_wTbCIalUEZlRAiBaa3Xgsl3U.json'}

exec(code, env_args)

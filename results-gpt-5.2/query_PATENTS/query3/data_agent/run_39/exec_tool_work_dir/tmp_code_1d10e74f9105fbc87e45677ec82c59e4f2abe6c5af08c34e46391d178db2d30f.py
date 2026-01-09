code = """import json, re
import pandas as pd

with open(var_call_GmMQfgQMjmnD4QOivtB1z6h3, 'r', encoding='utf-8') as f:
    cited = set(json.load(f)['cited_publication_numbers'])

with open(var_call_1Po7PcjbmLOEjWaYzsY1abY8, 'r', encoding='utf-8') as f:
    citing_rows = json.load(f)

res = []
for r in citing_rows:
    info = (r.get('Patents_info') or '')
    m = re.search(r'pub\.? (?:number|no\.)\s+([A-Z]{2,}-[0-9]+[A-Z0-9-]*?)\b', info)
    if not m:
        m = re.search(r'has pub\.? number\s+([A-Z]{2,}-[0-9]+[A-Z0-9-]*?)\b', info)
    pubno = m.group(1) if m else None
    if not pubno or pubno not in cited:
        continue

    am = re.search(r'(?:owned by|assigned to)\s+(.+?)\s+and has', info)
    if not am:
        continue
    assignee = am.group(1).strip().strip('.')
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue

    subclass = None
    cpc_str = r.get('cpc')
    if cpc_str:
        try:
            cpcs = json.loads(cpc_str)
            first_codes = [x.get('code') for x in cpcs if isinstance(x, dict) and x.get('first')]
            if first_codes and first_codes[0]:
                code = first_codes[0]
                subclass = re.sub(r'[^A-Z0-9]', '', code)[:4]
        except Exception:
            pass

    if subclass:
        res.append({'citing_assignee': assignee, 'primary_cpc_subclass': subclass})

df = pd.DataFrame(res)
if df.empty:
    out = []
else:
    out = df.drop_duplicates().sort_values(['citing_assignee','primary_cpc_subclass']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps({'pairs': out, 'n_pairs': len(out)}))"""

env_args = {'var_call_yKDWn9fEaaty0jZ9Ws0dcTn8': ['publicationinfo'], 'var_call_ttsOsaKfjgcL9gGDVwvMGFVe': ['cpc_definition'], 'var_call_wTbCIalUEZlRAiBaa3Xgsl3U': 'file_storage/call_wTbCIalUEZlRAiBaa3Xgsl3U.json', 'var_call_GmMQfgQMjmnD4QOivtB1z6h3': 'file_storage/call_GmMQfgQMjmnD4QOivtB1z6h3.json', 'var_call_1Po7PcjbmLOEjWaYzsY1abY8': 'file_storage/call_1Po7PcjbmLOEjWaYzsY1abY8.json'}

exec(code, env_args)

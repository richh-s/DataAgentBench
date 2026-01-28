code = """import re, json, pandas as pd

with open(var_call_m2LLoEH16g84QXjTOGBj4QDc, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_npnDnK093QGTuFX57b7O0woa, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
pattern = re.compile(r'\((FEMA|CalOES|CalJPIA)[^)]*\)', re.IGNORECASE)
fund_df['is_disaster_name'] = fund_df['Project_Name'].str.contains(pattern)

disaster_names = set(fund_df[fund_df['is_disaster_name']]['Project_Name'].unique())

full_text = '\n'.join(doc['text'] for doc in civic_docs)

name_started_2022 = set()
for name in disaster_names:
    esc = re.escape(name)
    m = re.search(esc, full_text)
    if not m:
        continue
    window = full_text[m.end():m.end()+300]
    if '2022' in window:
        name_started_2022.add(name)

sel = fund_df[fund_df['Project_Name'].isin(name_started_2022)].copy()
sel['Amount'] = sel['Amount'].astype(int)

total = int(sel['Amount'].sum())

result = {"total_disaster_funding_started_2022": total}

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_m2LLoEH16g84QXjTOGBj4QDc': 'file_storage/call_m2LLoEH16g84QXjTOGBj4QDc.json', 'var_call_npnDnK093QGTuFX57b7O0woa': 'file_storage/call_npnDnK093QGTuFX57b7O0woa.json'}

exec(code, env_args)

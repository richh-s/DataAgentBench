code = """import re, json, pandas as pd
from pathlib import Path

# Load full mongo results
mongo_path = Path(var_call_LEH58jzPnHoprvp12gTDIXi3)
with mongo_path.open() as f:
    mongo_records = json.load(f)

# Heuristic extraction: year 2016 in text, and 'physical activity' phrase
selected = []
for doc in mongo_records:
    text = doc.get('text','')
    if '2016' not in text:
        continue
    if 'physical activity' not in text.lower():
        continue
    filename = doc.get('filename','')
    title = re.sub(r"\.txt$","", filename).strip()
    selected.append({'title': title})

# Load citation totals
cit_path = Path(var_call_pNN9a3TN3myVRs0mInASK6nc)
with cit_path.open() as f:
    cit_records = json.load(f)

cit_df = pd.DataFrame(cit_records)
# Clean title quotes and types
cit_df['title'] = cit_df['title'].astype(str).str.replace('^"|"$','', regex=True)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

sel_df = pd.DataFrame(selected).drop_duplicates()
merged = sel_df.merge(cit_df, on='title', how='left')

result = merged.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LEH58jzPnHoprvp12gTDIXi3': 'file_storage/call_LEH58jzPnHoprvp12gTDIXi3.json', 'var_call_pNN9a3TN3myVRs0mInASK6nc': 'file_storage/call_pNN9a3TN3myVRs0mInASK6nc.json'}

exec(code, env_args)

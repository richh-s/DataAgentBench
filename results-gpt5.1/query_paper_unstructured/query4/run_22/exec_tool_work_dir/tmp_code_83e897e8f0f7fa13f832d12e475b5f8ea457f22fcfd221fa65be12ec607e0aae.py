code = """import re, json, pandas as pd
from pathlib import Path

# Load full Mongo results
with open(var_call_L3XiCIOLoiudlex9peL3TnMr, 'r') as f:
    mongo_docs = json.load(f)

# Extract title (from filename) and year from text
records = []
for doc in mongo_docs:
    text = doc.get('text', '')
    # find a 4-digit year between 2010-2020 as publication year
    years = re.findall(r'20(1[0-9]|20)', text)
    pub_year = None
    for y in years:
        y_full = int('20' + y[-2:]) if len(y)==2 else int('20'+y) if len(y)==1 else int('20'+y[-2:])
        if 2010 <= y_full <= 2020:
            pub_year = y_full
            break
    if pub_year != 2016:
        continue
    title = doc.get('filename','').replace('.txt','').strip()
    # rudimentary domain filter: require 'physical activity' phrase in text
    if re.search(r'physical activity', text, re.I):
        records.append({'title': title})

# Load citations aggregation
with open(var_call_sYZlPB0JAxtjMJwNmCzpk3bw, 'r') as f:
    cites = json.load(f)

cites_df = pd.DataFrame(cites)
phys_titles = {r['title'] for r in records}

# Titles in citations DB should match exactly; compute totals
result_rows = []
for t in phys_titles:
    row = cites_df[cites_df['title'] == t]
    if not row.empty:
        total = int(row['total_citations'].iloc[0])
        result_rows.append({'title': t, 'total_citations': total})

result = json.dumps(result_rows)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_L3XiCIOLoiudlex9peL3TnMr': 'file_storage/call_L3XiCIOLoiudlex9peL3TnMr.json', 'var_call_sYZlPB0JAxtjMJwNmCzpk3bw': 'file_storage/call_sYZlPB0JAxtjMJwNmCzpk3bw.json'}

exec(code, env_args)

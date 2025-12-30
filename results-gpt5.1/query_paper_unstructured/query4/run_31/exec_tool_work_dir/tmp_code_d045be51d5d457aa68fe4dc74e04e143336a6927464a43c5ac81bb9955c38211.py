code = """import re, json
from pathlib import Path

# Load full Mongo result
path_docs = Path(var_call_JfgRZrKyiLbsKM96RkqEqtxj)
import pandas as pd
papers = pd.read_json(path_docs)

# Extract title (filename without .txt), year (4-digit near 'CHI' etc.), and filter domain/year
results = []
for _, row in papers.iterrows():
    text = row['text']
    # crude year extraction: first 4-digit between 2010-2020
    years = re.findall(r"20[0-2][0-9]", text)
    year = int(years[0]) if years else None
    title = row['filename'].replace('.txt','') if isinstance(row['filename'], str) else None
    # domain: ensure 'physical activity' phrase appears
    if year == 2016 and re.search(r"physical activity", text, re.I):
        results.append({'title': title, 'year': year})

# Load citations aggregated
path_cit = Path(var_call_HkXNhSsIh8idlSX4154fTEj9)
cit = pd.read_json(path_cit)

# Join on title
df_res = pd.DataFrame(results)
if not df_res.empty:
    merged = df_res.merge(cit, left_on='title', right_on='title', how='left')
    out = merged[['title','total_citations']].to_dict(orient='records')
else:
    out = []

s = json.dumps(out)
print("__RESULT__:")
print(s)"""

env_args = {'var_call_JfgRZrKyiLbsKM96RkqEqtxj': 'file_storage/call_JfgRZrKyiLbsKM96RkqEqtxj.json', 'var_call_HkXNhSsIh8idlSX4154fTEj9': 'file_storage/call_HkXNhSsIh8idlSX4154fTEj9.json'}

exec(code, env_args)

code = """import re, json, pandas as pd
from pathlib import Path

# Load full Mongo results
mongo_path = Path(var_call_FdqiJ7EvbSCbwlMKdmFbNjZ7)
with mongo_path.open() as f:
    mongo_records = json.load(f)

# Heuristic extraction of year and domain from text
rows = []
for doc in mongo_records:
    text = doc.get('text', '')
    # year: look for 2016 near conference header
    year = None
    m = re.search(r"\b(20\d{2})\b", text[:1000])
    if m:
        year = int(m.group(1))
    # domain: look for 'physical activity'
    domain = 'physical activity' if re.search(r'physical activity', text, re.I) else None
    if year == 2016 and domain == 'physical activity':
        title = doc.get('filename', '').replace('.txt', '')
        rows.append({'title': title, 'year': year, 'domain': domain})

# Load citations aggregation
sql_path = Path(var_call_jc5JgJQftHBdaNHcadBFAbvB)
with sql_path.open() as f:
    citation_records = json.load(f)

cit_df = pd.DataFrame(citation_records)
if not cit_df.empty:
    cit_df['total_citations'] = cit_df['total_citations'].astype(int)

papers_df = pd.DataFrame(rows)
if papers_df.empty:
    result = []
else:
    merged = papers_df.merge(cit_df, left_on='title', right_on='title', how='left')
    merged = merged[['title', 'total_citations']].fillna(0)
    result = merged.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_FdqiJ7EvbSCbwlMKdmFbNjZ7': 'file_storage/call_FdqiJ7EvbSCbwlMKdmFbNjZ7.json', 'var_call_jc5JgJQftHBdaNHcadBFAbvB': 'file_storage/call_jc5JgJQftHBdaNHcadBFAbvB.json'}

exec(code, env_args)

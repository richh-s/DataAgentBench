code = """import re, json, pandas as pd
from pathlib import Path

# Load full Mongo results
path_docs = Path(var_call_6RdYrPc2lXf6soQC9BYLQrKI)
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title (from filename), year, and domain heuristic (physical activity)
records = []
for d in docs:
    text = d.get('text', '')
    # year: prefer a 4-digit year starting with 201 in first 1000 chars
    m = re.search(r"20(\d{2})", text[:1000])
    year = int(m.group(0)) if m else None
    title = d.get('filename', '').replace('.txt','')
    domain = 'physical activity' if re.search(r'physical activity', text, re.I) else None
    records.append({'title': title, 'year': year, 'domain': domain})

papers_df = pd.DataFrame(records)

# Filter to 2016 and physical activity
pa_2016 = papers_df[(papers_df['year'] == 2016) & (papers_df['domain'] == 'physical activity')]

# Load citations aggregation
path_cit = Path(var_call_lwg0IwymXoZ3NCilw6zKtOJC)
with open(path_cit, 'r') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on title
merged = pa_2016.merge(cit_df, on='title', how='left')

result = merged[['title','total_citations']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_6RdYrPc2lXf6soQC9BYLQrKI': 'file_storage/call_6RdYrPc2lXf6soQC9BYLQrKI.json', 'var_call_lwg0IwymXoZ3NCilw6zKtOJC': 'file_storage/call_lwg0IwymXoZ3NCilw6zKtOJC.json'}

exec(code, env_args)

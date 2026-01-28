code = """import re, json, pandas as pd

# Load full citation aggregates
path_citations = var_call_rRyCCJjIeXibO90SPQaHwE89
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Build DataFrame
cit_df = pd.DataFrame(citations)
# Normalize types
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Load physical-activity-related papers from Mongo preview variable (all results are in memory)
papers = var_call_Lo1yoOeJf4coYqqVZSsBfy69

rows = []
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','')
    title = re.sub(r"\.txt$","", filename).strip()
    # extract year as first 4-digit year between, say, 2000 and 2025
    years = re.findall(r"(20[0-2][0-9]|19[0-9]{2})", text)
    pub_year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2025:
            pub_year = yi
            break
    if pub_year == 2016:
        rows.append({'title': title, 'year': pub_year})

pa_df = pd.DataFrame(rows)
if not pa_df.empty:
    merged = pa_df.merge(cit_df, on='title', how='left')
    merged = merged[['title','total_citations']].fillna(0)
    result = merged.to_dict(orient='records')
else:
    result = []

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Lo1yoOeJf4coYqqVZSsBfy69': 'file_storage/call_Lo1yoOeJf4coYqqVZSsBfy69.json', 'var_call_rRyCCJjIeXibO90SPQaHwE89': 'file_storage/call_rRyCCJjIeXibO90SPQaHwE89.json'}

exec(code, env_args)

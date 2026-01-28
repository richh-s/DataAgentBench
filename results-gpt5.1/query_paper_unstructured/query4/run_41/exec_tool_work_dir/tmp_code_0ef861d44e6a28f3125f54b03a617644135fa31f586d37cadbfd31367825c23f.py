code = """import re, json, pandas as pd

# Load full citations data
with open(var_call_adtZqXgSEjqptVUjeSQVCCWC, 'r') as f:
    citations = json.load(f)

# From paper docs preview, we can't filter by year/domain reliably; instead load all docs
# (assuming file path stored in var_call_RmT9mCXXGIzzI2kZkkNwMfHE)
with open(var_call_RmT9mCXXGIzzI2kZkkNwMfHE, 'r') as f:
    docs = json.load(f)

records = []
for d in docs:
    text = d.get('text', '')
    # Extract year: look for 2016 in the header; fallback: first 4-digit 20xx
    year = None
    m = re.search(r"20(\d{2})", text)
    if m:
        year_val = int('20' + m.group(1))
        if 2000 <= year_val <= 2025:
            year = year_val
    # Domain heuristic: if 'physical activity' substring
    domain_pa = 'physical activity' in text.lower()
    if year == 2016 and domain_pa:
        title = d.get('filename', '').replace('.txt','').strip()
        records.append({'title': title})

# Deduplicate titles
pa2016_titles = sorted({r['title'] for r in records})

# Build dataframe for citations
cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

result = []
for t in pa2016_titles:
    # Titles in SQLite may have different quoting; simple exact match and stripped quotes
    matches = cit_df[cit_df['title'].str.replace('"','').str.strip() == t.replace('"','').strip()]
    if not matches.empty:
        total = int(matches['total_citations'].iloc[0])
    else:
        total = 0
    result.append({'title': t, 'total_citations': total})

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_RmT9mCXXGIzzI2kZkkNwMfHE': 'file_storage/call_RmT9mCXXGIzzI2kZkkNwMfHE.json', 'var_call_adtZqXgSEjqptVUjeSQVCCWC': 'file_storage/call_adtZqXgSEjqptVUjeSQVCCWC.json'}

exec(code, env_args)

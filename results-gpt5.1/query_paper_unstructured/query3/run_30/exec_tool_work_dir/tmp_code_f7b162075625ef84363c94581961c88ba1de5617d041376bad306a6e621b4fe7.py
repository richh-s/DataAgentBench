code = """import re, json, pandas as pd

# Load full Mongo result
with open(var_call_5Is0aDVdieTma4drbLzMjqOF, 'r') as f:
    mongo_docs = json.load(f)

# Heuristic extract year and contribution from text
records = []
for doc in mongo_docs:
    text = doc.get('text', '')
    # year: look for CHI 2018-style or any 4-digit year 2017-2025
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None
    # contribution: look for 'contribution' section or keywords
    contrib = None
    lower = text.lower()
    if 'contribution' in lower or 'we contribute' in lower or 'our contributions' in lower:
        contrib = 'empirical' if 'study' in lower or 'participants' in lower or 'interview' in lower or 'survey' in lower or 'experiment' in lower else None
    # also simple contains check as per instructions
    if 'empirical' in lower:
        if contrib is None:
            contrib = 'empirical'
    # Only keep if empirical and year>2016
    if contrib == 'empirical' and year and year > 2016:
        title = doc.get('filename', '').replace('.txt','')
        records.append({'title': title, 'year': year})

# Load citations aggregated
with open(var_call_ZBv6tDIg2hydyrurisf4rXzb, 'r') as f:
    cit_rows = json.load(f)

cit_df = pd.DataFrame(cit_rows)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

papers_df = pd.DataFrame(records)

if not papers_df.empty:
    merged = papers_df.merge(cit_df, left_on='title', right_on='title', how='left')
    merged = merged[['title','total_citations']].dropna(subset=['total_citations']).drop_duplicates()
    result = merged.to_dict(orient='records')
else:
    result = []

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_5Is0aDVdieTma4drbLzMjqOF': 'file_storage/call_5Is0aDVdieTma4drbLzMjqOF.json', 'var_call_ZBv6tDIg2hydyrurisf4rXzb': 'file_storage/call_ZBv6tDIg2hydyrurisf4rXzb.json'}

exec(code, env_args)

code = """import re, json
import pandas as pd

# Load full mongo results
path_docs = var_call_3Wp2Oh5apYppjdMzuq8UJdfY
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title (from filename), year, and detect empirical contribution
records = []
for d in docs:
    filename = d.get('filename','')
    title = filename.replace('.txt','')
    text = d.get('text','')
    # year: regex for 20xx or 19xx near venue strings like CHI etc; fallback None
    year_match = re.search(r'CHI\s+(19|20)\d{2}|CSCW\s+(19|20)\d{2}|Ubicomp\s+(19|20)\d{2}|DIS\s+(19|20)\d{2}|PervasiveHealth\s+(19|20)\d{2}|IUI\s+(19|20)\d{2}|OzCHI\s+(19|20)\d{2}|TEI\s+(19|20)\d{2}|AH\s+(19|20)\d{2}', text)
    year = None
    if year_match:
        # last 4 digits in match
        year_digits = re.findall(r'(19|20)\d{2}', year_match.group(0))
        if year_digits:
            year = int(year_digits[-1])
    if not year:
        # fallback: first occurrence of 20xx or 19xx between 1990-2025
        m = re.search(r'(19|20)\d{2}', text)
        if m:
            y = int(m.group(0))
            if 1990 <= y <= 2025:
                year = y
    # empirical contribution: look for word 'empirical' in text
    contrib_empirical = bool(re.search(r'empirical', text, re.IGNORECASE))
    records.append({'title': title, 'year': year, 'empirical': contrib_empirical})

papers_df = pd.DataFrame(records)

# Load citations
path_cit = var_call_HuOUnYuuLJ56L3EztVtH4eN0
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
# total_citations is string, convert
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on title
merged = pd.merge(papers_df, cit_df, on='title', how='inner')

# Filter: empirical and year > 2016
res = merged[(merged['empirical']) & (merged['year'] > 2016)][['title','total_citations']].sort_values('title')

result = res.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3Wp2Oh5apYppjdMzuq8UJdfY': 'file_storage/call_3Wp2Oh5apYppjdMzuq8UJdfY.json', 'var_call_HuOUnYuuLJ56L3EztVtH4eN0': 'file_storage/call_HuOUnYuuLJ56L3EztVtH4eN0.json'}

exec(code, env_args)

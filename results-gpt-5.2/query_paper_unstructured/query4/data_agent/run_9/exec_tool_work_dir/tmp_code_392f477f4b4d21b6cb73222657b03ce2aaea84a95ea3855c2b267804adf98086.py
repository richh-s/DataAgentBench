code = """import json, re
import pandas as pd

def load_mongo_result(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_docs = load_mongo_result(var_call_bPxDJPrrsdxrcjTrwJOJGmCr)

# Extract publication year from text using common patterns
patterns = [
    re.compile(r'(?i)\bCHI\s*2016\b'),
    re.compile(r'(?i)\bUbiComp\s*2016\b'),
    re.compile(r'(?i)\bCSCW\s*2016\b'),
    re.compile(r'(?i)\bDIS\s*2016\b'),
    re.compile(r'(?i)\bIUI\s*2016\b'),
    re.compile(r'(?i)\bWWW\s*2016\b'),
    re.compile(r'(?i)\bPervasiveHealth\s*2016\b'),
    re.compile(r'(?i)\bOzCHI\s*2016\b'),
    re.compile(r'(?i)\bTEI\s*2016\b'),
    re.compile(r'(?i)\bAH\s*2016\b'),
    re.compile(r'(?i)\bCopyright\s*(?:\(c\)\s*)?2016\b'),
    re.compile(r'(?i)\b2016\b')
]

def is_2016(text):
    if not text:
        return False
    # require a fairly strong signal: venue year or copyright 2016
    if patterns[0].search(text) or patterns[1].search(text) or patterns[2].search(text) or patterns[3].search(text) or patterns[4].search(text) or patterns[5].search(text) or patterns[6].search(text) or patterns[7].search(text) or patterns[8].search(text) or patterns[9].search(text):
        return True
    if patterns[10].search(text):
        return True
    # fallback: any 2016 but exclude clearly different years like 2017-2020 in header lines? too risky; keep as True if 2016 present.
    return bool(patterns[11].search(text))

rows = []
for d in paper_docs:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','')
    if is_2016(text):
        rows.append({'title': title})

# Deduplicate titles
titles_2016 = sorted(set(r['title'] for r in rows))

# citations totals
cit = var_call_HJPthmNZALmSVKQBM7AHsIhC
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

df_cit = pd.DataFrame(cit)
# coerce numeric
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

df_titles = pd.DataFrame({'title': titles_2016})
res = df_titles.merge(df_cit, on='title', how='left')
res['total_citations'] = res['total_citations'].fillna(0).astype(int)

# Only physical activity domain: already filtered by regex in mongo, but ensure via title/text? We'll keep as is.
res = res.sort_values(['total_citations','title'], ascending=[False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bPxDJPrrsdxrcjTrwJOJGmCr': 'file_storage/call_bPxDJPrrsdxrcjTrwJOJGmCr.json', 'var_call_HJPthmNZALmSVKQBM7AHsIhC': 'file_storage/call_HJPthmNZALmSVKQBM7AHsIhC.json'}

exec(code, env_args)

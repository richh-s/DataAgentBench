code = """import json, re
import pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load(var_call_9GZi2toXa4a5rd2z4Ie0MB7h)

# Determine publication year by looking for common venue-year strings or copyright year
venue_year_re = re.compile(r'(?i)\b(chi|ubicomp|cscw|dis|iui|www|pervasivehealth|ozchi|tei|ah)\s*[\'’`]?\s*\(?\s*16\s*\)?\b|\b(chi|ubicomp|cscw|dis|iui|www|pervasivehealth|ozchi|tei|ah)\s*2016\b')
copyright_re = re.compile(r'(?i)\bCopyright\s*(?:\(c\)\s*)?2016\b')
year2016_re = re.compile(r'\b2016\b')

def published_2016(text):
    if not text:
        return False
    if venue_year_re.search(text):
        return True
    if copyright_re.search(text):
        return True
    # weaker: 2016 near beginning
    head = text[:1500]
    return bool(year2016_re.search(head))

published_titles = []
for d in docs:
    t = d.get('text','')
    if published_2016(t):
        title = d.get('filename','')
        if title.lower().endswith('.txt'):
            title = title[:-4]
        published_titles.append(title)

published_titles = sorted(set(published_titles))

# Load citations totals (already aggregated)
cit = load(var_call_HJPthmNZALmSVKQBM7AHsIhC)
df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

df = pd.DataFrame({'title': published_titles})
res = df.merge(df_cit, on='title', how='left')
res['total_citations'] = res['total_citations'].fillna(0).astype(int)
res = res.sort_values(['total_citations','title'], ascending=[False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bPxDJPrrsdxrcjTrwJOJGmCr': 'file_storage/call_bPxDJPrrsdxrcjTrwJOJGmCr.json', 'var_call_HJPthmNZALmSVKQBM7AHsIhC': 'file_storage/call_HJPthmNZALmSVKQBM7AHsIhC.json', 'var_call_nAYC7LC2u7ZLdEsWP40Rr6T2': [], 'var_call_9GZi2toXa4a5rd2z4Ie0MB7h': 'file_storage/call_9GZi2toXa4a5rd2z4Ie0MB7h.json'}

exec(code, env_args)

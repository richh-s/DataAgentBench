code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_maybe_path(var_call_UvXhsCnXZ7Sjwow7gHUODKNR)
cits = load_maybe_path(var_call_tExXsXwagXZ3wW1LVAUu9Scr)

docs_df = pd.DataFrame(docs)
# title from filename
if 'filename' in docs_df.columns:
    docs_df['title'] = docs_df['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    docs_df['title'] = None

# extract publication year: first 4-digit year between 1990-2026 in first 3000 chars
pat_year = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    if not isinstance(text, str):
        return None
    head = text[:4000]
    yrs = [int(m.group(1)) for m in pat_year.finditer(head)]
    yrs = [y for y in yrs if 1990 <= y <= 2026]
    if not yrs:
        return None
    # use minimum in head as likely publication year
    return min(yrs)

docs_df['pub_year'] = docs_df['text'].apply(extract_year)

# contribution: contains 'empirical'
docs_df['is_empirical'] = docs_df['text'].str.contains(r'\bempirical\b', case=False, na=False)

filtered = docs_df[(docs_df['is_empirical']) & (docs_df['pub_year'].notna()) & (docs_df['pub_year'] > 2016)][['title','pub_year']]

cits_df = pd.DataFrame(cits)
# ensure numeric
if 'total_citations' in cits_df.columns:
    cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce')

out = filtered.merge(cits_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True])
res = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_UvXhsCnXZ7Sjwow7gHUODKNR': 'file_storage/call_UvXhsCnXZ7Sjwow7gHUODKNR.json', 'var_call_tExXsXwagXZ3wW1LVAUu9Scr': 'file_storage/call_tExXsXwagXZ3wW1LVAUu9Scr.json'}

exec(code, env_args)

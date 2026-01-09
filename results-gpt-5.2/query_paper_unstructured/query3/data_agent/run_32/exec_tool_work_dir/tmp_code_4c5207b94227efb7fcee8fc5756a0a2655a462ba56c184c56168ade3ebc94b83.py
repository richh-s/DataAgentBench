code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_docs = load_records(var_call_X1otFK7bGW5GM8TVjJB7QrCw)
cits = load_records(var_call_X70sFsGGZBlyCgx6OqKE5McP)

df_docs = pd.DataFrame(paper_docs)
df_cits = pd.DataFrame(cits)

# title from filename
if 'filename' in df_docs.columns:
    df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_docs['title'] = None

# extract year: prefer explicit 4-digit year 19xx/20xx; take max (often publication year appears in header)
year_pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    if not isinstance(text, str):
        return None
    years = [int(y) for y in year_pat.findall(text)]
    if not years:
        return None
    # heuristic: publication year likely between 2000 and 2026; take max but cap reasonable
    years = [y for y in years if 1970 <= y <= 2026]
    if not years:
        return None
    return max(years)

df_docs['year'] = df_docs['text'].apply(extract_year)

# contribution: substring match in text for 'empirical'

def has_empirical(text):
    if not isinstance(text, str):
        return False
    return 'empirical' in text.lower()

df_docs['is_empirical'] = df_docs['text'].apply(has_empirical)

# filter
filtered = df_docs[(df_docs['is_empirical']) & (df_docs['year'].notna()) & (df_docs['year'] > 2016)][['title','year']]

# join with citations totals
# normalize titles whitespace
filtered['title_norm'] = filtered['title'].str.strip()
df_cits['title_norm'] = df_cits['title'].astype(str).str.strip()

# total_citations may be string
if 'total_citations' in df_cits.columns:
    df_cits['total_citations'] = pd.to_numeric(df_cits['total_citations'], errors='coerce')

out = filtered.merge(df_cits[['title_norm','total_citations']], on='title_norm', how='left')
# choose title from docs
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

# aggregate in case duplicates
out2 = out.groupby(['title_norm'], as_index=False).agg(title=('title_norm','first'), total_citations=('total_citations','max'))
out2 = out2.sort_values(['total_citations','title'], ascending=[False, True])

result = out2[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_X1otFK7bGW5GM8TVjJB7QrCw': 'file_storage/call_X1otFK7bGW5GM8TVjJB7QrCw.json', 'var_call_X70sFsGGZBlyCgx6OqKE5McP': 'file_storage/call_X70sFsGGZBlyCgx6OqKE5McP.json'}

exec(code, env_args)

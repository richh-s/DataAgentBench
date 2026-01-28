code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_bnWsofWCjS9TDlhBuXBX6EPL)
reviews = load_records(var_call_Gp5ZibnmE9kPymtVlTHeVGwi)

df_b = pd.DataFrame(books)
df_r = pd.DataFrame(reviews)

# parse year from details
pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    # prefer year near 'on' or 'released' or 'published'
    m = re.search(r'(?:released|published|publication|edition).*?(18\d{2}|19\d{2}|20\d{2})', s, flags=re.I)
    if m:
        return int(m.group(1))
    # else first plausible year
    m2 = pat.search(s)
    if m2:
        return int(m2.group(1))
    return None

df_b['year'] = df_b['details'].map(extract_year)
df_b = df_b.dropna(subset=['year'])
df_b['decade'] = (df_b['year']//10)*10

# fuzzy join purchaseid_<n> to bookid_<n>

def norm_id(x):
    if not isinstance(x, str):
        return None
    m = re.search(r'_(\d+)$', x)
    return m.group(1) if m else None

df_b['idnum'] = df_b['book_id'].map(norm_id)
df_r['idnum'] = df_r['purchase_id'].map(norm_id)

# ratings to float

df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['rating','idnum'])
df_b = df_b.dropna(subset=['idnum'])

# map idnum -> decade (if multiple book entries, take min year)
df_b_min = df_b.sort_values('year').drop_duplicates('idnum', keep='first')[['idnum','decade']]

df = df_r.merge(df_b_min, on='idnum', how='inner')
# distinct books rated per decade
books_per_decade = df[['idnum','decade']].drop_duplicates().groupby('decade').size().rename('distinct_books')
mean_rating = df.groupby('decade')['rating'].mean().rename('avg_rating')
summary = pd.concat([books_per_decade, mean_rating], axis=1).dropna().reset_index()
summary = summary[summary['distinct_books']>=10]
if summary.empty:
    out = None
else:
    best = summary.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
    out = f"{int(best['decade'])}s"

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bnWsofWCjS9TDlhBuXBX6EPL': 'file_storage/call_bnWsofWCjS9TDlhBuXBX6EPL.json', 'var_call_WqGx47xfzfQkzgonWp9J9x6t': ['review'], 'var_call_Gp5ZibnmE9kPymtVlTHeVGwi': 'file_storage/call_Gp5ZibnmE9kPymtVlTHeVGwi.json'}

exec(code, env_args)

code = """import json, re, pandas as pd

# load reviews
p = var_call_OKkAF21mQdkUTaYurKkPXmsB
with open(p, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
dfr = pd.DataFrame(reviews)
dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')
dfr = dfr.dropna(subset=['purchase_id','rating'])

# load books details
bp = var_call_YnIAuKW256ykqUu57964O2bB
with open(bp, 'r', encoding='utf-8') as f:
    books = json.load(f)
dfb = pd.DataFrame(books)
dfb = dfb.dropna(subset=['book_id','details'])

# extract year from details
year_re = re.compile(r'\b(19\d{2}|20\d{2}|18\d{2}|17\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = year_re.search(s)
    if not m:
        return None
    y = int(m.group(1))
    # keep plausible publication years
    if 1500 <= y <= 2026:
        return y
    return None

dfb['year'] = dfb['details'].map(extract_year)
dfb = dfb.dropna(subset=['year'])
dfb['year'] = dfb['year'].astype(int)
dfb['decade_start'] = (dfb['year']//10)*10

# join via numeric suffix mapping purchaseid_X -> bookid_X
suf_re = re.compile(r'(\d+)')

def suffix(x):
    if not isinstance(x, str):
        return None
    m = suf_re.search(x)
    return m.group(1) if m else None

dfr['sid'] = dfr['purchase_id'].map(suffix)
dfb['sid'] = dfb['book_id'].map(suffix)

# keep only rated books: purchase_id with at least one rating
# join on sid
j = dfr.merge(dfb[['sid','decade_start']], on='sid', how='inner')

# compute decade stats; require at least 10 distinct books (sid) rated
stats = j.groupby('decade_start').agg(
    avg_rating=('rating','mean'),
    distinct_books=('sid','nunique')
).reset_index()

stats = stats[stats['distinct_books']>=10]
if len(stats)==0:
    out = None
else:
    best = stats.sort_values(['avg_rating','distinct_books','decade_start'], ascending=[False,False,True]).iloc[0]
    out = f"{int(best['decade_start'])}s"

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YnIAuKW256ykqUu57964O2bB': 'file_storage/call_YnIAuKW256ykqUu57964O2bB.json', 'var_call_dCYaOyPHLJHl3Upz7FRgk02m': ['review'], 'var_call_OKkAF21mQdkUTaYurKkPXmsB': 'file_storage/call_OKkAF21mQdkUTaYurKkPXmsB.json'}

exec(code, env_args)

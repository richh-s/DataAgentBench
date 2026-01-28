code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load_records(var_call_Pj2KBRPN4bB3qqDOrpPp3Dm1)
books = load_records(var_call_b1E0ZfYMOf4K46XiCiAOCX5q)

df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

df_b = pd.DataFrame(books)
# extract first 4-digit year from details
pat = re.compile(r'\b(1[5-9]\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = pat.search(s)
    if not m:
        return None
    y = int(m.group(1))
    if 1500 <= y <= 2026:
        return y
    return None

df_b['year'] = df_b['details'].map(extract_year)
df_b = df_b.dropna(subset=['book_id','year'])
df_b['year'] = df_b['year'].astype(int)

# fuzzy join: purchaseid_123 -> bookid_123
# extract trailing digits
get_num = lambda x: re.search(r'(\d+)$', str(x)).group(1) if re.search(r'(\d+)$', str(x)) else None

df_r['num'] = df_r['purchase_id'].map(get_num)
df_b['num'] = df_b['book_id'].map(get_num)

df = df_r.merge(df_b[['num','year']], on='num', how='inner')

# decade label
df['decade_start'] = (df['year']//10)*10
df['decade'] = df['decade_start'].astype(int).astype(str) + 's'

# count distinct books (num) per decade and avg rating across all reviews
agg = df.groupby('decade').agg(distinct_books=('num', pd.Series.nunique), avg_rating=('rating','mean')).reset_index()
agg = agg[agg['distinct_books']>=10]
if len(agg)==0:
    out = {"decade": None, "avg_rating": None}
else:
    top = agg.sort_values(['avg_rating','distinct_books'], ascending=[False,False]).iloc[0]
    out = {"decade": top['decade'], "avg_rating": float(top['avg_rating']), "distinct_books": int(top['distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_b1E0ZfYMOf4K46XiCiAOCX5q': 'file_storage/call_b1E0ZfYMOf4K46XiCiAOCX5q.json', 'var_call_4dtiFeYlCAIcvmcIO1JFxy9w': ['review'], 'var_call_Pj2KBRPN4bB3qqDOrpPp3Dm1': 'file_storage/call_Pj2KBRPN4bB3qqDOrpPp3Dm1.json'}

exec(code, env_args)

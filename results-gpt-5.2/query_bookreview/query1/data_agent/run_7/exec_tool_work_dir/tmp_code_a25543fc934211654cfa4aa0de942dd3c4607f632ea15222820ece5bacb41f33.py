code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load_records(var_call_vPC0zFlaCTyw14OuhYKTIqCw)
books = load_records(var_call_7I4bhnkbIOljWNwzPjVEqtTX)

df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

df_b = pd.DataFrame(books)
# extract year from details
pat = re.compile(r'\b(17\d{2}|18\d{2}|19\d{2}|20\d{2})\b')

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
df_b['decade_start'] = (df_b['year']//10)*10

df = df_r.merge(df_b[['book_id','decade_start']], left_on='purchase_id', right_on='book_id', how='inner')
# group by decade: average rating across all reviews, only decades with >=10 distinct books rated
agg = df.groupby('decade_start').agg(avg_rating=('rating','mean'), distinct_books=('book_id','nunique'))
agg = agg[agg['distinct_books']>=10]
if agg.empty:
    out = None
else:
    best = agg.sort_values(['avg_rating','distinct_books'], ascending=[False,False]).head(1)
    decade = int(best.index[0])
    out = f"{decade}s"

print('__RESULT__:')
print(json.dumps({'decade': out}))"""

env_args = {'var_call_Jyzs4xCLg4SomqpxFEtrGM26': ['review'], 'var_call_VNBPV8j9yDOd019dUwlzjfpD': ['books_info'], 'var_call_vPC0zFlaCTyw14OuhYKTIqCw': 'file_storage/call_vPC0zFlaCTyw14OuhYKTIqCw.json', 'var_call_7I4bhnkbIOljWNwzPjVEqtTX': 'file_storage/call_7I4bhnkbIOljWNwzPjVEqtTX.json'}

exec(code, env_args)

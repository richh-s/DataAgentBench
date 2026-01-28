code = """import json, re
import pandas as pd

def load(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

reviews = load(var_call_iP4n4V9tuo4eOArzdfRn6ekC)
books = load(var_call_MbCIAE7ldfHOwh0hB9bDcLgR)

df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
df_r = df_r.dropna(subset=['purchase_id','rating'])

df_b = pd.DataFrame(books)

def extract_year(s):
    if s is None:
        return None
    m = re.search(r'\b(19\d{2}|20\d{2})\b', str(s))
    if not m:
        return None
    y = int(m.group(1))
    if y < 1000 or y > 2026:
        return None
    return y

df_b['year'] = df_b['details'].map(extract_year)
df_b = df_b.dropna(subset=['book_id','year'])
df_b['year'] = df_b['year'].astype(int)

# fuzzy join: ids like purchaseid_186 vs bookid_186

def num_suffix(x):
    m = re.search(r'(\d+)$', str(x))
    return int(m.group(1)) if m else None

df_r['num'] = df_r['purchase_id'].map(num_suffix)
df_b['num'] = df_b['book_id'].map(num_suffix)

j = df_r.merge(df_b[['num','book_id','year']], on='num', how='inner')
# require rated books: distinct books with >=1 rating already by construction
j['decade'] = (j['year']//10)*10

agg = j.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id','nunique')
).reset_index()
agg = agg[agg['distinct_books']>=10]
if agg.empty:
    out = None
else:
    best = agg.sort_values(['avg_rating','distinct_books','decade'], ascending=[False,False,True]).iloc[0]
    out = f"{int(best['decade'])}s"

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MbCIAE7ldfHOwh0hB9bDcLgR': 'file_storage/call_MbCIAE7ldfHOwh0hB9bDcLgR.json', 'var_call_s65RDICBjwtZnHfNUi8324hW': ['review'], 'var_call_iP4n4V9tuo4eOArzdfRn6ekC': 'file_storage/call_iP4n4V9tuo4eOArzdfRn6ekC.json'}

exec(code, env_args)

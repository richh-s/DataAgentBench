code = """import json, pandas as pd

# load reviews
path_reviews = var_call_v2wcdQFmmawaWvPcV8HcXIon
with open(path_reviews, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
# rating can be string
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# compute avg rating and count per purchase_id
agg = df_r.groupby('purchase_id', dropna=True)['rating'].agg(['mean','count']).reset_index()
agg = agg[agg['mean'] >= 4.5]

# load books
path_books = var_call_cCNXu4GM9l8kfYWzpu9BJjn9
with open(path_books, 'r') as f:
    books = json.load(f)
df_b = pd.DataFrame(books)

# only children's books
df_b['is_childrens'] = df_b['categories'].fillna('').str.contains("Children's Books", regex=False)
df_cb = df_b[df_b['is_childrens']].copy()

# fuzzy join: purchase_id like purchaseid_XX, book_id like bookid_XX -> extract numeric suffix
import re

def suffix_num(s):
    if s is None:
        return None
    m = re.search(r'(\d+)$', str(s))
    return int(m.group(1)) if m else None

agg['id_num'] = agg['purchase_id'].apply(suffix_num)
df_cb['id_num'] = df_cb['book_id'].apply(suffix_num)

merged = pd.merge(agg, df_cb, on='id_num', how='inner')
merged = merged[['title','book_id','purchase_id','mean','count']].sort_values(['mean','count','title'], ascending=[False,False,True])

result = merged.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cCNXu4GM9l8kfYWzpu9BJjn9': 'file_storage/call_cCNXu4GM9l8kfYWzpu9BJjn9.json', 'var_call_ERlBCGKie7G1mPhkpw88GyPZ': ['review'], 'var_call_v2wcdQFmmawaWvPcV8HcXIon': 'file_storage/call_v2wcdQFmmawaWvPcV8HcXIon.json'}

exec(code, env_args)

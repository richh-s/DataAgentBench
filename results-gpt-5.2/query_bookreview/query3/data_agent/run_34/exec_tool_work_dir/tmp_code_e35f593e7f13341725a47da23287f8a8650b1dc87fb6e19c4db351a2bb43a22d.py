code = """import json, pandas as pd
from pathlib import Path

def load(maybe_path_or_obj):
    if isinstance(maybe_path_or_obj, str) and maybe_path_or_obj.endswith('.json') and Path(maybe_path_or_obj).exists():
        return json.loads(Path(maybe_path_or_obj).read_text())
    return maybe_path_or_obj

books = load(var_call_h197diQPVOjRBZMIdqB0J8PH)
reviews = load(var_call_oUG1Zv1KbuQRbMq8XYZgfpVY)

df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# normalize ids: purchaseid_123 <-> bookid_123

def id_num(x):
    if pd.isna(x):
        return None
    s = str(x)
    digits = ''.join([c for c in s if c.isdigit()])
    return digits if digits else None

# filter children's books via categories string contains
mask_child = df_books['categories'].fillna('').str.contains("Children's Books", regex=False)
df_child = df_books[mask_child].copy()
df_child['idnum'] = df_child['book_id'].map(id_num)

df_reviews['idnum'] = df_reviews['purchase_id'].map(id_num)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

merged = df_reviews.merge(df_child[['book_id','title','idnum']], on='idnum', how='inner')

agg = merged.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count','title'], ascending=[False,False,True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_h197diQPVOjRBZMIdqB0J8PH': 'file_storage/call_h197diQPVOjRBZMIdqB0J8PH.json', 'var_call_tYJI0Io1FAZu1abEVlp3WLtF': ['review'], 'var_call_oUG1Zv1KbuQRbMq8XYZgfpVY': 'file_storage/call_oUG1Zv1KbuQRbMq8XYZgfpVY.json'}

exec(code, env_args)

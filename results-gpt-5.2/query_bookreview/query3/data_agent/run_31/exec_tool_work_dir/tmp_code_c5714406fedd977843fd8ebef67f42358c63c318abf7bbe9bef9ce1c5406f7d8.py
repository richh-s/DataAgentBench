code = """import json, pandas as pd

# load reviews
p_reviews = var_call_ZnvrVRdgJTJxNmdldCLp7DEn
with open(p_reviews, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# load books
p_books = var_call_KgZuLY2Ev31mPjzISUAI1iuV
with open(p_books, 'r') as f:
    books = json.load(f)
df_b = pd.DataFrame(books)

# filter Children's Books by substring in categories string
mask_children = df_b['categories'].fillna('').str.contains("Children's Books", regex=False)
df_b_child = df_b.loc[mask_children, ['book_id','title','categories']].copy()

# fuzzy join purchaseid_X -> bookid_X by extracting numeric suffix
for col, newcol in [('purchase_id','key'), ('book_id','key')]:
    pass

df_r['key'] = df_r['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]
df_b_child['key'] = df_b_child['book_id'].astype(str).str.extract(r'(\d+)$')[0]

# join and aggregate
merged = df_r.merge(df_b_child, on='key', how='inner', suffixes=('_review','_book'))
agg = merged.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating']>=4.5].sort_values(['avg_rating','review_count','title'], ascending=[False,False,True])

out_lines = []
for _, row in res.iterrows():
    out_lines.append(f"{row['title']} (avg rating {row['avg_rating']:.2f} from {int(row['review_count'])} reviews since 2020)")
answer = "\n".join(out_lines) if out_lines else "No Children's Books found with average rating >= 4.5 based on reviews from 2020 onwards."

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_KgZuLY2Ev31mPjzISUAI1iuV': 'file_storage/call_KgZuLY2Ev31mPjzISUAI1iuV.json', 'var_call_slu3ZASUNdbWJF5CRrJ0mxV0': ['review'], 'var_call_ZnvrVRdgJTJxNmdldCLp7DEn': 'file_storage/call_ZnvrVRdgJTJxNmdldCLp7DEn.json'}

exec(code, env_args)

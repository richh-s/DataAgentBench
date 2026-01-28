code = """import json, pandas as pd

# load books
books_path = var_call_6OhAxNEGf3qsLzYn0LLeOq5X
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
books_df = pd.DataFrame(books)

# load reviews (2020+)
reviews_path = var_call_I3Sfpv6wdlexxlZ5rtNut6v2
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
rev_df = pd.DataFrame(reviews)

# filter children's books by categories string contains
books_df['is_childrens'] = books_df['categories'].fillna('').str.contains("Children's Books", regex=False)
child_books = books_df[books_df['is_childrens']].copy()

# fuzzy join purchase_id -> book_id by numeric suffix
child_books['id_num'] = child_books['book_id'].str.extract(r'(\d+)$')[0]
rev_df['id_num'] = rev_df['purchase_id'].str.extract(r'(\d+)$')[0]

rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

merged = rev_df.merge(child_books[['book_id','title','categories','id_num']], on='id_num', how='inner')

grp = merged.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = grp[grp['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count'], ascending=[False, False])

# format answer lines
lines = []
for _, r in res.iterrows():
    lines.append(f"{r['title']} (book_id: {r['book_id']}): avg_rating={r['avg_rating']:.2f} from {int(r['review_count'])} reviews (2020+)")

answer = "No matching books found." if len(lines)==0 else "\n".join(lines)

print('__RESULT__:')
print(json.dumps({'answer': answer}))"""

env_args = {'var_call_6OhAxNEGf3qsLzYn0LLeOq5X': 'file_storage/call_6OhAxNEGf3qsLzYn0LLeOq5X.json', 'var_call_xoURwmHYBaUpzKcB884QdXJu': ['review'], 'var_call_I3Sfpv6wdlexxlZ5rtNut6v2': 'file_storage/call_I3Sfpv6wdlexxlZ5rtNut6v2.json'}

exec(code, env_args)

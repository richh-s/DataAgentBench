code = """import json, pandas as pd

rev_src = var_call_NroCOalgwaUpd88cM3ow0W47
if isinstance(rev_src, str) and rev_src.endswith('.json'):
    with open(rev_src, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
else:
    reviews = rev_src

books_src = var_call_qFsvMIaY6MjG7hSOCplORy02
if isinstance(books_src, str) and books_src.endswith('.json'):
    with open(books_src, 'r', encoding='utf-8') as f:
        books = json.load(f)
else:
    books = books_src

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

rev_df['id_num'] = rev_df['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]
books_df['id_num'] = books_df['book_id'].astype(str).str.extract(r'(\d+)$')[0]
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

books_df['is_childrens'] = books_df['categories'].astype(str).str.contains("Children's Books", na=False)
child_books = books_df[books_df['is_childrens']].copy()

joined = rev_df.merge(child_books[['book_id','title','categories','id_num']], on='id_num', how='inner')
agg = joined.groupby(['book_id','title'], as_index=False).agg(avg_rating=('rating','mean'), review_count=('rating','size'))
res = agg[agg['avg_rating'] >= 4.5].sort_values(['avg_rating','review_count','title'], ascending=[False, False, True])

lines = []
for _, r in res.iterrows():
    line = '{} (book_id: {}) - avg_rating={:.2f} (n={})'.format(r['title'], r['book_id'], r['avg_rating'], int(r['review_count']))
    lines.append(line)

answer = "\n".join(lines) if len(lines)>0 else "No Children's Books meet the criteria (avg rating >= 4.5 from reviews in 2020+)."

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_qFsvMIaY6MjG7hSOCplORy02': 'file_storage/call_qFsvMIaY6MjG7hSOCplORy02.json', 'var_call_TdMBZtaPP5efKtL1HvnMBOeh': ['review'], 'var_call_NroCOalgwaUpd88cM3ow0W47': 'file_storage/call_NroCOalgwaUpd88cM3ow0W47.json'}

exec(code, env_args)

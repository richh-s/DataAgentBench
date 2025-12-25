code = """import json, pandas as pd

books_path = var_call_2PKAVmd6q3JCbdA0wdPAYIOp
with open(books_path, 'r') as f:
    books = json.load(f)
reviews_path = var_call_jYxAwZoPOG259yxqLqssOePC
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

books_df['is_children'] = books_df['categories'].astype(str).str.contains("Children's Books", regex=False)
children_books = books_df[books_df['is_children']]

reviews_df['rating'] = reviews_df['rating'].astype(float)

merged = reviews_df.merge(children_books[['book_id','title']], left_on='purchase_id', right_on='book_id', how='inner')

avg_ratings = merged.groupby(['book_id','title'])['rating'].mean().reset_index()

result_df = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_2PKAVmd6q3JCbdA0wdPAYIOp': 'file_storage/call_2PKAVmd6q3JCbdA0wdPAYIOp.json', 'var_call_dB79UwGGcoB3ntGfzDs0PyK1': ['review'], 'var_call_jYxAwZoPOG259yxqLqssOePC': 'file_storage/call_jYxAwZoPOG259yxqLqssOePC.json'}

exec(code, env_args)

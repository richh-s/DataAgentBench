code = """import json, pandas as pd

books_file = var_call_EtFlvuIDD52crzDgEaMiXkvg
reviews_file = var_call_3EZvcNj7HIITo8twuMDQC6jz

with open(books_file, 'r') as f:
    books = json.load(f)
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

children_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

merged = reviews_df.merge(children_books, left_on='purchase_id', right_on='book_id', how='inner')

merged['rating'] = merged['rating'].astype(float)

avg_ratings = merged.groupby(['book_id', 'title'])['rating'].mean().reset_index()

result_df = avg_ratings[avg_ratings['rating'] >= 4.5].sort_values('rating', ascending=False)

result = result_df.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EtFlvuIDD52crzDgEaMiXkvg': 'file_storage/call_EtFlvuIDD52crzDgEaMiXkvg.json', 'var_call_vc1FMlTWmeXan1iUj5tQwQYj': ['review'], 'var_call_3EZvcNj7HIITo8twuMDQC6jz': 'file_storage/call_3EZvcNj7HIITo8twuMDQC6jz.json'}

exec(code, env_args)

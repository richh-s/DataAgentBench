code = """import json
import pandas as pd

books_file = locals()['var_functions.query_db:2']
with open(books_file, 'r') as f:
    books_data = json.load(f)

reviews_file = locals()['var_functions.query_db:6']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

print('Books dataframe shape:', books_df.shape)
print('Books columns:', books_df.columns.tolist())
print('\nReviews dataframe shape:', reviews_df.shape)
print('Reviews columns:', reviews_df.columns.tolist())

print('\nBooks data sample:')
print(books_df.head(2).to_string())
print('\nReviews data sample:')
print(reviews_df.head(5).to_string())

print('\nSample purchase IDs from reviews:')
print(reviews_df['purchase_id'].head(10).tolist())
print('\nSample book IDs from books:')
print(books_df['book_id'].head(10).tolist())"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

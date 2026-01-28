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

print('Books shape:', books_df.shape)
print('Reviews shape:', reviews_df.shape)

print('Books columns:', list(books_df.columns))
print('Reviews columns:', list(reviews_df.columns))

print('\nFirst book row:')
print(books_df.iloc[0].to_dict())

print('\nFirst review rows:')
print(reviews_df.head(3).to_dict('records'))

# Check categories field
print('\nCategories field type and sample:', type(books_df['categories'].iloc[0]))
print(books_df['categories'].iloc[0])"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

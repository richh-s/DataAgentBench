code = """import json
import pandas as pd

# Load books data
books_file = var_functions.query_db:0
with open(books_file, 'r') as f:
    books_data = json.load(f)

books_df = pd.DataFrame(books_data)
print('Books columns:', books_df.columns.tolist())
print('Books shape:', books_df.shape)

# Check categories column
print('\nSample categories entries:')
for i, cat in enumerate(books_df['categories'].head()):
    print(f"{i}: {cat}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Load books data
books_file = var_functions.query_db:0
with open(books_file, 'r') as f:
    books_data = json.load(f)

books_df = pd.DataFrame(books_data)
print('__RESULT__:')
print(json.dumps({
    'columns': books_df.columns.tolist(),
    'shape': books_df.shape,
    'sample': books_df[['title', 'book_id', 'categories']].head().to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

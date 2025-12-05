code = """import json, pandas as pd
from pathlib import Path

path = var_call_GuxX3F8FDWh7czndNVYM5d7a
with open(path, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)][['book_id', 'title']]

result = child_books.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GuxX3F8FDWh7czndNVYM5d7a': 'file_storage/call_GuxX3F8FDWh7czndNVYM5d7a.json'}

exec(code, env_args)

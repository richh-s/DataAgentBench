code = """import json, pandas as pd, ast, os

path = var_call_CFxJJKCKwqr6ub1gcap6a1kI
with open(path, 'r') as f:
    books = json.load(f)

books_df = pd.DataFrame(books)

# Filter for Children's Books in categories string
children = books_df[books_df['categories'].str.contains("Children's Books", na=False)]

result = children[['book_id', 'title']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CFxJJKCKwqr6ub1gcap6a1kI': 'file_storage/call_CFxJJKCKwqr6ub1gcap6a1kI.json'}

exec(code, env_args)

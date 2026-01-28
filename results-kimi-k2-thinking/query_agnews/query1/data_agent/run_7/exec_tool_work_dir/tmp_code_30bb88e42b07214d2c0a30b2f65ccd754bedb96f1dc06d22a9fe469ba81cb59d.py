code = """import json
import os

# Try to access the stored variable
articles = locals()['var_functions.query_db:2']

# If it's a string that looks like a file path, open and read it
if isinstance(articles, str):
    with open(articles, 'r') as f:
        articles = json.load(f)

print("Total articles loaded:", len(articles))
print("First article:", articles[0])

# Calculate description lengths
desc_lengths = [(article.get('title'), article.get('description'), len(article.get('description', ''))) for article in articles]
desc_lengths.sort(key=lambda x: x[2], reverse=True)

print("\nTop 5 longest descriptions:")
for i, (title, desc, length) in enumerate(desc_lengths[:5]):
    print(f"{i+1}. Length: {length} - Title: {title}")
    print(f"   Description: {desc[:100]}...")
    print()"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

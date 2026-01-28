code = """import json
import os

# Get the file path from the variable
file_path = var_functions.query_db:2
if isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        articles = json.load(f)
else:
    # Fallback if result is directly stored
    articles = var_functions.query_db:2

print(f"Total articles loaded: {len(articles)}")
print(f"First few articles:")
for i, article in enumerate(articles[:5]):
    print(f"  {i+1}. {article.get('title', 'N/A')}")"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

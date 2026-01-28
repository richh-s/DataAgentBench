code = """import json
import re

# Read the file path from the variable
file_path = var_functions.query_db_5

# Read the MongoDB results from the file
with open(file_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")
print("Sample paper structure:")
print(list(papers[0].keys()))
print("\nSample filename:", papers[0]['filename'])
print("Sample text preview (first 200 chars):", papers[0]['text'][:200])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

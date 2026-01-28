code = """import json
import re

# Read the MongoDB results from the file
with open('/tmp/tmp8b5k6pbd.json', 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")
print("Sample paper structure:")
print(papers[0].keys())
print("\nSample filename:", papers[0]['filename'])
print("Sample text preview:", papers[0]['text'][:500])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import re

# Read the full MongoDB data from file
mongo_data_path = var_functions.query_db:5

with open(mongo_data_path, 'r') as f:
    papers_raw = json.load(f)

print(f"Total papers in MongoDB: {len(papers_raw)}")
print(f"First paper sample: {papers_raw[0]['filename']}")
print(f"Sample text preview: {papers_raw[0]['text'][:500]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

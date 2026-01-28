code = """import json
import pandas as pd

# Load the full results from the previous queries
# MongoDB paper_docs
mongo_file = var_functions.query_db:3
if isinstance(mongo_file, str) and mongo_file.endswith('.json'):
    with open(mongo_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db:3

# SQLite citations
citations_file = var_functions.query_db:2
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations = json.load(f)
else:
    citations = var_functions.query_db:2

print(f"Loaded {len(paper_docs)} paper documents and {len(citations)} citation records")

# Preview the data structure
print("\nFirst paper doc:")
print(json.dumps(paper_docs[0], indent=2)[:500])

print("\nFirst citation:")
print(json.dumps(citations[0], indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

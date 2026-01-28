code = """import json
import pandas as pd
import os

# Check the type and value of the variables to understand the data structure
mongo_result = var_functions.query_db:3
citations_result = var_functions.query_db:2

print("Mongo result type:", type(mongo_result))
print("Citations result type:", type(citations_result))

# If they are strings ending with .json, they're file paths
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = mongo_result

if isinstance(citations_result, str) and citations_result.endswith('.json'):
    with open(citations_result, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_result

print(f"Loaded {len(paper_docs)} paper documents and {len(citations)} citation records")

# Show sample data
print("Sample paper doc title:", paper_docs[0].get('filename'))
print("Sample citation:", citations[0])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

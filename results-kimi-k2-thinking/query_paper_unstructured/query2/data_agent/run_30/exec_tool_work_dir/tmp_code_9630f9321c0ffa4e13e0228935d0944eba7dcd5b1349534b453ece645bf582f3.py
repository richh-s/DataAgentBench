code = """import json
import re

# Load citation data from 2018
citations_file = var_functions.query_db:0
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = var_functions.query_db:0

# Load paper documents
papers_file = var_functions.query_db:2
if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = var_functions.query_db:2

print(f"Number of citation records in 2018: {len(citations_data)}")
print(f"Number of paper documents: {len(papers_data)}")

# Preview first few records to understand the structure
print("\nFirst citation record:")
print(citations_data[0] if citations_data else "No data")

print("\nFirst paper document:")
print(papers_data[0] if papers_data else "No data")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

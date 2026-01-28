code = """import json
import re

# Load citations data from file
citations_file = var_functions.query_db:0
try:
    # If it's a string path, read the file
    if isinstance(citations_file, str):
        with open(citations_file, 'r') as f:
            citations_data = json.load(f)
    else:
        citations_data = citations_file
except Exception as e:
    print(f"Error loading citations: {e}")
    citations_data = []

# Load paper docs data from file
paper_docs_file = var_functions.query_db:4
try:
    # If it's a string path, read the file
    if isinstance(paper_docs_file, str):
        with open(paper_docs_file, 'r') as f:
            paper_docs_data = json.load(f)
    else:
        paper_docs_data = paper_docs_file
except Exception as e:
    print(f"Error loading paper docs: {e}")
    paper_docs_data = []

print(f"Citations count: {len(citations_data)}")
print(f"Paper docs count: {len(paper_docs_data)}")

# Show first few records to understand structure
if citations_data:
    print(f"First citation: {citations_data[0]}")
if paper_docs_data:
    print(f"First paper doc: {paper_docs_data[0]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

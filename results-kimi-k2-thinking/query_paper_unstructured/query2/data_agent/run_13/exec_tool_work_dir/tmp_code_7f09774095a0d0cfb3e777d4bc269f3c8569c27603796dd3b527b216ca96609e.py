code = """import json
import re

# Read citation data
citation_file_path = locals()['var_functions.query_db:0']
citation_data = []
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

# Read paper documents
doc_file_path = locals()['var_functions.query_db:2']
paper_docs = []
with open(doc_file_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total citations in 2018: {len(citation_data)}")
print(f"Total paper documents: {len(paper_docs)}")

# Let's inspect the first few items to understand the structure
print("\\nFirst 3 citations:")
for i, cite in enumerate(citation_data[:3]):
    print(f"  {i+1}. Title: {cite.get('title', 'N/A')}, Count: {cite.get('citation_count', 'N/A')}")

print("\\nFirst 3 paper documents:")
for i, doc in enumerate(paper_docs[:3]):
    print(f"  {i+1}. Filename: {doc.get('filename', 'N/A')}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

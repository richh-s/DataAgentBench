code = """import json

# Load citations data from 2020
citations_file = var_functions.query_db:6
citations_file_path = citations_file if isinstance(citations_file, str) else None

if citations_file_path and citations_file_path.endswith('.json'):
    with open(citations_file_path, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

print(f"Number of citation records: {len(citations_data)}")

# Show first few records to verify structure
print("First few citation records:")
for i, record in enumerate(citations_data[:3]):
    print(f"  {i+1}. {record}")

# Load paper docs data
paper_docs_file = var_functions.query_db:2
paper_docs_file_path = paper_docs_file if isinstance(paper_docs_file, str) else None

if paper_docs_file_path and paper_docs_file_path.endswith('.json'):
    with open(paper_docs_file_path, 'r') as f:
        paper_docs_data = json.load(f)
else:
    paper_docs_data = paper_docs_file

print(f"\nNumber of paper docs: {len(paper_docs_data)}")

# Show first few paper docs records
print("First few paper docs records:")
for i, record in enumerate(paper_docs_data[:2]):
    print(f"  {i+1}. Filename: {record.get('filename', 'N/A')}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

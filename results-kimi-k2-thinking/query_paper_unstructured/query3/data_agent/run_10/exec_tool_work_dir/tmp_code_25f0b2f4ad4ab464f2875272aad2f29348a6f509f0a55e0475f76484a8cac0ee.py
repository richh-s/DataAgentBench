code = """# Let's check the structure of the data first
import json
import os

# Get the file path from storage
paper_data_info = locals()['var_functions.query_db:2']

# Check if it's a string (file path) or already loaded data
if isinstance(paper_data_info, str):
    print(f"Loading data from file: {paper_data_info}")
    if os.path.exists(paper_data_info):
        with open(paper_data_info, 'r') as f:
            paper_docs = json.load(f)
        print(f"Successfully loaded {len(paper_docs)} documents")
    else:
        print(f"File not found: {paper_data_info}")
        paper_docs = []
else:
    paper_docs = paper_data_info
    print(f"Data already loaded, {len(paper_docs)} documents")

# Show first document structure
if paper_docs:
    first_doc = paper_docs[0]
    print(f"First document keys: {list(first_doc.keys())}")
    print(f"First document filename: {first_doc.get('filename')}")

print('__RESULT__:')
print(json.dumps({
    'document_count': len(paper_docs),
    'first_doc_keys': list(paper_docs[0].keys()) if paper_docs else [],
    'sample_filename': paper_docs[0].get('filename') if paper_docs else None
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'total_papers': 5, 'empirical_papers_after_2016_count': 0, 'sample_empirical_papers': []}, 'var_functions.list_db:8': ['Citations', 'sqlite_sequence']}

exec(code, env_args)

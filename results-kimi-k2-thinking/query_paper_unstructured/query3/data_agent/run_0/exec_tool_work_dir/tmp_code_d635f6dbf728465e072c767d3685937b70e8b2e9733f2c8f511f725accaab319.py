code = """import json
import re

# Get the file paths
paper_docs_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

# Load the data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Debug: Print first file to see structure
first_doc = paper_docs[0] if paper_docs else None
print('__RESULT__:')
print(json.dumps({
    'first_filename': first_doc.get('filename', '') if first_doc else 'none',
    'total_papers': len(paper_docs),
    'total_citations': len(citations),
    'citation_sample': citations[0] if citations else 'none'
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'paper_docs_path': 'file_storage/functions.query_db:2.json', 'citations_path': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:14': []}

exec(code, env_args)

code = """import json

# Check what variables are available
available_vars = [k for k in locals().keys() if 'query_db' in str(k)]
print('Available variables:', available_vars)

# Try to access the paper docs data
paper_docs_data = None
citations_data = None

for key in available_vars:
    if ':0' in key and 'query_db' in key:
        paper_docs_data = locals()[key]
        print(f'Paper docs stored as: {key}')
    elif ':2' in key and 'query_db' in key:
        citations_data = locals()[key]
        print(f'Citations stored as: {key}')

if paper_docs_data and isinstance(paper_docs_data, str) and '.json' in paper_docs_data:
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
    print(f'Loaded {len(paper_docs)} paper documents')
else:
    paper_docs = []
    print('Paper docs data not found or not a file path')

if citations_data and isinstance(citations_data, str) and '.json' in citations_data:
    with open(citations_data, 'r') as f:
        citations = json.load(f)
    print(f'Loaded {len(citations)} citations')
else:
    citations = []
    print('Citations data not found or not a file path')

# Print a sample to verify structure
if paper_docs:
    print(f'Sample paper doc keys: {list(paper_docs[0].keys())}')
    print(f'Sample filename: {paper_docs[0].get("filename", "N/A")}')
    
if citations:
    print(f'Sample citation keys: {list(citations[0].keys())}')
    print(f'Sample citation: {citations[0]}')

print('__RESULT__:')
print(json.dumps({'paper_docs_count': len(paper_docs), 'citations_count': len(citations)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

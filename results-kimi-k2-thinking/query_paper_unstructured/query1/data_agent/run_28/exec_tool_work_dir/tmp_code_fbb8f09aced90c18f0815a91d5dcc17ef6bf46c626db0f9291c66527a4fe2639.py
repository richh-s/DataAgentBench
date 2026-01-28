code = """import json

# Access the variables from locals()
paper_docs_key = 'var_functions.query_db:3'
citations_key = 'var_functions.query_db:2'

# Get the actual values
paper_docs_val = locals().get(paper_docs_key) if paper_docs_key in locals() else None
citations_val = locals().get(citations_key) if citations_key in locals() else None

# Check if these are file paths or direct data
if isinstance(paper_docs_val, str) and paper_docs_val.endswith('.json'):
    with open(paper_docs_val, 'r') as f:
        paper_docs = json.load(f)
    print('Loaded paper_docs from file')
else:
    paper_docs = paper_docs_val
    print('Used paper_docs directly')

if isinstance(citations_val, str) and citations_val.endswith('.json'):
    with open(citations_val, 'r') as f:
        citations = json.load(f)
    print('Loaded citations from file')
else:
    citations = citations_val
    print('Used citations directly')

print(f'paper_docs type: {type(paper_docs)}')
print(f'citations type: {type(citations)}')

if paper_docs and len(paper_docs) > 0:
    print(f'Number of papers: {len(paper_docs)}')
    print(f'First paper keys: {list(paper_docs[0].keys())}')
    print(f'First paper filename: {paper_docs[0].get("filename", "N/A")}')

if citations and len(citations) > 0:
    print(f'Number of citations: {len(citations)}')
    print(f'First citation: {citations[0]}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

code = """import json

# Access variables directly from storage
paper_docs = var_functions.query_db:2
citations = var_functions.query_db:5

# Check types
print('__RESULT__:')
print(json.dumps({
    'paper_docs_type': str(type(paper_docs))[:50],
    'citations_type': str(type(citations))[:50],
    'paper_docs_len': len(paper_docs) if isinstance(paper_docs, (list, dict)) else 'N/A',
    'citations_len': len(citations) if isinstance(citations, (list, dict)) else 'N/A'
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

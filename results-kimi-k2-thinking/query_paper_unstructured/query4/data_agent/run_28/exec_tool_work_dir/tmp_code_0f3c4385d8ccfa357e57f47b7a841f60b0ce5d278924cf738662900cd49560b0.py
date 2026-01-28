code = """import json

# Access the stored results - they appear to be swapped based on the output
# paper_docs_result actually contains citations
# citations_result actually contains paper_docs

paper_docs = locals()['var_functions.query_db:2']  # This is actually citations based on structure
citations = locals()['var_functions.query_db:3']   # This is actually paper docs based on structure

# If they are file paths, load them
if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'paper_docs_count': len(paper_docs),
    'citations_count': len(citations),
    'first_citation': citations[0] if citations else None,
    'sample_paper_doc': paper_docs[0] if paper_docs else None
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_docs_count': 1405, 'citations_count': 5, 'first_paper_keys': ['id', 'title', 'citation_count', 'citation_year'], 'first_citation_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)

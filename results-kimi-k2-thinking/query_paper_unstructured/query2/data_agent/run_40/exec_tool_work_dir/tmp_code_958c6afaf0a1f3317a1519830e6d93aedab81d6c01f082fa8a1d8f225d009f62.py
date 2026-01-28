code = """import json

# Get citations data for 2018
citation_data_key = 'var_functions.query_db:0'
citations_2018 = locals().get(citation_data_key)

if isinstance(citations_2018, str) and citations_2018.endswith('.json'):
    with open(citations_2018, 'r') as f:
        citations_2018 = json.load(f)

# Get paper documents
paper_data_key = 'var_functions.query_db:2'
paper_docs = locals().get(paper_data_key)

if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

# Debug info
print('__RESULT__:')
print(json.dumps({
    'citations_count': len(citations_2018) if isinstance(citations_2018, list) else str(type(citations_2018)),
    'papers_count': len(paper_docs) if isinstance(paper_docs, list) else str(type(paper_docs)),
    'citations_sample': citations_2018[:2] if isinstance(citations_2018, list) else None,
    'papers_sample': paper_docs[:1] if isinstance(paper_docs, list) else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

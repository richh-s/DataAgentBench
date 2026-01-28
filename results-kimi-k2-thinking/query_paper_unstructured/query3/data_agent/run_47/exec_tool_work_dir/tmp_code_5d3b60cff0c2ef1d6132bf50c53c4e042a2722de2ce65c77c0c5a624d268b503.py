code = """papers = locals()['var_functions.query_db:2']
citations = locals()['var_functions.query_db:3']

# Debug: check structure
print('Paper type:', type(papers))
print('Paper length:', len(papers))
if len(papers) > 0:
    print('First paper type:', type(papers[0]))
    print('First paper:', papers[0][:200] if isinstance(papers[0], str) else str(papers[0])[:200])

print('Citation type:', type(citations))
print('Citation length:', len(citations))
if len(citations) > 0:
    print('First citation type:', type(citations[0]))
    print('First citation keys:', citations[0].keys() if hasattr(citations[0], 'keys') else 'No keys')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}}

exec(code, env_args)

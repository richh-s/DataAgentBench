code = """import json

# Load paper documents and citations from storage
paper_docs = var_functions.query_db:3
citations = var_functions.query_db:2

print('paper_docs type:', type(paper_docs))
print('citations type:', type(citations))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

code = """import json

# Read the paper documents data (stored in a file path under the key)
paper_docs_path = var_functions.query_db:0
paper_docs = []
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read the citations data
citations_path = var_functions.query_db:2
citations = []
with open(citations_path, 'r') as f:
    citations = json.load(f)

len(paper_docs), len(citations)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

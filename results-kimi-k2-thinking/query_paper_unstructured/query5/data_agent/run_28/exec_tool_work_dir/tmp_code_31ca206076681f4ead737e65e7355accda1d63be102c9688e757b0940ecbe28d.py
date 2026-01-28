code = """import json

# Load citations data for 2020
citations_path = var_query_db:0
with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
papers_path = var_query_db:5
with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

print('Total 2020 citations:', len(citations_2020))
print('Total paper documents:', len(paper_docs))
print('\nFirst citation:', citations_2020[0])
print('\nFirst paper keys:', list(paper_docs[0].keys()))
print('First paper filename:', paper_docs[0].get('filename'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

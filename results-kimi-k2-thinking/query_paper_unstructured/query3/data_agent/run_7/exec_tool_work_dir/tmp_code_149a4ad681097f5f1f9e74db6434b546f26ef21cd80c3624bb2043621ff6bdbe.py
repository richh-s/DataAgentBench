code = """import json
import re

# Load the paper documents
paper_docs_file = locals()['var_functions.query_db:0']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load the citation data
citations_file = locals()['var_functions.query_db:1']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Check data structure
print('__RESULT__:')
print('Paper docs count:', len(paper_docs))
print('Citations count:', len(citations_data))
print('First paper:', paper_docs[0].get('filename') if paper_docs else 'No papers')
print('First citation:', citations_data[0] if citations_data else 'No citations')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)

code = """import json
import re

# Get the MongoDB paper documents file path
paper_docs_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

print('__RESULT__:')
print(json.dumps({
    'paper_docs_path': str(paper_docs_path),
    'citations_path': str(citations_path)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

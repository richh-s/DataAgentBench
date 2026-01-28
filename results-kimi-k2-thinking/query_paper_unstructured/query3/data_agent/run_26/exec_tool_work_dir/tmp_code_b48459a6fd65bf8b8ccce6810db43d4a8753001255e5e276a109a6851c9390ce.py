code = """import json
import re

# Access storage variables
paper_docs = locals()['var_functions.query_db:2']
citations = locals()['var_functions.query_db:5']

# Check what type they are
result_info = {
    'paper_docs_type': str(type(paper_docs)),
    'citations_type': str(type(citations)),
    'paper_docs_is_str': isinstance(paper_docs, str),
    'citations_is_str': isinstance(citations, str)
}

if isinstance(paper_docs, str):
    result_info['paper_docs_preview'] = paper_docs[:200]
if isinstance(citations, str):
    result_info['citations_preview'] = citations[:200]

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

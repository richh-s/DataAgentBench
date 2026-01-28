code = """import json

# Load citations data - it's stored in a file, so open it
citations_file = open('/tmp/tmpa7r3x_8s.json', 'r')
citations_2018 = json.load(citations_file)
citations_file.close()

# Load paper documents
papers_file = open('/tmp/tmpu_hk9n8q.json', 'r')
paper_docs = json.load(papers_file)
papers_file.close()

# Debug info
print('__RESULT__:')
print('Loaded %d citations and %d papers' % (len(citations_2018), len(paper_docs)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json'}

exec(code, env_args)

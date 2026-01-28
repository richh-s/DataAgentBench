code = """import json

# Load all citations from 2018
citations_file = var_functions.query_db:48
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load all paper documents
papers_file = var_functions.query_db:56
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Debug: print document structure
print('Paper docs count:', len(paper_docs))
print('Citations 2018 count:', len(citations_2018))
print('First paper doc keys:', list(paper_docs[0].keys()) if paper_docs else 'No docs')
print('Sample paper filename:', paper_docs[0]['filename'] if paper_docs else 'No docs')
print('Sample paper text snippet:', paper_docs[0]['text'][:200] if paper_docs and 'text' in paper_docs[0] else 'No text')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:52': {'total_2018': 158, 'acm_papers': 2, 'avg_citations': 68.5, 'sample_counts': [50, 87]}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)

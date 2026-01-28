code = """import json, pandas as pd, re

# Load data
papers_path = locals()['var_functions.query_db:32']
citations_path = locals()['var_functions.query_db:36']

with open(papers_path, 'r') as f:
    papers_raw = json.load(f)
with open(citations_path, 'r') as f:
    citations_raw = json.load(f)

# Find empirical papers after 2016
empirical_papers = []
for doc in papers_raw:
    title = doc['filename'].replace('.txt', '')
    year_match = re.search(r'\b(20[12]\d|202[0-5])\b', doc['text'])
    year = int(year_match.group(1)) if year_match else None
    
    if year and year > 2016 and 'empirical' in doc['text'].lower():
        empirical_papers.append({'title': title, 'year': year})

# Get citations
papers_df = pd.DataFrame(empirical_papers)
citations_df = pd.DataFrame(citations_raw)
citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'])

# Merge
merged = pd.merge(papers_df, citations_df, on='title', how='inner')
results = merged[['title', 'total_citations']].to_dict('records')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:48': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', '__builtins__', 'json'], 'var_functions.execute_python:50': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', 'var_functions.execute_python:48', '__builtins__', 'json'], 'var_functions.execute_python:54': {'var_functions.query_db:2': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.query_db:24': {'type': "<class 'list'>", 'is_str': False, 'is_list': True, 'length': 10}, 'var_functions.query_db:30': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:30.json'}, 'var_functions.query_db:32': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:32.json'}, 'var_functions.query_db:36': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:36.json'}}, 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:70': []}

exec(code, env_args)

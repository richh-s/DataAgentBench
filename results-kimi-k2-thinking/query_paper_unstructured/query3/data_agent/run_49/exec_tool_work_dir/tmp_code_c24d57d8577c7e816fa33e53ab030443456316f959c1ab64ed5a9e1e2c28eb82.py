code = """import json
import re

# Get the file path
file_path = locals()['var_functions.query_db:10']

# Read all papers
with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Sample a few papers to examine
sample = papers_data[:10]

results = []
for paper in sample:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Find all years
    years = re.findall(r'20\d{2}', text)
    
    # Find if empirical mentioned
    has_empirical = 'empirical' in text.lower()
    
    results.append({
        'title': filename.replace('.txt', ''),
        'years_found': years,
        'has_empirical': has_empirical,
        'text_snippet': text[:200]
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 1, 'papers': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': 2018, 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt"}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:16': {'count': 0, 'papers': []}, 'var_functions.execute_python:18': {'count': 0, 'papers': []}, 'var_functions.execute_python:20': {'count': 0, 'papers': []}}

exec(code, env_args)

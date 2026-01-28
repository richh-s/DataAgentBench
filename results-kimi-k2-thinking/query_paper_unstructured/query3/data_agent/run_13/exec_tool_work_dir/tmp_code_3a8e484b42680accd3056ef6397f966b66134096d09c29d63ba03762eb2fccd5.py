code = """import json
import re

# Load papers through a variable reference
papers_file_path = locals()['var_functions.query_db:8']
print('Loading from:', papers_file_path)

with open(papers_file_path) as f:
    papers = json.load(f)

empirical_titles = []

for p in papers:
    t = p['filename'].replace('.txt', '')
    txt = p['text']
    
    # Extract year
    y = None
    matches = re.findall(r"(?:'|\b)(\d{2})\b|(?:\b)(201\d|202\d)\b", txt)
    years = []
    for m in matches:
        if m[0]:
            year_val = int('20' + m[0])
            if 2010 <= year_val <= 2030: years.append(year_val)
        if m[1]:
            year_val = int(m[1])
            if 2010 <= year_val <= 2030: years.append(year_val)
    if years: y = max(years)
    
    # Check empirical and year filter
    if 'empirical' in txt.lower() and y and y > 2016:
        empirical_titles.append(t)

print('__RESULT__:')
print(json.dumps(empirical_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': []}

exec(code, env_args)

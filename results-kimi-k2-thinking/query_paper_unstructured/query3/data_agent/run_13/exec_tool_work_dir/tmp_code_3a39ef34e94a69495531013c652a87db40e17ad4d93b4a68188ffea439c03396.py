code = """import json
import re

# Read papers data from the stored file
with open('var_functions.query_db:8', 'r') as f:
    papers = json.load(f)

print('Loaded papers:', len(papers))

# Extract empirical papers after 2016
empirical_titles = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Check for year pattern
    year_match = re.search(r"\b(201[7-9]|202[0-1])\b", text)
    if year_match:
        year = int(year_match.group(1))
        # Check for empirical
        if 'empirical' in text.lower():
            empirical_titles.append(title)

print('Empirical papers after 2016:', len(empirical_titles))
print('__RESULT__:')
print(json.dumps(empirical_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': []}

exec(code, env_args)

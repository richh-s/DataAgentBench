code = """import json
import re

# Load papers
papers = json.load(open(var_functions.query_db:8))
print('Papers loaded:', len(papers))

# Extract titles and check for empirical and year
titles_to_check = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text'].lower()
    
    # Simple year extraction - look for 2017, 2018, 2019, 2020, 2021
    year_match = re.search(r"\b(201[7-9]|202[0-1])\b", paper['text'])
    year = int(year_match.group(1)) if year_match else None
    
    if year and 'empirical' in text:
        titles_to_check.append({'title': title, 'year': year})

print('Empirical papers after 2016:', len(titles_to_check))

# Output just the titles for the next query
titles_list = [item['title'] for item in titles_to_check]
print('__RESULT__:')
print(json.dumps(titles_list))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': []}

exec(code, env_args)

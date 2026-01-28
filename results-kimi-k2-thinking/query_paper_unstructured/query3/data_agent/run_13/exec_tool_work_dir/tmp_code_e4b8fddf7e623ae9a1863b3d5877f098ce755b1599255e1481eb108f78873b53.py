code = """import json
import re

# Load papers from file
papers = json.load(open(var_functions.query_db:8))

# Process papers
empirical_papers_after_2016 = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year from text
    year = None
    # Look for patterns like 2017, 2018, 2019, 2020, 2021
    year_match = re.search(r"\b(201[7-9]|202[0-1])\b", text)
    if year_match:
        year = int(year_match.group(1))
        
    # Check if empirical in text (case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    if year and has_empirical and year > 2016:
        empirical_papers_after_2016.append({'title': title, 'year': year})

print('Found', len(empirical_papers_after_2016), 'empirical papers after 2016')

# Return list of titles for next step
titles = [p['title'] for p in empirical_papers_after_2016]
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': []}

exec(code, env_args)

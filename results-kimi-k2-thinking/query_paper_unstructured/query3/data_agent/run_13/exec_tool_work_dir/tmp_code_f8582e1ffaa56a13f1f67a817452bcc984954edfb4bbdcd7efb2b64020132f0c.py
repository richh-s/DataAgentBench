code = """import json
import re

# Load papers from MongoDB query
papers = json.load(open(var_functions.query_db:8))

empirical_papers_2017plus = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year using regex patterns
    year = None
    # Look for year patterns in text
    year_matches = re.findall(r"(?:'|\b)(\d{2})\b|(?:\b)(201\d|202\d)\b", text)
    years_found = []
    
    for match in year_matches:
        if match[0]:  # '15 format
            y = int('20' + match[0])
            if 2010 <= y <= 2030:
                years_found.append(y)
        if match[1]:  # 2015 format
            y = int(match[1])
            if 2010 <= y <= 2030:
                years_found.append(y)
    
    if years_found:
        year = max(years_found)
    
    # Check for empirical contribution
    if 'empirical' in text.lower() and year and year > 2016:
        empirical_papers_2017plus.append(title)

print('__RESULT__:')
print(json.dumps(empirical_papers_2017plus))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': []}

exec(code, env_args)

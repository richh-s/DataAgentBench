code = """import json
import re

# Load papers from the file path stored in the variable
papers_data_path = locals()['var_functions.query_db:8']
print('Loading from:', papers_data_path)

with open(papers_data_path) as f:
    papers = json.load(f)

print('Number of papers:', len(papers))

# Process each paper to find empirical contributions after 2016
empirical_papers = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - look for patterns that indicate publication year
    year = None
    # Pattern: look for years 2017-2021
    matches = re.findall(r"\b(201[7-9]|202[012])\b", text)
    if matches:
        year = max([int(y) for y in matches])
    
    # Check if 'empirical' appears in text (case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    if year and has_empirical and year > 2016:
        empirical_papers.append({
            'title': title,
            'year': year
        })

# Return the list of papers
result_json = json.dumps(empirical_papers)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': []}

exec(code, env_args)

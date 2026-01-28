code = """import json
import re

# Get the file path
file_path = locals()['var_functions.query_db:10']

# Read all papers
with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Let's examine some papers to see what years exist
sample_papers = papers_data[:20]
all_years = []

empirical_papers = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Look for years - more flexible pattern
    year_matches = re.findall(r'(\b(20\d{2})\b)', text)
    
    year = None
    if year_matches:
        # Take the first 20xx year found
        for match in year_matches:
            yr = int(match[1])
            if yr > 2016:
                year = yr
                break
    
    # Check for empirical contribution more carefully
    has_empirical = 'empirical' in text.lower()
    
    if year and has_empirical:
        empirical_papers.append({
            'title': title,
            'year': year
        })

result = {
    'count': len(empirical_papers),
    'papers': empirical_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 1, 'papers': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': 2018, 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt"}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:16': {'count': 0, 'papers': []}, 'var_functions.execute_python:18': {'count': 0, 'papers': []}}

exec(code, env_args)

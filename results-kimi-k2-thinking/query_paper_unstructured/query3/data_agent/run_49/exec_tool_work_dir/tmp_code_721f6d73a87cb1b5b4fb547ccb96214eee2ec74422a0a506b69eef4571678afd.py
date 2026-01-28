code = """import json
import re

# Get the file path
file_path = locals()['var_functions.query_db:10']

# Read all papers
with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Extract paper metadata - all papers with years > 2016
papers_after_2016 = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Try to find year in text
    year = None
    year_matches = re.findall(r'\b(20(1[7-9]|[2-9][0-9]))\b', text)
    if year_matches:
        year = int(year_matches[0][0])
    
    # Filter: year > 2016
    if year and year > 2016:
        papers_after_2016.append({
            'title': title,
            'year': year
        })

result = {
    'count': len(papers_after_2016),
    'papers': papers_after_2016
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 1, 'papers': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': 2018, 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt"}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:16': {'count': 0, 'papers': []}}

exec(code, env_args)

code = """import json
import re

# Access papers data
paper_docs_key = 'var_functions.query_db:2'
paper_docs_path = locals()[paper_docs_key]

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print('Total papers loaded:', len(paper_docs))

# Debug: Check year distribution and content
year_counts = {}
physical_activity_papers = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Find years
    year_matches = re.findall(r'(19|20)\d{2}', text)
    
    # Count all years
    for y in year_matches:
        year = int(y)
        if 2000 <= year <= 2025:
            year_counts[year] = year_counts.get(year, 0) + 1
    
    # Check for 2016 publication
    has_2016 = '2016' in year_matches
    
    # Check for physical activity
    text_lower = text.lower()
    has_physical = 'physical activity' in text_lower or 'fitness' in text_lower
    
    if has_2016 and has_physical:
        physical_activity_papers.append(title)

print('\nYear distribution:')
for year in sorted(year_counts.keys()):
    print(f'  {year}: {year_counts[year]}')

print(f'\nPapers from 2016 with "physical activity" or "fitness": {len(physical_activity_papers)}')
for title in physical_activity_papers:
    print(f'  - {title}')

print('__RESULT__:')
print(json.dumps(physical_activity_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:18': []}

exec(code, env_args)

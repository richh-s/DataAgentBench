code = """import json
import re

mongo_path = locals()['var_functions.query_db:2']

with open(mongo_path, 'r') as f:
    docs = json.load(f)

print('Total documents loaded:', len(docs))

all_years = []
papers_by_year = {}

for doc in docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    year_match = re.search(r'\b(20\d{2})\b', text)
    if year_match:
        year = int(year_match.group(1))
        all_years.append(year)
        
        if year not in papers_by_year:
            papers_by_year[year] = []
        papers_by_year[year].append(title)

unique_years = sorted(set(all_years))
print('Unique years found:', unique_years)

for year in unique_years:
    print(year, ':', len(papers_by_year[year]), 'papers')
    for title in papers_by_year[year]:
        print('  ', title)

pa_papers = []
for doc in docs:
    text = doc.get('text', '').lower()
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if 'physical activity' in text:
        pa_papers.append(title)

print('\nAll physical activity papers:', len(pa_papers))
for title in pa_papers:
    print('  ', title)

result = {
    'years': unique_years,
    'pa_paper_count': len(pa_papers),
    'pa_titles': pa_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}, 'var_functions.execute_python:14': {'total_papers': 5, 'papers_2016_count': 0, 'papers_2016_physical_activity': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'papers_2016_pa_count': 0, 'papers_2016_pa_titles': []}}

exec(code, env_args)

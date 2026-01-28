code = """import json
import re

# Load MongoDB data
mongo_path = locals()['var_functions.query_db:2']
with open(mongo_path, 'r') as f:
    docs = json.load(f)

print('Total docs:', len(docs))

# Extract paper info
papers = []
for doc in docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Find year
    year = None
    m = re.search(r'\b(20\d{2})\b', text)
    if m:
        year = int(m.group(1))
    
    # Check for physical activity
    has_pa = 'physical activity' in text.lower()
    
    domain_str = 'physical activity' if has_pa else None
    
    papers.append({'title': title, 'year': year, 'domain': domain_str, 'has_pa': has_pa})

# Filter for 2016 physical activity papers
papers_2016_pa = []
for p in papers:
    if p['year'] == 2016 and p['has_pa']:
        papers_2016_pa.append(p)

print('2016 PA papers count:', len(papers_2016_pa))

# Get just the titles
titles_2016_pa = []
for p in papers_2016_pa:
    titles_2016_pa.append(p['title'])
    print('Found paper:', p['title'])

result = {
    'count': len(titles_2016_pa),
    'titles': titles_2016_pa
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}, 'var_functions.execute_python:14': {'total_papers': 5, 'papers_2016_count': 0, 'papers_2016_physical_activity': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'papers_2016_pa_count': 0, 'papers_2016_pa_titles': []}}

exec(code, env_args)

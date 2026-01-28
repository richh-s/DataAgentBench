code = """import json
import re

# Load MongoDB papers
path = var_functions.query_db:2
with open(path, 'r') as f:
    papers = json.load(f)

print('Total papers:', len(papers))

paper_info = []

for paper in papers:
    filename = paper.get('filename', '')
    if not filename:
        continue
    
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    
    # Extract year
    year = None
    first_part = text[:3000]
    year_match = re.search('20[0-9]{2}', first_part)
    if year_match:
        year = int(year_match.group())
    
    if not year:
        continue
    
    # Check for empirical
    empirical = 'empirical' in text[:5000].lower()
    
    if empirical:
        paper_info.append({'title': title, 'year': year})

# Filter after 2016
filtered = [p for p in paper_info if p['year'] > 2016]

result = {
    'total_empirical': len(paper_info),
    'after_2016': len(filtered),
    'sample_filtered': filtered[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)

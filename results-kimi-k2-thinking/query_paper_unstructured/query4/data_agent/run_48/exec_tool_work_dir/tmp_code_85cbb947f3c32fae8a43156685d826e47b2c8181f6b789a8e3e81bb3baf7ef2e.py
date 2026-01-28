code = """import json
import re

# Load data
papers_file = locals()['var_functions.query_db:26']
citations_file = locals()['var_functions.query_db:9']

with open(papers_file, 'r') as f:
    papers = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract metadata
paper_info = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Find year
    year = None
    if re.search(r'2016', text):
        year = 2016
    elif re.search(r'2015', text):
        year = 2015
    elif re.search(r'2014', text):
        year = 2014
    elif re.search(r'2013', text):
        year = 2013
    
    # Check copyright
    if not year:
        m = re.search(r'Copyright\D*(\d{4})\D*', text)
        if m:
            year = int(m.group(1))
    
    # Check domains
    text_lower = text.lower()
    has_physical_activity = 'physical activity' in text_lower
    
    paper_info.append({
        'title': title,
        'year': year,
        'physical_activity': has_physical_activity
    })

# Find 2016 physical activity papers
papers_2016_pa = [p for p in paper_info if p['year'] == 2016 and p['physical_activity']]
titles_set = set(p['title'] for p in papers_2016_pa)

# Count citations
total_citations = 0
for cit in citations:
    if cit.get('title') in titles_set:
        total_citations += int(cit.get('citation_count', 0))

result = {
    'papers_2016_physical_activity': len(papers_2016_pa),
    'titles': [p['title'] for p in papers_2016_pa],
    'total_citations': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'papers_count': 5, 'citations_count': 1405}, 'var_functions.execute_python:12': {'total_papers': 5, 'papers_2016_physical_activity': 0, 'sample_titles': []}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'papers_loaded': 5, 'citations_loaded': 1405}, 'var_functions.execute_python:22': {'papers_found': 0, 'titles': [], 'total_citations': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

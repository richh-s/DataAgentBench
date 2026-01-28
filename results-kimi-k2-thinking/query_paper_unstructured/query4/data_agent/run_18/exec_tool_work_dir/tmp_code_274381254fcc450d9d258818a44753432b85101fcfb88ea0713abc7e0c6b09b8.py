code = """import json
import re

# Load MongoDB data
mongo_path = locals()['var_functions.query_db:2']
with open(mongo_path, 'r') as f:
    all_docs = json.load(f)

print('Total MongoDB documents:', len(all_docs))

# Process all documents
papers_metadata = []
for doc in all_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Find year
    year = None
    patterns = [
        r'\b(20\d{2})\b',
        r"[A-Za-z]+\s+'(\d{2})\b",
        r'Proceedings\s+of\s+[A-Za-z]+\s+(\d{4})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 4:
                year = int(year_str)
            elif len(year_str) == 2:
                year = 2000 + int(year_str)
            break
    
    # Check domains
    text_lower = text.lower()
    has_pa = 'physical activity' in text_lower
    
    papers_metadata.append({
        'title': title,
        'year': year,
        'has_physical_activity': has_pa
    })

# Find 2016 physical activity papers
papers_2016_pa = []
for paper in papers_metadata:
    if paper['year'] == 2016 and paper['has_physical_activity']:
        papers_2016_pa.append(paper['title'])

print('Papers from 2016 in physical activity domain:', len(papers_2016_pa))
total_docs = len(all_docs)
print('Total documents examined:', total_docs)

result = {
    'papers_2016_physical_activity': papers_2016_pa,
    'count': len(papers_2016_pa),
    'total_docs': total_docs
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}, 'var_functions.execute_python:14': {'total_papers': 5, 'papers_2016_count': 0, 'papers_2016_physical_activity': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'papers_2016_pa_count': 0, 'papers_2016_pa_titles': []}, 'var_functions.execute_python:26': {'count': 0, 'titles': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'count': 0, 'papers': []}}

exec(code, env_args)

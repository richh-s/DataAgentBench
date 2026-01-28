code = """import json
import re

mongo_path = locals()['var_functions.query_db:2']
with open(mongo_path, 'r') as f:
    docs = json.load(f)

print('Total documents:', len(docs))

# Debug: Show first few documents
print('
First 3 documents:')
for i in range(min(3, len(docs))):
    doc = docs[i]
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text_start = doc.get('text', '')[:200]
    print(f"  {i+1}. {title}")
    print(f"     Text start: {text_start[:100]}...")
    
    # Extract year
    year_match = re.search(r'\b(20\d{2})\b', doc.get('text', ''))
    if year_match:
        print(f"     Year found: {year_match.group(1)}")
    else:
        print(f"     No year found")

# Find all unique years
print('
All unique years:')
years = set()
for doc in docs:
    text = doc.get('text', '')
    year_matches = re.findall(r'\b(20\d{2})\b', text)
    for y in year_matches:
        years.add(int(y))

print('Unique years found:', sorted(years))

# Find all papers with physical activity and their years
print('
Papers with physical activity:')
pa_papers = []
for doc in docs:
    text = doc.get('text', '').lower()
    if 'physical activity' in text:
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        
        # Find year
        year_match = re.search(r'\b(20\d{2})\b', doc.get('text', ''))
        year = int(year_match.group(1)) if year_match else None
        
        pa_papers.append({'title': title, 'year': year})
        print(f"  {title} (Year: {year})")

result = {
    'total_docs': len(docs),
    'unique_years': sorted(years),
    'pa_papers_count': len(pa_papers),
    'pa_papers': pa_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}, 'var_functions.execute_python:14': {'total_papers': 5, 'papers_2016_count': 0, 'papers_2016_physical_activity': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'papers_2016_pa_count': 0, 'papers_2016_pa_titles': []}, 'var_functions.execute_python:26': {'count': 0, 'titles': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'count': 0, 'papers': []}}

exec(code, env_args)

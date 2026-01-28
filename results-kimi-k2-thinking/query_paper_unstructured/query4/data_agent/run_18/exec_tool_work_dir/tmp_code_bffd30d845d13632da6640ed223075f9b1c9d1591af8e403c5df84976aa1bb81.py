code = """import json
import re

# Get the MongoDB file path from storage
mongo_file_path = locals()['var_functions.query_db:2']
print(f"Mongo file path: {mongo_file_path}")

# Read and process the paper documents
with open(mongo_file_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total papers loaded: {len(paper_docs)}")

# Extract information for each paper
papers_list = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Find publication year using regex
    year = None
    
    # Pattern for 4-digit years starting with 20
    year_match = re.search(r"\b(20\d{2})\b", text)
    if year_match:
        year = int(year_match.group(1))
    
    # Alternative pattern for 2-digit years after venue names
    if not year:
        two_digit_match = re.search(r"[A-Za-z]+\s+'(\d{2})\b", text)
        if two_digit_match:
            year_str = two_digit_match.group(1)
            year = 2000 + int(year_str)
    
    # Check domains
    text_lower = text.lower()
    domains = []
    if 'physical activity' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'food' in text_lower:
        domains.append('food')
    
    domain_str = ','.join(domains) if domains else None
    
    papers_list.append({
        'title': title,
        'year': year,
        'domain': domain_str,
        'has_physical_activity': 'physical activity' in text_lower
    })

# Filter for 2016 papers with physical activity
papers_2016_pa = []
for p in papers_list:
    if p['year'] == 2016 and p['has_physical_activity']:
        papers_2016_pa.append(p)

print(f"Papers from 2016 about physical activity: {len(papers_2016_pa)}")
for p in papers_2016_pa:
    print(f"  - {p['title']}")

# Return JSON-serializable result
result = {
    'total_papers': len(papers_list),
    'papers_2016_count': len([p for p in papers_list if p['year'] == 2016]),
    'papers_2016_physical_activity': [p['title'] for p in papers_2016_pa]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}}

exec(code, env_args)

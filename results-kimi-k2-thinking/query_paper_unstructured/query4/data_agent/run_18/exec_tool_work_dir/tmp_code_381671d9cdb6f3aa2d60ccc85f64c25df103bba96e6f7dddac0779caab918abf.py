code = """import json
import re

# Load the full MongoDB data
mongo_path = locals()['var_functions.query_db:2']
print(f"Loading from: {mongo_path}")

with open(mongo_path, 'r') as f:
    all_docs = json.load(f)

print(f"Total documents: {len(all_docs)}")

# Process each document to extract metadata
processed_papers = []
for doc in all_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Extract year with multiple patterns
    year = None
    
    # Pattern 1: Four digit year like 2015, 2016
    year_match = re.search(r'\b(20\d{2})\b', text)
    if year_match:
        year = int(year_match.group(1))
    
    # Pattern 2: Two digit year in venue format
    if not year:
        venue_match = re.search(r"[A-Za-z]+\s+'(\d{2})\b", text)
        if venue_match:
            year = 2000 + int(venue_match.group(1))
    
    # Extract domains
    text_lower = text.lower()
    domains = []
    if 'physical activity' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'food' in text_lower:
        domains.append('food')
    if 'mental' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower:
        domains.append('finances')
    if 'fitness' in text_lower:
        domains.append('fitness')
    
    processed_papers.append({
        'title': title,
        'year': year,
        'domains': domains,
        'has_physical_activity': 'physical activity' in text_lower
    })

# Filter for 2016 physical activity papers
papers_2016_pa = [p for p in processed_papers if p['year'] == 2016 and p['has_physical_activity']]

print(f"\nPapers from 2016 in physical activity domain: {len(papers_2016_pa)}")
for p in papers_2016_pa:
    print(f"  - {p['title']} ({p['year']})")

# Show all papers by year
print("\nAll papers by year:")
year_dist = {}
for p in processed_papers:
    y = p['year']
    year_dist[y] = year_dist.get(y, 0) + 1
    print(f"  {y}: {p['title']}")

print(f"\nYear distribution: {year_dist}")

result = {
    'processed_count': len(processed_papers),
    'papers_2016_pa': papers_2016_pa,
    'year_distribution': year_dist
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}, 'var_functions.execute_python:14': {'total_papers': 5, 'papers_2016_count': 0, 'papers_2016_physical_activity': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)

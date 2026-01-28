code = """import json
import re

# Load the MongoDB data
mongo_path = locals()['var_functions.query_db:2']
print(f"Loading data from: {mongo_path}")

with open(mongo_path, 'r') as f:
    docs = json.load(f)

print(f"Total documents: {len(docs)}")

# Extract all papers with their years
all_papers = []
for doc in docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Extract year - try multiple patterns
    year = None
    
    # Pattern 1: Look for 20XX year
    match1 = re.search(r'\b(20\d{2})\b', text)
    if match1:
        year = int(match1.group(1))
    
    # Pattern 2: Look for 2-digit year after venue
    if not year:
        match2 = re.search(r"[A-Za-z]+\s+'(\d{2})\b", text)
        if match2:
            year = 2000 + int(match2.group(1))
    
    # Pattern 3: Look for other common formats
    if not year:
        match3 = re.search(r'Proceedings.*?\b(20\d{2})\b', text, re.IGNORECASE)
        if match3:
            year = int(match3.group(1))
    
    all_papers.append({'title': title, 'year': year})

# Show all papers by year
print("\nAll papers by year:")
year_counts = {}
for p in all_papers:
    year = p['year']
    if year not in year_counts:
        year_counts[year] = 0
    year_counts[year] += 1
    print(f"  {year}: {p['title']}")

print(f"\nYear distribution: {year_counts}")

# Check for physical activity mentions
pa_papers = []
for doc in docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '').lower()
    
    if 'physical activity' in text:
        # Find year
        year = None
        year_match = re.search(r'\b(20\d{2})\b', doc.get('text', ''))
        if year_match:
            year = int(year_match.group(1))
        
        pa_papers.append({'title': title, 'year': year})

print(f"\nPapers mentioning 'physical activity': {len(pa_papers)}")
for p in pa_papers:
    print(f"  {p['year']} - {p['title']}")

result = {
    'total_documents': len(docs),
    'papers_by_year': year_counts,
    'physical_activity_papers': pa_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}, 'var_functions.execute_python:14': {'total_papers': 5, 'papers_2016_count': 0, 'papers_2016_physical_activity': []}}

exec(code, env_args)

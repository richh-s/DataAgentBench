code = """import json
import re

# Access papers data
paper_docs_key = 'var_functions.query_db:2'
paper_docs_path = locals()[paper_docs_key]

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print('Total papers loaded:', len(paper_docs))

# Check a few papers to understand structure and year patterns
for i in range(min(5, len(paper_docs))):
    doc = paper_docs[i]
    text = doc.get('text', '')
    year_matches = re.findall(r'(19|20)\d{2}', text[:2000])
    print(f'Paper {i}: {doc.get("filename")} - Years found: {year_matches}')

# Try broader search for 2016 papers with physical activity
papers_2016_physical_activity = []
found_years = {}

check_terms = ['physical', 'activity', 'fitness', 'exercise', 'steps', 'walking', 'running']

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Find all years in the document
    year_matches = re.findall(r'(19|20)\d{2}', text)
    
    # Filter for valid years and prefer 2016 if exists
    year = None
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2025]
        if 2016 in valid_years:
            year = 2016
        elif valid_years:
            year = max(valid_years)  # Use max year if not 2016
    
    # Check if contains physical activity terms
    text_lower = text.lower()
    has_physical_activity = any(term in text_lower for term in check_terms)
    
    if year == 2016 and has_physical_activity:
        papers_2016_physical_activity.append(title)
    
    if year:
        found_years[year] = found_years.get(year, 0) + 1

print('\nPaper counts by year:')
for y in sorted(found_years.keys()):
    print(f'  {y}: {found_years[y]}')

print(f'\n2016 papers with physical activity terms: {len(papers_2016_physical_activity)}')
if papers_2016_physical_activity:
    for title in papers_2016_physical_activity:
        print(f'  - {title}')
else:
    # Debug: check if any papers have physical activity terms at all
    any_physical = []
    for doc in paper_docs:
        text = doc.get('text', '').lower()
        if any(term in text for term in check_terms):
            any_physical.append(doc.get('filename', '').replace('.txt', ''))
    print(f'Any papers with physical activity terms: {len(any_physical)}')
    print(any_physical[:10])

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:18': []}

exec(code, env_args)

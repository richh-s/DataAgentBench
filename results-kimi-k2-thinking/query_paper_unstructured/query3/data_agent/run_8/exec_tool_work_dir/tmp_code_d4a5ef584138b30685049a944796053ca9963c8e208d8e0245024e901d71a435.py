code = """import json
import re

# Get the file paths for both datasets
papers_file_path = var_functions.query_db:26
citations_file_path = var_functions.query_db:24

# Read papers data
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Extract metadata for each paper
paper_metadata = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text - look for 4-digit years 2000-2029
    year_match = re.search(r'\b(20[0-2][0-9])\b', text)
    year = int(year_match.group()) if year_match else None
    
    # Extract contribution type - check if 'empirical' is mentioned
    text_lower = text.lower()
    has_empirical = 'empirical' in text_lower
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Filter papers after 2016 (i.e., 2017+) with empirical contribution
empirical_papers_2017_plus = [
    paper for paper in paper_metadata 
    if paper['year'] and paper['year'] > 2016 and paper['has_empirical']
]

# Read citations data
with open(citations_file_path, 'r') as f:
    citations = json.load(f)

# Create a lookup dictionary for citation counts
citation_lookup = {item['title']: int(item['total_citations']) for item in citations}

# For empirical papers after 2016, get their citation counts
result = []
for paper in empirical_papers_2017_plus:
    title = paper['title']
    if title in citation_lookup:
        result.append({
            'title': title,
            'total_citations': citation_lookup[title],
            'year': paper['year']
        })

# Sort by citation count descending
result_sorted = sorted(result, key=lambda x: x['total_citations'], reverse=True)

print(f"__RESULT__:")
print(json.dumps(
    result_sorted,
    indent=2
))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'available_variables': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:10', 'var_functions.query_db:14', '__builtins__', 'json'], 'var_functions.query_db:14_type': "<class 'str'>", 'var_functions.query_db:14_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

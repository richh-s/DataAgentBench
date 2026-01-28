code = """import json
import re

# Get the file paths from storage
papers_file_path = globals()['var_functions.query_db:26']
citations_file_path = globals()['var_functions.query_db:24']

# Read papers data
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Read citations data
with open(citations_file_path, 'r') as f:
    citations = json.load(f)

# Create a lookup dictionary for citation counts
citation_lookup = {item['title']: int(item['total_citations']) for item in citations}

# Debug: Check some paper titles and their presence in citations
sample_titles = []
for i, paper in enumerate(papers[:20]):
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    in_citations = title in citation_lookup
    sample_titles.append({
        'index': i,
        'title': title,
        'in_citations': in_citations,
        'citations': citation_lookup.get(title, 0) if in_citations else 0
    })

# Debug: Check years found
years_found = []
empirical_found = 0
for paper in papers[:100]:  # Check first 100
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for year patterns
    year_match = re.search(r'\b(20[0-2][0-9])\b', text)
    year = int(year_match.group()) if year_match else None
    
    if year:
        years_found.append(year)
    
    if 'empirical' in text.lower():
        empirical_found += 1

# Statistics
year_counts = {}
for year in years_found:
    year_counts[year] = year_counts.get(year, 0) + 1

print("__RESULT__:")
print(json.dumps({
    "total_papers": len(papers),
    "sample_title_matches": sample_titles,
    "year_distribution": year_counts,
    "empirical_mentions_in_first_100": empirical_found,
    "papers_in_citations": len([p for p in papers[:100] if p.get('filename', '').replace('.txt', '') in citation_lookup])
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'available_variables': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:10', 'var_functions.query_db:14', '__builtins__', 'json'], 'var_functions.query_db:14_type': "<class 'str'>", 'var_functions.query_db:14_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': [], 'var_functions.execute_python:34': {'total_processed': 5, 'year_range': 'N/A to N/A', 'papers_with_empirical': 2, 'papers_after_2016': 0, 'empirical_after_2016': 0, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}]}, 'var_functions.execute_python:36': [], 'var_functions.execute_python:38': []}

exec(code, env_args)

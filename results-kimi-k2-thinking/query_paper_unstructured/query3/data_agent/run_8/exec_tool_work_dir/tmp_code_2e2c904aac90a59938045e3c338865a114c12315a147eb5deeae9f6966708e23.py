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

# Extract and filter papers
empirical_papers_after_2016 = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Skip if title not in citation lookup
    if title not in citation_lookup:
        continue
    
    # Extract year - be more aggressive in finding years
    year = None
    text_to_search = text[:2000]  # Look in first 2000 chars
    
    # Pattern 1: Four digit years 2000-2030
    year_match = re.search(r'\b(20(1[7-9]|2[0-3]))\b', text_to_search)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Pattern 2: Look for copyright notices
        copyright_match = re.search(r'Copyright[^\d]{0,50}(20(1[7-9]|2[0-3]))', text_to_search, re.IGNORECASE)
        if copyright_match:
            year = int(copyright_match.group(1))
        else:
            # Pattern 3: Look for venue notation like '17, '18, '19, '20, '21, '22, '23
            venue_match = re.search(r"'([7-9]|2[0-3])\b", text_to_search)
            if venue_match:
                year_suffix = venue_match.group(1)
                if year_suffix.startswith('2'):
                    year = 2000 + int(year_suffix)
                else:
                    year = 2010 + int(year_suffix)
    
    # Check if year is after 2016 and paper is empirical
    if year and year > 2016:
        text_lower = text.lower()
        if 'empirical' in text_lower:
            empirical_papers_after_2016.append({
                'title': title,
                'year': year,
                'total_citations': citation_lookup[title]
            })

# Sort by citation count descending
result_sorted = sorted(empirical_papers_after_2016, key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(result_sorted, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'available_variables': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:10', 'var_functions.query_db:14', '__builtins__', 'json'], 'var_functions.query_db:14_type': "<class 'str'>", 'var_functions.query_db:14_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': [], 'var_functions.execute_python:34': {'total_processed': 5, 'year_range': 'N/A to N/A', 'papers_with_empirical': 2, 'papers_after_2016': 0, 'empirical_after_2016': 0, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}]}, 'var_functions.execute_python:36': []}

exec(code, env_args)

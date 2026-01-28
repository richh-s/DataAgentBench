code = """import json
import re

# Load data
citations_debug = locals()['var_functions.query_db:16']
if isinstance(citations_debug, str) and 'json' in citations_debug:
    with open(citations_debug, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_debug

papers_file_path = locals()['var_functions.query_db:17']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Find all papers that mention 'food' in their text
food_papers = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if 'food' appears in the text (case-insensitive)
    if re.search(r'food\b', text, re.IGNORECASE):
        food_papers.append(title.lower())

# Sum citations for food papers
total_citations = 0
papers_found = 0
matched_details = []

for citation in citations_data:
    citation_title = citation.get('title', '').lower()
    citation_count = int(str(citation.get('citation_count', 0)))
    
    if citation_title in food_papers:
        total_citations += citation_count
        papers_found += 1
        matched_details.append({
            'title': citation.get('title', ''),
            'citations': citation_count
        })

result = {
    'total_citation_count': total_citations,
    'papers_in_food_domain': papers_found,
    'matched_papers': matched_details
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:24': {'total_citation_count': 0, 'papers_in_food_domain': 0, 'matched_paper_titles': []}}

exec(code, env_args)

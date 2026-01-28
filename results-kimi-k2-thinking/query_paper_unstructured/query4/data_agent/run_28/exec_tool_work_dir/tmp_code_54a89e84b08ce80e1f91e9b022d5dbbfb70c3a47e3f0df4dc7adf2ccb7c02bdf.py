code = """import json
import re

# Load citations
cit_file = var_functions.query_db:24
with open(cit_file, 'r') as f:
    citations = json.load(f)

# Load paper documents
paper_file = var_functions.query_db:31
with open(paper_file, 'r') as f:
    papers = json.load(f)

print(f"Citations: {len(citations)}")
print(f"Papers: {len(papers)}")

# Build citation map
cit_map = {}
for c in citations:
    cit_map[c['title']] = int(c['total_citations'])

# Find 2016 physical activity papers
results = []
keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable', 'steps', 'walking', 'running']

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check year 2016
    if not re.search(r'2016', text):
        continue
    
    # Check physical activity domain
    text_lower = text.lower()
    if not any(k in text_lower for k in keywords):
        continue
    
    title = filename.replace('.txt', '')
    total_cit = cit_map.get(title, 0)
    
    results.append({
        'title': title,
        'total_citations': total_cit
    })

print(f"Found {len(results)} matching papers")
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_docs_count': 1405, 'citations_count': 5, 'first_paper_keys': ['id', 'title', 'citation_count', 'citation_year'], 'first_citation_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': [], 'var_functions.execute_python:18': [{'index': 0, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 1, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 2, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 3, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 4, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 5, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 6, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 7, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 8, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 9, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}], 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'paper_docs_type': "<class 'str'>", 'citations_is_str': True, 'paper_docs_is_str': True, 'citations_file_exists': True, 'paper_docs_file_exists': True}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)

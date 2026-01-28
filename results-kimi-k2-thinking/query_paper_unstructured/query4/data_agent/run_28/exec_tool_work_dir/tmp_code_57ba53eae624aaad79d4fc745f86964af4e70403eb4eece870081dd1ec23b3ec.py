code = """import json
import re

# Load the data files
citations_path = locals()['var_functions.query_db:24']
papers_path = locals()['var_functions.query_db:31']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Create citation dictionary
cit_dict = {}
for item in citations:
    cit_dict[item['title']] = int(item['total_citations'])

# Find 2016 physical activity papers
matching_papers = []
pa_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable', 'steps', 'walking', 'running']

for doc in papers:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check for 2016
    has_2016 = re.search(r'2016', text) is not None
    if not has_2016:
        continue
    
    # Check for physical activity
    lower_text = text.lower()
    is_pa = any(keyword in lower_text for keyword in pa_keywords)
    if not is_pa:
        continue
    
    title = filename.replace('.txt', '')
    total_cit = cit_dict.get(title, 0)
    
    matching_papers.append({
        'title': title,
        'total_citations': total_cit
    })

# Sort by citations
matching_papers.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(matching_papers, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_docs_count': 1405, 'citations_count': 5, 'first_paper_keys': ['id', 'title', 'citation_count', 'citation_year'], 'first_citation_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': [], 'var_functions.execute_python:18': [{'index': 0, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 1, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 2, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 3, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 4, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 5, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 6, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 7, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 8, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 9, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}], 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'paper_docs_type': "<class 'str'>", 'citations_is_str': True, 'paper_docs_is_str': True, 'citations_file_exists': True, 'paper_docs_file_exists': True}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)

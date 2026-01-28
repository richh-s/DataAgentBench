code = """import json
import re

# Load citations data
citations_file = var_functions.query_db:24
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load paper documents data
paper_docs_file = var_functions.query_db:31
with open(paper_docs_file, 'r') as f:
    paper_docs_data = json.load(f)

print(f"Loaded {len(citations_data)} citation records")
print(f"Loaded {len(paper_docs_data)} paper documents")

# Create citation dictionary: title -> total citations
citation_dict = {}
for cit in citations_data:
    title = cit['title']
    total_citations = int(cit['total_citations'])
    citation_dict[title] = total_citations

print(f"Created citation dictionary with {len(citation_dict)} unique titles")

# Analyze paper documents
physical_activity_papers_2016 = []
keywords_2016 = [r'\b2016\b', r"'16\b"]
physical_activity_keywords = [
    'physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable',
    'steps', 'walking', 'running', 'fitness tracker', 'activity monitor'
]

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Check for year 2016
    year_2016 = False
    for pattern in keywords_2016:
        if re.search(pattern, text):
            year_2016 = True
            break
    
    if not year_2016:
        continue
    
    # Check for physical activity domain
    text_lower = text.lower()
    is_physical_activity = any(keyword in text_lower for keyword in physical_activity_keywords)
    
    if is_physical_activity:
        # Get citation count
        citation_count = citation_dict.get(title, 0)
        physical_activity_papers_2016.append({
            'title': title,
            'total_citations': citation_count
        })

print(f"Found {len(physical_activity_papers_2016)} papers from 2016 in physical activity domain")

# Sort by citation count
the_sorted = sorted(physical_activity_papers_2016, key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(the_sorted, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_docs_count': 1405, 'citations_count': 5, 'first_paper_keys': ['id', 'title', 'citation_count', 'citation_year'], 'first_citation_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': [], 'var_functions.execute_python:18': [{'index': 0, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 1, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 2, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 3, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 4, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 5, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 6, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 7, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 8, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 9, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}], 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'paper_docs_type': "<class 'str'>", 'citations_is_str': True, 'paper_docs_is_str': True, 'citations_file_exists': True, 'paper_docs_file_exists': True}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)

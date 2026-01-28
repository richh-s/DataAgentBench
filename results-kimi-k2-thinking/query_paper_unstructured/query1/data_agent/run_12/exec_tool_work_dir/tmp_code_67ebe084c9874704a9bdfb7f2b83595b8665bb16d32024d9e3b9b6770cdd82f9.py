code = """import json
import re

# Load the paper_docs data
paper_docs_data = locals()['var_functions.query_db:5']
if isinstance(paper_docs_data, str):  # It's a file path
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

# Load the citations data
citations_data = locals()['var_functions.query_db:8']
if isinstance(citations_data, str):  # It's a file path
    with open(citations_data, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_data

# Process paper documents to extract title and domain
papers_info = []

domain_keywords = [
    'food', 'nutrition', 'diet', 'eating', 'meal', 'calorie',
    'physical activity', 'exercise', 'fitness', 'sleep', 'mental',
    'finances', 'productivity', 'screen time', 'social interactions',
    'location', 'chronic', 'diabetes', 'health_behavior'
]

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract domains from text
    domains = []
    text_lower = text.lower()
    
    for keyword in domain_keywords:
        if keyword in text_lower:
            domains.append(keyword)
    
    papers_info.append({
        'title': title,
        'domains': domains,
        'text': text[:1000]  # Store first 1000 chars for debugging
    })

# Convert citations to a more usable format
citations_list = []
for cit in citations:
    citations_list.append({
        'title': cit.get('title', ''),
        'citation_count': int(cit.get('citation_count', 0)),
        'citation_year': int(cit.get('citation_year', 0))
    })

print('__RESULT__:')
print(json.dumps({
    'papers_processed': len(papers_info),
    'citations_processed': len(citations_list),
    'sample_papers': papers_info[:3],
    'sample_citations': citations_list[:3]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json'}

exec(code, env_args)

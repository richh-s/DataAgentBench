code = """import json
import re

# Load citation data
citation_file = locals()['var_functions.query_db:2']
papers_file = locals()['var_functions.query_db:5']

with open(citation_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Build citation dictionary
citation_dict = {cite['title']: int(cite['citation_count']) for cite in citations_2018}

# Find ACM papers with 2018 citations
acm_papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    if title not in citation_dict:
        continue
        
    text = doc.get('text', '').lower()
    
    # Check for ACM patterns
    is_acm = False
    if 'acm' in text:
        is_acm = True
    elif 'permission to make digital or hard copies' in text:
        is_acm = True
    elif 'association for computing machinery' in text:
        is_acm = True
    elif 'proceedings of the acm' in text:
        is_acm = True
    
    if is_acm:
        acm_papers.append({
            'title': title,
            'citations': citation_dict[title]
        })

# Calculate average
if acm_papers:
    total_cites = sum(p['citations'] for p in acm_papers)
    avg_cites = total_cites / len(acm_papers)
    result = {
        'avg': round(avg_cites, 2),
        'count': len(acm_papers),
        'total': total_cites
    }
else:
    result = {'avg': 0, 'count': 0, 'total': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'average_citation_count': 68.5, 'total_acm_papers': 2, 'total_citations': 137}}

exec(code, env_args)

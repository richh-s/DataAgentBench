code = """import json
import re

# Load the full data
citations_data = locals()['var_functions.query_db:0']
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

paper_docs_data = locals()['var_functions.query_db:2']
if isinstance(paper_docs_data, str) and paper_docs_data.endswith('.json'):
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

print(f"Total 2018 citations: {len(citations_data)}")
print(f"Total MongoDB documents: {len(paper_docs_data)}")

# Create citations dictionary
citations_dict = {item['title']: int(item['citation_count']) for item in citations_data}

# Look for ACM patterns more broadly
acm_patterns = [
    r'\bACM\b',
    r'ACM Classification Keywords',
    r'Copyright.*ACM',
    r'ACM\s+\d{4}-\d+-\d+',  # ACM DOI format part
    r'10\.1145/\d+\.\d+',  # ACM DOI pattern
    r'ACM TRANSACTIONS', 
    r'ACM SIG',
    r'Association for Computing Machinery'
]

acm_papers_with_citations = []

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Check if any ACM pattern exists
    has_acm = any(re.search(pattern, text, re.IGNORECASE) for pattern in acm_patterns)
    
    if has_acm and title in citations_dict:
        acm_papers_with_citations.append({
            'title': title,
            'citation_count': citations_dict[title]
        })

print(f"ACM papers with 2018 citations: {len(acm_papers_with_citations)}")

if acm_papers_with_citations:
    total_citations = sum(p['citation_count'] for p in acm_papers_with_citations)
    avg_citations = total_citations / len(acm_papers_with_citations)
    result = {
        'acm_papers_count': len(acm_papers_with_citations),
        'total_citations': total_citations,
        'average_citation_count': round(avg_citations, 2)
    }
else:
    result = {
        'acm_papers_count': 0,
        'total_citations': 0,
        'average_citation_count': 0,
        'message': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'acm_papers_count': 0, 'total_citations': 0, 'average_citation_count': 0, 'message': 'No ACM papers found in 2018 citations'}, 'var_functions.execute_python:12': {'summary': {'total_2018_citations': 158, 'total_paper_docs': 5, 'acm_papers_found': 0, 'acm_papers_cited_in_2018': 0}, 'average_citation_count': 0}}

exec(code, env_args)

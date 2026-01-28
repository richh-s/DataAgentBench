code = """import json
import re

# Load the file path
chi_papers_file_path = locals()['var_functions.execute_python:18']

# Read the actual CHI papers data
with open(chi_papers_file_path, 'r') as f:
    chi_papers_data = json.load(f)

# Extract CHI paper titles
chi_papers = []
for doc in chi_papers_data:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    # Look for CHI conference patterns
    chi_patterns = [r'CHI\s*\'?\d{2}', r'CHI\s*20\d{2}', r'CHI\s+Conference', r'Proceedings of the.*?CHI', r'ACM.*?CHI', r'CHI\s*\d{4}\s*Conference']
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        chi_papers.append(title)

# Load citations data file path
citations_file_path = locals()['var_functions.execute_python:4']

# Read the citations data
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Find citations for CHI papers in 2020
total_citations = 0
cited_chi_papers = []

for citation in citations_data:
    paper_title = citation['title']
    cite_count = int(citation['citation_count'])
    
    # Check if this paper is in our CHI papers list
    if paper_title in chi_papers:
        total_citations += cite_count
        cited_chi_papers.append({
            'title': paper_title,
            'citations_2020': cite_count
        })

print("__RESULT__:")
print(json.dumps({
    'total_citations': total_citations,
    'chi_papers_count': len(chi_papers),
    'cited_papers_count': len(cited_chi_papers),
    'sample_cited_papers': cited_chi_papers[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:18': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

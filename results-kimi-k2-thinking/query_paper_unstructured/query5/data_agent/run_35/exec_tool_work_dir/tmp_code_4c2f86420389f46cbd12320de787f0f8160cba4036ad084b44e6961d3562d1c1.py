code = """import json
import re

# Load data from file paths
citations_file_path = locals()['var_functions.query_db:0']
paper_docs_file_path = locals()['var_functions.query_db:2']

with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary mapping paper titles to their CHI status
chi_papers = {}
chi_patterns = ['CHI', 'SIGCHI', 'Human Factors in Computing Systems']

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Check if this is a CHI paper
    is_chi = any(pattern in text for pattern in chi_patterns)
    
    if is_chi:
        chi_papers[title] = {'venue': 'CHI', 'year': None}

# Find CHI papers in the 2020 citations
chi_citations_2020 = []
total_citation_count = 0

for citation in citations_2020:
    title = citation['title']
    if title in chi_papers:
        citation_count = int(citation['citation_count'])
        chi_citations_2020.append({
            'title': title,
            'citation_count': citation_count
        })
        total_citation_count += citation_count

result = {
    'total_citation_count': total_citation_count,
    'matched_papers': len(chi_citations_2020)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', '__builtins__', 'json', 're']}, 'var_functions.execute_python:20': {'citations_type': "<class 'str'>", 'paper_docs_type': "<class 'str'>", 'citations_is_string': True, 'citations_preview': 'file_storage/functions.query_db:0.json', 'paper_docs_is_string': True, 'paper_docs_preview': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)

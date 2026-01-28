code = """import json
import re

# Access the stored variables  
citations_2020 = locals()['var_functions.query_db:0']
paper_docs = locals()['var_functions.query_db:2']

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
            'citation_count': citation_count,
            'venue': 'CHI'
        })
        total_citation_count += citation_count

result = {
    'total_citation_count': total_citation_count,
    'matched_papers': len(chi_citations_2020)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', '__builtins__', 'json', 're']}}

exec(code, env_args)

code = """import json
import re

# Access the stored variables
citations_2020 = locals()['var_functions.query_db:0']
paper_docs = locals()['var_functions.query_db:2']

# Create a dictionary mapping paper titles to their CHI status
chi_papers = {}

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Check if this is a CHI paper
    is_chi = False
    if 'CHI' in text or 'SIGCHI' in text or 'Human Factors in Computing Systems' in text:
        is_chi = True
    
    if is_chi:
        # Try to extract year
        year_match = re.search(r'CHI.*?[\'"]?\s*(\d{2,4})', text)
        year = None
        if year_match:
            year_str = year_match.group(1)
            if len(year_str) == 2:
                year = int('20' + year_str if int(year_str) < 50 else '19' + year_str)
            else:
                year = int(year_str)
        
        chi_papers[title] = {'venue': 'CHI', 'year': year}

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
            'venue': 'CHI',
            'year': chi_papers[title]['year']
        })
        total_citation_count += citation_count

result = {
    'total_citation_count': total_citation_count,
    'matched_chi_papers': len(chi_citations_2020),
    'total_chi_papers_found': len(chi_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', '__builtins__', 'json', 're']}}

exec(code, env_args)

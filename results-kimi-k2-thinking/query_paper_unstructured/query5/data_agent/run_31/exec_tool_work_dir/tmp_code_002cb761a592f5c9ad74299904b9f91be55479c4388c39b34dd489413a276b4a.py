code = """import json
import re

# Access the stored variables correctly
citations_var = locals()['var_functions.query_db:10']
papers_var = locals()['var_functions.query_db:5']

# Read the citations data from 2020
with open(citations_var, 'r') as f:
    citations_2020 = json.load(f)

# Read the paper documents
with open(papers_var, 'r') as f:
    papers = json.load(f)

chi_paper_titles = set()

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    if not text or not filename:
        continue
    
    # Check for CHI patterns
    chi_patterns = [
        r'CHI[\s\']+\d{2}', r'CHI[\s\d]{1,4}\d{4}', 
        r'Proceeding[^\n]{0,50}CHI', r'ACM[^\n]{0,30}CHI'
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        # Extract title from filename
        title = filename[:-4] if filename.endswith('.txt') else filename
        chi_paper_titles.add(title)

# Sum citations for CHI papers
total_citations = 0
chi_citations_count = 0

for citation in citations_2020:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if title in chi_paper_titles:
        total_citations += count
        chi_citations_count += 1

result = {
    'total_chi_citations_in_2020': total_citations,
    'chi_papers_cited': chi_citations_count,
    'chi_papers_identified': len(chi_paper_titles),
    'total_citation_records': len(citations_2020)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

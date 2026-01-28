code = """import json
import re

# Load data from previous tool calls
citation_data = var_functions.query_db:0
paper_data = var_functions.query_db:5

# Handle file paths vs direct data
if isinstance(citation_data, str) and citation_data.endswith('.json'):
    with open(citation_data, 'r') as f:
        citation_data = json.load(f)

if isinstance(paper_data, str) and paper_data.endswith('.json'):
    with open(paper_data, 'r') as f:
        paper_data = json.load(f)

print(f"Citation records: {len(citation_data)}")
print(f"Paper documents: {len(paper_data)}")

# Identify CHI papers by looking for CHI in text
chi_papers = []
chi_pattern = re.compile(r'CHI', re.IGNORECASE)

for paper in paper_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    if chi_pattern.search(text):
        title = filename.replace('.txt', '') if filename else ''
        if title:
            chi_papers.append(title.lower().strip())

print(f"CHI papers found: {len(chi_papers)}")

# Match with citations
total_citations = 0
matches = 0

for citation in citation_data:
    cit_title = citation.get('title', '').lower().strip()
    cit_count = int(citation.get('citation_count', 0))
    
    # Direct match
    if cit_title in chi_papers:
        total_citations += cit_count
        matches += 1
    else:
        # Clean both titles and try again
        clean_cit = re.sub(r'[^a-z0-9\s]', '', cit_title)
        for chi_title in chi_papers:
            clean_chi = re.sub(r'[^a-z0-9\s]', '', chi_title)
            if clean_cit == clean_chi:
                total_citations += cit_count
                matches += 1
                break

print(f"Matched papers: {matches}")
print(f"Total citations: {total_citations}")

result = {
    'total_citation_count': total_citations,
    'chi_papers_cited': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

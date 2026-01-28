code = """# Use the data from storage directly
papers_data = locals()['var_functions.query_db:2']
citations_data = locals()['var_functions.query_db:5']

# If they're file paths, read them
import json

if isinstance(papers_data, str):
    papers = json.load(open(papers_data))
else:
    papers = papers_data
    
if isinstance(citations_data, str):
    citations_2020 = json.load(open(citations_data))
else:
    citations_2020 = citations_data

# Process papers to extract CHI venue
import re

chi_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Check if it's a CHI paper by looking for CHI in text
    if 'CHI' in text or 'chi' in text.lower():
        paper['title'] = title
        chi_papers.append(paper)

chi_titles = set(p['title'].lower().strip() for p in chi_papers)

chi_citations_2020 = []
for citation in citations_2020:
    citation_title = citation.get('title', '').lower().strip()
    if citation_title in chi_titles:
        chi_citations_2020.append({
            'title': citation['title'],
            'citation_count': int(citation['citation_count']),
            'citation_year': int(citation['citation_year'])
        })

total_citations = sum(c['citation_count'] for c in chi_citations_2020)
unique_papers_count = len(chi_citations_2020)

result = str(total_citations)

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

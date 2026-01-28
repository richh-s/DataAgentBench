code = """import json
import re

papers = json.load(open('var_functions.query_db:2'))
citations_2020 = json.load(open('var_functions.query_db:5'))

chi_papers = []
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    text = paper.get('text', '')
    
    patterns = [
        r'CHI\s*\'\d{2}',
        r'CHI\s+\d{4}',
        r'Proceedings of the .*?CHI',
        r'ACM Conference on Human Factors'
    ]
    
    venue = None
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = "CHI"
            break
    
    if venue == "CHI":
        paper['title'] = title
        chi_papers.append(paper)

chi_titles = set()
for p in chi_papers:
    chi_titles.add(p['title'].lower().strip())

chi_citations_2020 = []
for citation in citations_2020:
    citation_title = citation['title'].lower().strip()
    if citation_title in chi_titles:
        chi_citations_2020.append({
            'title': citation['title'],
            'citation_count': int(citation['citation_count']),
            'citation_year': int(citation['citation_year'])
        })

total_citations = sum(c['citation_count'] for c in chi_citations_2020)
unique_papers_count = len(chi_citations_2020)

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': unique_papers_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

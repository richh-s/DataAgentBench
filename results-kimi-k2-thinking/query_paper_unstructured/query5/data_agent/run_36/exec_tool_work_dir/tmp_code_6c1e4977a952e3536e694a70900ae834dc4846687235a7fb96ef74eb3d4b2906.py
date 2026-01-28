code = """import json
import re

papers = json.load(open('var_functions.query_db:2'))
citations_2020 = json.load(open('var_functions.query_db:5'))

chi_papers = []
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    text = paper.get('text', '')
    
    pattern1 = r'CHI\s*\'\d{2}'
    pattern2 = r'CHI\s+\d{4}'
    pattern3 = r'Proceedings of the .*?CHI'
    pattern4 = r'ACM Conference on Human Factors'
    
    venue = None
    if re.search(pattern1, text, re.IGNORECASE) or \
       re.search(pattern2, text, re.IGNORECASE) or \
       re.search(pattern3, text, re.IGNORECASE) or \
       re.search(pattern4, text, re.IGNORECASE):
        venue = "CHI"
    
    if venue == "CHI":
        paper['title'] = title
        paper['venue'] = venue
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

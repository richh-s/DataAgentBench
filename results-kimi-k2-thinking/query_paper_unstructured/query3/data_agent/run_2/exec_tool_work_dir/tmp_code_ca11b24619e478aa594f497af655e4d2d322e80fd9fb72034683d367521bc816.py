code = """import json
import re
from collections import defaultdict

paper_docs_data = locals()['var_functions.query_db:2']
citations_data = locals()['var_functions.query_db:5']

paper_docs_file = paper_docs_data if isinstance(paper_docs_data, str) else None

if paper_docs_file:
    with open(paper_docs_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = []

citations = citations_data if isinstance(citations_data, list) else []

papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    year_match = re.search(r'(20[0-2][0-9])', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    text_lower = text.lower()
    contributions = []
    
    if re.search(r'empirical|study|survey|interview|experiment|evaluation', text_lower):
        contributions.append('empirical')
    
    if title:
        papers_info.append({
            'title': title,
            'year': year,
            'contributions': contributions
        })

citations_by_title = defaultdict(int)
for citation in citations:
    cit_title = citation.get('title', '').lower()
    cit_count = int(citation.get('citation_count', 0))
    citations_by_title[cit_title] += cit_count

result_papers = []
for paper in papers_info:
    year = paper.get('year')
    if year and year > 2016:
        if 'empirical' in paper.get('contributions', []):
            title = paper['title']
            title_lower = title.lower()
            total_citations = citations_by_title.get(title_lower, 0)
            result_papers.append({
                'title': title,
                'total_citations': total_citations
            })

result_papers.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(result_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)

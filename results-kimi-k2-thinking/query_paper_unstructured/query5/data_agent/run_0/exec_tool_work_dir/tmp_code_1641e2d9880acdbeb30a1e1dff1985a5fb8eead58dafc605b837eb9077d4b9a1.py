code = """import json
import re

citations_path = var_functions.query_db:0
papers_path = var_functions.query_db:2

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_path, 'r') as f:
    papers_data = json.load(f)

citation_counts = {}
for citation in citations_data:
    citation_counts[citation['title']] = int(citation['citation_count'])

chi_papers = []
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    if re.search(r'CHI', text, re.IGNORECASE):
        chi_papers.append(title)

total_citations = 0
matched_papers = []

for paper_title in chi_papers:
    if paper_title in citation_counts:
        count = citation_counts[paper_title]
        total_citations += count
        matched_papers.append({'title': paper_title, 'citation_count': count})

matched_papers.sort(key=lambda x: x['citation_count'], reverse=True)

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': len(matched_papers),
    'chi_papers_with_citations': matched_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

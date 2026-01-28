code = """import json
import os
import re

citations_data = locals()['var_functions.query_db:0']
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

papers_data = locals()['var_functions.query_db:6']
if isinstance(papers_data, str) and os.path.exists(papers_data):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

chi_papers = set()

for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename:
        continue
        
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    if 'CHI' in text.upper():
        chi_indicators = ['CHI ', 'CHI', 'CHI20', 'CHI21', 'CHI19', 'CHI18', 'CHI17', 'CHI16', 'CHI15']
        text_upper = text.upper()
        for indicator in chi_indicators:
            if indicator in text_upper:
                chi_papers.add(title)
                break

total_citations = 0
chi_citation_count = 0
matched_titles = []

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_papers:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        chi_citation_count += 1
        matched_titles.append(citation_title)

result = {
    'chi_papers_total': len(chi_papers),
    'chi_papers_cited': chi_citation_count,
    'total_citations_2020': total_citations,
    'sample_matched_titles': matched_titles[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully'}

exec(code, env_args)

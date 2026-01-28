code = """import json
import os

citations_data = locals()['var_functions.query_db:6']
paper_docs_data = locals()['var_functions.query_db:2']

if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)
        
if isinstance(paper_docs_data, str) and os.path.exists(paper_docs_data):
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

print('Total citations:', len(citations_data))
print('Total paper docs:', len(paper_docs_data))

chi_papers = []
for doc in paper_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    is_chi = False
    if 'CHI' in text or 'chi' in filename.lower():
        is_chi = True
    
    if is_chi:
        title = filename.replace('.txt', '')
        chi_papers.append(title)

print('CHI papers found:', len(chi_papers))

citations_dict = {c['title']: int(c['citation_count']) for c in citations_data if int(c.get('citation_year', 0)) == 2020}

chi_citations_total = 0
chi_citations_count = 0
for paper in chi_papers:
    if paper in citations_dict:
        chi_citations_total += citations_dict[paper]
        chi_citations_count += 1

result = {
    'total_citations_for_chi_papers_in_2020': chi_citations_total,
    'number_of_chi_papers_cited_in_2020': chi_citations_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'status': 'data_loaded'}}

exec(code, env_args)

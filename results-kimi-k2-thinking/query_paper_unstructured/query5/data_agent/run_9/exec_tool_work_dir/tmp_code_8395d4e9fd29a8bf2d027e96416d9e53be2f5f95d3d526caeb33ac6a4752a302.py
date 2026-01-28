code = """import json
import re

citation_file = locals()['var_functions.query_db:4']
paper_file = locals()['var_functions.query_db:22']

with open(citation_file, 'r') as f:
    citations_2020 = json.load(f)

with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

citation_dict = {}
for item in citations_2020:
    citation_dict[item['title']] = int(item['citation_count'])

total_citations = 0
chi_papers_count = 0
chi_papers_list = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    chi_patterns = [
        r'CHI\s+\'\d{2}',
        r'CHI\s+\d{4}',
        r'CHI\s+Conference',
        r'Conference on Human Factors in Computing Systems',
        r'Proceedings of the .* Conference on Human Factors',
        r'Proceedings of the SIGCHI Conference',
        r'ACM.*CHI'
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi and title in citation_dict:
        cite_count = citation_dict[title]
        total_citations += cite_count
        chi_papers_count += 1
        chi_papers_list.append({'title': title, 'citations': cite_count})

result = {
    'total_citations': total_citations,
    'chi_papers_cited': chi_papers_count,
    'papers': chi_papers_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'total_citations': 243, 'chi_papers_cited': 4}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'total_citations': 243, 'chi_papers_cited': 4}}

exec(code, env_args)

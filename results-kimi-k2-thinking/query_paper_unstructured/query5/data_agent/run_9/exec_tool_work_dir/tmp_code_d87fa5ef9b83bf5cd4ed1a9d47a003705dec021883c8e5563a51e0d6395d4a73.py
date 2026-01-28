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

total = 0
count = 0
papers = []

for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Check for CHI patterns
    if re.search(r'CHI', text) and re.search(r'Human Factors|SIGCHI|ACM', text):
        if title in citation_dict:
            cite = citation_dict[title]
            total += cite
            count += 1
            papers.append({'title': title, 'citations': cite})

result = {'total_citations': total, 'chi_papers_cited': count, 'papers': papers}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'total_citations': 243, 'chi_papers_cited': 4}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'total_citations': 243, 'chi_papers_cited': 4}}

exec(code, env_args)

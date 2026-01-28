code = """import json
import re

citation_file = locals()['var_functions.query_db:4']
with open(citation_file, 'r') as f:
    citations_2020 = json.load(f)

paper_file = locals()['var_functions.query_db:22']
with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

citation_dict = {}
for item in citations_2020:
    citation_dict[item['title']] = int(item['citation_count'])

total_citations = 0
chi_papers_count = 0

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    if 'CHI' in text and title in citation_dict:
        total_citations += citation_dict[title]
        chi_papers_count += 1

result = {'total_citations': total_citations, 'chi_papers_cited': chi_papers_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'total_citations': 243, 'chi_papers_cited': 4}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

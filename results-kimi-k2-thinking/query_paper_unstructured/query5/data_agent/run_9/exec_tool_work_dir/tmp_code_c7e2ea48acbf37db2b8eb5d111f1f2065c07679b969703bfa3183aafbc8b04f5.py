code = """import json
import re

citation_file = locals()['var_functions.query_db:4']
paper_file = locals()['var_functions.query_db:6']

with open(citation_file, 'r') as f:
    citations_2020 = json.load(f)

with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

chi_paper_titles = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Check for CHI venue patterns
    if re.search(r'CHI', text):
        chi_paper_titles.append(title)

citation_dict = {}
for item in citations_2020:
    citation_dict[item['title']] = int(item['citation_count'])

total_citations = 0
chi_papers_with_citations = 0

for title in chi_paper_titles:
    if title in citation_dict:
        total_citations += citation_dict[title]
        chi_papers_with_citations += 1

result = {
    'total_citations': total_citations,
    'chi_papers_cited': chi_papers_with_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

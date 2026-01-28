code = """import json, re
import pandas as pd

path_citations = var_call_ZAAx8wOu8VLjEfqpRyHEUeAj
with open(path_citations, 'r') as f:
    citations_2020 = json.load(f)

path_docs = var_call_1r9E9Ef5h5rxtm6qgEGHTnw3
with open(path_docs, 'r') as f:
    paper_docs = json.load(f)

chi_titles = set()
for doc in paper_docs:
    text = doc.get('text', '')
    header = '\n'.join(text.split('\n')[:40]).upper()
    cond1 = ' CHI ' in header
    cond2 = header.strip().startswith('CHI ')
    cond3 = "CHI '" in header
    cond4 = 'ACM CHI' in header
    if cond1 or cond2 or cond3 or cond4:
        title = doc.get('filename','')
        if title.lower().endswith('.txt'):
            title = title[:-4]
        chi_titles.add(title)

chi_citations = 0
for rec in citations_2020:
    if rec['title'] in chi_titles:
        chi_citations += int(rec['citation_count'])

result = chi_citations

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZAAx8wOu8VLjEfqpRyHEUeAj': 'file_storage/call_ZAAx8wOu8VLjEfqpRyHEUeAj.json', 'var_call_nj8zn9UzXI052KapRU175OZa': ['paper_docs'], 'var_call_1r9E9Ef5h5rxtm6qgEGHTnw3': 'file_storage/call_1r9E9Ef5h5rxtm6qgEGHTnw3.json'}

exec(code, env_args)

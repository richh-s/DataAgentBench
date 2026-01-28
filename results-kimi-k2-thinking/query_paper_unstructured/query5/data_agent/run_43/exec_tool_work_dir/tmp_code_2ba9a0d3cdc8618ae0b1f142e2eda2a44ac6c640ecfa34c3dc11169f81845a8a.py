code = """import json
import re

# Load data
citations_file = var_functions.query_db:2
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Extract CHI papers
chi_titles = set()
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text'].lower()
    if 'chi' in text[0:2000]:
        chi_titles.add(title)

# Calculate citations
total = 0
for citation in citations_2020:
    if citation['title'] in chi_titles:
        total += int(citation['citation_count'])

print('__RESULT__:')
print(json.dumps({'total_citations': total}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json

# Load citations data for 2020
citations_path = var_functions.query_db:2
with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
papers_path = var_functions.query_db:5
with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

# Build a set of CHI paper titles
chi_titles = set()
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    # Check if CHI appears near the beginning of the document
    if 'CHI' in text[0:2000]:
        chi_titles.add(title)

# Sum citations for CHI papers in 2020
total_citations = 0
for citation in citations_2020:
    if citation['title'] in chi_titles:
        total_citations += int(citation['citation_count'])

result = str(total_citations)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

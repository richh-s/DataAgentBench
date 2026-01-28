code = """import json

# Load citation data first
citation_path = locals()['var_functions.query_db:6']
with open(citation_path) as f:
    citations = json.load(f)

print('Number of papers in citation database:', len(citations))
print('Sample titles:')
for i, item in enumerate(citations[:10]):
    print('-', item['title'])

# Find papers with physical activity in title
pa_titles = []
for item in citations:
    if 'physical' in item['title'].lower() and 'activity' in item['title'].lower():
        pa_titles.append(item['title'])

print('\nPapers with physical activity in title:', len(pa_titles))
print('Sample PA titles:')
for title in pa_titles[:10]:
    print('-', title)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

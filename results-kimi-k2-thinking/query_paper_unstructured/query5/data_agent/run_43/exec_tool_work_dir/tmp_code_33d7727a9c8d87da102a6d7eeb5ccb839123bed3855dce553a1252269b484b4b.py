code = """import json

# Load citations data
citations_file = 'functions.query_db:2_result.json'
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
papers_file = 'functions.query_db:5_result.json'  
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Build set of CHI paper titles
chi_titles = set()
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    if 'CHI' in doc['text'][:2000]:
        chi_titles.add(title)

# Calculate total citations
total = 0
for citation in citations_2020:
    if citation['title'] in chi_titles:
        total += int(citation['citation_count'])

print('__RESULT__:')
print(str(total))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

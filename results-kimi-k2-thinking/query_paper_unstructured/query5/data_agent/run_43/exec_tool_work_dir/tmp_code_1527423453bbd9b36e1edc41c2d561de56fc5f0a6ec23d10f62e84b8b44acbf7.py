code = """import json

# Load citations data
citations_file = var_functions.query_db:2
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

print('Loaded data')
print('Citations 2020 count:', len(citations_2020))
print('Paper docs count:', len(paper_docs))

# Find CHI papers by checking first 2000 characters for 'CHI'
chi_paper_titles = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text_start = doc['text'][:2000]
    if 'CHI' in text_start:
        chi_paper_titles.append(title)

print('CHI papers found:', len(chi_paper_titles))

# Calculate total citations for CHI papers
total_citations = 0
for citation in citations_2020:
    if citation['title'] in chi_paper_titles:
        total_citations += int(citation['citation_count'])

print('Total citations:', total_citations)

result = {'total_citation_count': total_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

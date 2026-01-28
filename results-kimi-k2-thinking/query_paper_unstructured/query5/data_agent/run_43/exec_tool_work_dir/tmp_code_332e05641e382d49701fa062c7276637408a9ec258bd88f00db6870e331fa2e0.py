code = """import json
import os

# Access the stored data
citations_file = globals()['var_functions.query_db:2']
papers_file = globals()['var_functions.query_db:5']

print('Files loaded:', citations_file, papers_file)

# Load the actual data
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

print('Data loaded:')
print('- 2020 citations:', len(citations_2020))
print('- Paper documents:', len(paper_docs))

# More robust CHI venue detection
chi_titles = set()
chi_patterns = [
    'CHI ',
    'Proceeding of CHI',
    'Proceedings of the SIGCHI',
    'CHI Conference',
    'cscw',  # Include CSCW as it's SIGCHI
    'CSCW ',
    'Proceedings of ACM CHI'
]

for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Look for CHI venue markers in the header
    header = text[:3000]
    
    # Check patterns
    for pattern in chi_patterns:
        if pattern in header or pattern.upper() in header.upper():
            chi_titles.add(title)
            break

print('CHI papers detected:', len(chi_titles))

# Debug: Show some detected CHI papers
sample_chi = list(chi_titles)[:10]
print('Sample detected CHI papers:')
for t in sample_chi:
    print('  -', t[:80])

# Calculate total citations
total_citations = 0
chi_papers_cited = 0

for citation in citations_2020:
    cit_title = citation['title']
    if cit_title in chi_titles:
        cit_count = int(citation['citation_count'])
        total_citations += cit_count
        chi_papers_cited += 1

print('CHI papers cited in 2020:', chi_papers_cited)
print('Total citations for CHI papers in 2020:', total_citations)

result = {
    'total_citation_count': total_citations,
    'chi_papers_cited': chi_papers_cited
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:26': 0, 'var_functions.execute_python:28': {'total_citations': 16}}

exec(code, env_args)

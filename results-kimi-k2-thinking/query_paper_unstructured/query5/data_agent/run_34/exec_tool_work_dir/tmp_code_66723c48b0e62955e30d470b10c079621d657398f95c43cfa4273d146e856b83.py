code = """import json
import re

# Get CHI papers from MongoDB
chi_file_path = "file_storage/functions.query_db:26.json"
with open(chi_file_path, 'r') as f:
    chi_docs = json.load(f)

# Get citations from 2020
citations_file_path = "file_storage/functions.query_db:24.json"
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Extract CHI paper titles
chi_titles = set()
for doc in chi_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    chi_titles.add(title)

# Sum citations for CHI papers in 2020
total_citations = 0
chi_papers_cited = []

for citation in citations_2020:
    paper_title = citation['title']
    cite_count = int(citation['total_citations_2020'])
    
    if paper_title in chi_titles:
        total_citations += cite_count
        chi_papers_cited.append(paper_title)

# Prepare result
result = {
    'total_citations_count': total_citations,
    'chi_papers_identified': len(chi_titles),
    'chi_papers_cited_in_2020': len(chi_papers_cited)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:18': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

code = """import json

# Load citation data
citation_file = locals()['var_functions.query_db:2']
citations_2020 = []
with open(citation_file, 'r') as f:
    for line in f:
        citations_2020.append(json.loads(line.strip()))

# Load paper documents  
paper_file = locals()['var_functions.query_db:6']
paper_docs = []
with open(paper_file, 'r') as f:
    for line in f:
        paper_docs.append(json.loads(line.strip()))

# Create mapping of paper titles to venue
paper_venues = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '').lower()
    
    # Check if CHI paper
    if 'chi' in text:
        paper_venues[title] = 'CHI'

# Sum citations for CHI papers
total_citations = 0
chi_papers_found = 0

for citation in citations_2020:
    title = citation.get('title', '')
    if title in paper_venues:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        chi_papers_found += 1

result = {
    'total_citation_count': total_citations,
    'chi_papers_count': chi_papers_found
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

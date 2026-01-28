code = """import json
import re

# Load the citations data for 2020
citations_file = var_functions.query_db:2
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load the paper documents data
papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Extract venue information from paper documents
paper_venues = {}
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Look for venue information in the first part of the text
    header_text = text[:2000].lower()
    
    # Check if CHI appears in a context that suggests it's the venue
    if 'chi' in header_text:
        paper_venues[title] = 'CHI'

# Join with citations data
total_citations = 0
chi_papers_count = 0

for citation in citations_2020:
    cit_title = citation['title']
    cit_count = int(citation['citation_count'])
    
    if cit_title in paper_venues:
        total_citations += cit_count
        chi_papers_count += 1

# Prepare result
result = {
    'total_citation_count': total_citations,
    'chi_papers_cited': chi_papers_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

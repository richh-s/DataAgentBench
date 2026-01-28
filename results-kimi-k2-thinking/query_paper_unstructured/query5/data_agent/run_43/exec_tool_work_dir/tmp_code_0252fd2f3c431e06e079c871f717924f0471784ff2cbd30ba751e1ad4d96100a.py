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

# Count records
print('Total 2020 citations records:', len(citations_2020))
print('Total paper documents:', len(paper_docs))

# Extract venue information from paper documents
paper_venues = {}
chi_count = 0

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Look for CHI in the first part of the document (header)
    header_text = text[:2000].lower()
    
    # Pattern matching for CHI venue
    if 'chi' in header_text and ('proceedings' in header_text or 'conference' in header_text or 'acm' in header_text):
        paper_venues[title] = 'CHI'
        chi_count += 1

print('Found', chi_count, 'CHI papers in documents')

# Create a set of CHI paper titles for fast lookup
chi_titles = set(paper_venues.keys())

# Calculate total citations for CHI papers in 2020
total_citations = 0
chi_papers_with_citations = 0

for citation in citations_2020:
    cit_title = citation['title']
    if cit_title in chi_titles:
        cit_count = int(citation['citation_count'])
        total_citations += cit_count
        chi_papers_with_citations += 1

print('CHI papers cited in 2020:', chi_papers_with_citations)
print('Total citation count for CHI papers in 2020:', total_citations)

result = {
    'total_citation_count': total_citations,
    'chi_papers_cited': chi_papers_with_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

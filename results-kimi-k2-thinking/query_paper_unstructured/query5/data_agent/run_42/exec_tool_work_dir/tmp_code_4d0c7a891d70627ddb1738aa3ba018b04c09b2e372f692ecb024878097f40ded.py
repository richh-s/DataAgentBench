code = """import json
import os
import re

# Load citations data
citations_data = locals()['var_functions.query_db:0']
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

# Load paper documents data
papers_data = locals()['var_functions.query_db:6']
if isinstance(papers_data, str) and os.path.exists(papers_data):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Create mapping of paper titles to venues
chi_papers = set()

for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename:
        continue
        
    # Extract title
    title = filename.replace('.txt', '')
    
    # Check if this is a CHI paper by looking at the text
    text = doc.get('text', '')
    
    # Simple check for CHI patterns
    text_upper = text.upper()
    if 'CHI' in text_upper:
        # Additional verification to avoid false positives
        chi_indicators = ['CHI ', 'CHI\'', 'CHI,', 'CHI.', 'CHI:', '(CHI', 'CHI20', 'CHI21']
        for indicator in chi_indicators:
            if indicator in text_upper:
                chi_papers.add(title)
                break

print('Number of CHI papers found:', len(chi_papers))

# Calculate total citations for CHI papers in 2020
total_citations = 0
chi_citation_count = 0

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_papers:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        chi_citation_count += 1

print('CHI papers cited in 2020:', chi_citation_count)
print('Total citations for CHI papers in 2020:', total_citations)

result = {
    'chi_papers_count': len(chi_papers),
    'chi_papers_cited_in_2020': chi_citation_count,
    'total_citations_2020': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully'}

exec(code, env_args)

code = """import json
import os
import re

# Load the 2020 citations data
citations_key = 'var_functions.query_db:0'
citations_data = locals()[citations_key]
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

# Load all paper documents
papers_key = 'var_functions.query_db:6'
papers_data = locals()[papers_key]
if isinstance(papers_data, str) and os.path.exists(papers_data):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Create a set of CHI paper titles
chi_titles = set()

# Process each paper document
for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Get the text content
    text = doc.get('text', '')
    
    # Look for CHI venue indicators in the first part of the text (where venue info usually appears)
    text_start = text[:1000].upper()
    
    # Check if it's a CHI paper using multiple indicators
    if 'CHI' in text_start:
        # Additional verification - look for conference-related terms
        conference_terms = ['CONFERENCE', 'PROCEEDINGS', 'PAPER', 'ACM']
        if any(term in text_start for term in conference_terms):
            chi_titles.add(title)

# Now match with 2020 citations
total_citation_count = 0
chi_papers_cited = 0

# Create a mapping of titles that match
for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_titles:
        count = int(citation.get('citation_count', 0))
        total_citation_count += count
        chi_papers_cited += 1

# Also check for exact matches in the other direction (some titles might be slightly different)
# Create a simplified title mapping
simple_title_map = {}
for title in chi_titles:
    simple = title.lower().replace(' ', '').replace(':', '').replace('-', '')
    simple_title_map[simple] = title

# Try to match citations that might have slightly different formatting
for citation in citations_2020:
    citation_title = citation.get('title', '')
    simple_citation_title = citation_title.lower().replace(' ', '').replace(':', '').replace('-', '')
    
    if simple_citation_title in simple_title_map:
        count = int(citation.get('citation_count', 0))
        total_citation_count += count
        chi_papers_cited += 1

result = {
    'chi_papers_identified': len(chi_titles),
    'chi_papers_cited_in_2020': chi_papers_cited,
    'total_citation_count_2020': total_citation_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:18': {'chi_papers_total': 0, 'chi_papers_cited_2020': 0, 'total_citations_2020': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'chi_papers': 0, 'chi_cited_2020': 0, 'total_citations': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)

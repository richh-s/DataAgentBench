code = """import json
import re
from collections import defaultdict

# Load citations data from 2020
citations_result = var_functions.query_db_4

# Handle both direct data and file path
if isinstance(citations_result, str) and citations_result.endswith('.json'):
    with open(citations_result, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_result

print(f"Total citations in 2020: {len(citations_2020)}")

# Load paper documents
paper_docs_result = var_functions.query_db_5

if isinstance(paper_docs_result, str) and paper_docs_result.endswith('.json'):
    with open(paper_docs_result, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_result

print(f"Total paper documents: {len(paper_docs)}")

# Create mapping from paper title to venue
paper_venues = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text_upper = text.upper()
    
    # Check for CHI venue
    chi_patterns = [
        r'CHI\s*\'?\d{2}',
        r'CHI\s+CONFERENCE',
        r'PROCEEDINGS\s+OF\s+CHI',
        r'CHI\s+\d{4}'
    ]
    
    venue = ''
    for pattern in chi_patterns:
        if re.search(pattern, text_upper):
            venue = 'CHI'
            break
    
    paper_venues[title] = venue

# Match citations with papers and sum CHI citations
total_chi_citations = 0
chi_papers = 0
matched = 0

for citation in citations_2020:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if title in paper_venues:
        matched += 1
        if paper_venues[title] == 'CHI':
            total_chi_citations += count
            chi_papers += 1

print(f"Matched citations: {matched}")
print(f"CHI papers: {chi_papers}")
print(f"Total CHI citations in 2020: {total_chi_citations}")

result = str(total_chi_citations)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

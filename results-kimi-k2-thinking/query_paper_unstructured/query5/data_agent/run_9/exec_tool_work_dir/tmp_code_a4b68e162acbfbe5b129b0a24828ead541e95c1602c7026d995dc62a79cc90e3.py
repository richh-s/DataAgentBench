code = """import json
import re
import os

# Load all citations from 2020
citation_file = locals()['var_functions.query_db:4']
with open(citation_file, 'r') as f:
    citations_2020 = json.load(f)

# Load all paper documents
paper_file = locals()['var_functions.query_db:22']
with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

# Create a set of all paper titles from citations for fast lookup
citation_titles = set()
citation_dict = {}
for item in citations_2020:
    title = item['title']
    citation_titles.add(title)
    citation_dict[title] = int(item['citation_count'])

# Process paper documents to find CHI papers
chi_papers = []
total_citations = 0
chi_papers_with_citations = 0

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Check if this paper was presented at CHI
    # Look for CHI conference mentions
    chi_indicators = [
        r'CHI\s+\'\d{2}',  # CHI '15, CHI '16, etc.
        r'CHI\s+\d{4}',   # CHI 2015, CHI 2016, etc.
        r'CHI\s+Conference',
        r'Conference on Human Factors in Computing Systems',
        r'Proceedings of the .* Conference on Human Factors in Computing Systems',
        r'Proceedings of the SIGCHI Conference',
        r'ACM.*CHI',
    ]
    
    is_chi = False
    for pattern in chi_indicators:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    # If it's a CHI paper and has citations in 2020
    if is_chi and title in citation_titles:
        citation_count = citation_dict[title]
        total_citations += citation_count
        chi_papers_with_citations += 1
        chi_papers.append({
            'title': title,
            'citations_2020': citation_count
        })

# Prepare the final result
result = {
    'total_citation_count': total_citations,
    'chi_papers_cited_in_2020': chi_papers_with_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'total_citations': 243, 'chi_papers_cited': 4}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

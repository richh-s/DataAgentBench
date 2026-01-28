code = """import json
import re

# Access stored variables
citations_data = locals()['var_functions.query_db:2']
paper_docs_data = locals()['var_functions.query_db:5']

# Load citation data
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

# Load paper documents
if isinstance(paper_docs_data, str):
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

# Convert citation counts to integers
for citation in citations_2020:
    citation['citation_count'] = int(citation['citation_count'])

# Create mapping from paper title to citation count
title_to_citations = {}
for citation in citations_2020:
    title_to_citations[citation['title']] = citation['citation_count']

# Function to extract venue from text
venue_patterns = {
    'CHI': ['CHI', 'Proceedings of the ACM.*CHI', 'ACM.*Conference on Human Factors'],
    'Ubicomp': ['UbiComp', 'Ubiquitous Computing'],
    'CSCW': ['CSCW', 'Computer Supported Cooperative Work'],
    'DIS': ['DIS', 'Designing Interactive Systems'],
    'WWW': ['WWW', 'World Wide Web'],
    'IUI': ['IUI', 'Intelligent User Interfaces'],
    'PervasiveHealth': ['PervasiveHealth'],
    'TEI': ['TEI', 'Tangible Embedded Interaction'],
    'OzCHI': ['OzCHI']
}

def find_venue(text):
    header = text[:4000]  # Check first 4000 chars
    for venue, patterns in venue_patterns.items():
        for pattern in patterns:
            if re.search(pattern, header, re.IGNORECASE):
                return venue
    return None

# Create venue mapping
title_to_venue = {}
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    venue = find_venue(doc.get('text', ''))
    if venue:
        title_to_venue[title] = venue

# Find CHI papers cited in 2020
citation_total = 0
papers_found = 0
chi_papers = []

for title, citation_count in title_to_citations.items():
    if title in title_to_venue and title_to_venue[title] == 'CHI':
        citation_total += citation_count
        papers_found += 1
        chi_papers.append({'title': title, 'citations': citation_count})

# Sort by citation count (descending)
chi_papers.sort(key=lambda x: x['citations'], reverse=True)

# Prepare final result
final_result = {
    'total_citation_count': citation_total,
    'chi_papers_identified': papers_found,
    'top_chi_papers': chi_papers[:10]
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

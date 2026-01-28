code = """import json
import re

# Load citation data
citations_var = var_functions.query_db:2
if isinstance(citations_var, str):
    with open(citations_var, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_var

# Load paper documents
paper_docs_var = var_functions.query_db:5
if isinstance(paper_docs_var, str):
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_var

# Convert citation counts to integers
for citation in citations_2020:
    citation['citation_count'] = int(citation['citation_count'])

# Create mapping from title to citation count
citation_map = {}
for citation in citations_2020:
    citation_map[citation['title']] = citation['citation_count']

# Function to extract venue from text
def extract_paper_venue(text_content):
    # Check first part of text for venue/location info
    sample_text = text_content[:3000]
    
    venue_indicators = [
        ('CHI', ['CHI', 'Proceedings of the ACM CHI', 'ACM Conference on Human Factors']),
        ('Ubicomp', ['UbiComp', 'Ubiquitous Computing', 'Ubiq']),
        ('CSCW', ['CSCW', 'Computer Supported Cooperative Work']),
        ('DIS', ['DIS', 'Designing Interactive Systems']),
        ('WWW', ['WWW', 'World Wide Web Conference']),
        ('IUI', ['IUI', 'Intelligent User Interfaces']),
        ('TEI', ['TEI', 'Tangible Embedded Interaction']),
        ('PervasiveHealth', ['PervasiveHealth']),
        ('OzCHI', ['OzCHI'])
    ]
    
    for venue_name, patterns in venue_indicators:
        for pattern in patterns:
            if pattern.lower() in sample_text.lower():
                return venue_name
    
    return None

# Create mapping from title to venue
paper_venues = {}
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    venue = extract_paper_venue(doc.get('text', ''))
    if venue:
        paper_venues[title] = venue

# Find CHI papers cited in 2020 and calculate total citations
total_chi_citations = 0
chi_papers_found = 0
chi_papers_list = []

for paper_title in citation_map:
    if paper_title in paper_venues and paper_venues[paper_title] == 'CHI':
        citations = citation_map[paper_title]
        total_chi_citations += citations
        chi_papers_found += 1
        chi_papers_list.append({'title': paper_title, 'citations': citations})

# Sort by citation count descending
chi_papers_list.sort(key=lambda x: x['citations'], reverse=True)

output = {
    'total_citations': total_chi_citations,
    'number_of_chi_papers': chi_papers_found,
    'sample_papers': chi_papers_list[:10]
}

import json as js
print('__RESULT__:')
print(js.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

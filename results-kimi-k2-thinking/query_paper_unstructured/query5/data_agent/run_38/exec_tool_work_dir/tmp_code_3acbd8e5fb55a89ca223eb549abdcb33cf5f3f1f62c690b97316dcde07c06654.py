code = """import json
import re

# Read the citation data from 2020
citations_data = var_functions.query_db:2

# Read the paper documents data
paper_docs_data = var_functions.query_db:5

# Check if data is a file path (string) or actual data (list)
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_data

if isinstance(paper_docs_data, str):
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

# Convert citation counts to integers
for cit in citations:
    cit['citation_count'] = int(cit['citation_count'])

# Create a mapping from title to citation count
title_to_citation = {cit['title']: cit['citation_count'] for cit in citations}

# Function to extract venue from paper text
venue_patterns = [
    (r'CHI\s*\'\d{2}|CHI\s+\d{4}|Proceedings of the .*CHI|ACM .*CHI', 'CHI'),
    (r'UbiComp|Ubiq|Ubiquitous', 'Ubicomp'),
    (r'CSCW|Computer Supported Cooperative Work', 'CSCW'),
    (r'DIS|Designing Interactive Systems', 'DIS'),
    (r'PervasiveHealth', 'PervasiveHealth'),
    (r'WWW|World Wide Web', 'WWW'),
    (r'IUI|Intelligent User Interfaces', 'IUI'),
    (r'OzCHI', 'OzCHI'),
    (r'TEI|Tangible Embedded Interaction', 'TEI'),
    (r'AH|Augmented Human', 'AH')
]

def extract_venue(text):
    # Look for venue patterns in the first part of the text (usually header)
    header = text[:2000]  # Check first 2000 characters
    
    for pattern, venue_name in venue_patterns:
        if re.search(pattern, header, re.IGNORECASE):
            return venue_name
    
    # Also check for common conference/journal indicators
    if re.search(r'Proceedings of the ACM|ACM Press|ACM', header):
        # Look for venue near ACM
        lines = header.split('\n')
        for line in lines:
            if 'ACM' in line and ('CHI' in line or 'Conference' in line):
                return 'CHI' if 'CHI' in line else None
    
    return None

# Extract venue for each paper and create title to venue mapping
title_to_venue = {}
for doc in paper_docs:
    filename = doc['filename']
    # Remove .txt extension to get title
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    venue = extract_venue(text)
    if venue:
        title_to_venue[title] = venue

# Find CHI papers that have citations in 2020 and sum their citations
total_citations = 0
chi_papers_count = 0
matched_papers = []

for title, citation_count in title_to_citation.items():
    # Check if this paper is in our venue mapping and is CHI
    if title in title_to_venue and title_to_venue[title] == 'CHI':
        total_citations += citation_count
        chi_papers_count += 1
        matched_papers.append({'title': title, 'citations': citation_count})

# Sort matched papers by citation count (descending)
matched_papers.sort(key=lambda x: x['citations'], reverse=True)

result = {
    'total_citations': total_citations,
    'chi_papers_count': chi_papers_count,
    'top_papers': matched_papers[:10]  # Top 10 for preview
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

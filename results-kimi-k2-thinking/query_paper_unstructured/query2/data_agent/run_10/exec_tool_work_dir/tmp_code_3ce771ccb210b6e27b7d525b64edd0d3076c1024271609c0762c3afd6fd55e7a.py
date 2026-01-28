code = """import json
import pandas as pd

# Load citations data
citations_file_key = 'var_functions.query_db:0'
acm_citations_file_key = 'var_functions.query_db:2'

# Access the variables using locals()
citations_file = locals()[citations_file_key]
papers_file = locals()[acm_citations_file_key]

# Read the citations data
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Read the papers data
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

print(f"Total citations in 2018: {len(citations_2018)}")
print(f"Total paper documents: {len(paper_docs)}")

# Extract paper info from documents and identify ACM papers
acm_titles = set()
paper_lookup = {}

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    # Determine source by looking for publisher patterns in text
    text_lower = text.lower()
    
    # Check for ACM patterns - more robust detection
    is_acm = False
    if any(pattern in text_lower for pattern in ['acm', 'doi.org/10.1145', 'doi/10.1145']):
        is_acm = True
    elif 'association for computing machinery' in text_lower:
        is_acm = True
    
    if is_acm:
        acm_titles.add(title)
        paper_lookup[title] = 'ACM'

print(f"Found {len(acm_titles)} ACM papers")

# Find ACM citations from 2018
acm_citation_counts = []
for cit in citations_2018:
    cit_title = cit.get('title', '')
    if cit_title in acm_titles:
        count = int(cit.get('citation_count', 0))
        acm_citation_counts.append(count)

print(f"Found {len(acm_citation_counts)} ACM citations in 2018")

# Calculate average if we have data
if acm_citation_counts:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_papers': len(acm_citation_counts),
        'total_citations': sum(acm_citation_counts)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_papers': 0,
        'total_citations': 0,
        'message': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

code = """import json
import re

# Access the stored results
all_vars = locals()

# Get the file paths from the storage variables
citations_file = all_vars.get('var_functions.query_db:2')
papers_file = all_vars.get('var_functions.query_db:5')

if not citations_file or not papers_file:
    print("Error: Could not find stored results")
    print(f"Available keys: {list(all_vars.keys())}")
    exit()

# Load the data
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Convert citation data to a dict for easier lookup
citation_dict = {}
for cite in citations_2018:
    citation_dict[cite['title']] = int(cite['citation_count'])

# Process paper documents to extract source information
acm_papers = []

for doc in paper_docs:
    # Extract title from filename
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Get text content
    text = doc.get('text', '')
    
    # Check if this is an ACM paper
    # Look for ACM references in the text
    has_acm = False
    
    # Check for common ACM patterns
    acm_patterns = [
        'ACM',
        'Association for Computing Machinery',
        'ACM Digital Library',
        'Permission to make digital or hard copies',
        'ACM 978-'
    ]
    
    for pattern in acm_patterns:
        if pattern.lower() in text.lower():
            has_acm = True
            break
    
    # Also check for ACM venues with ACM reference
    if not has_acm:
        acm_venues = ['Proceedings of the ACM', 'ACM Conference', 'ACM SIG']
        for venue in acm_venues:
            if venue.lower() in text.lower():
                has_acm = True
                break
    
    if has_acm:
        acm_papers.append(title)

# Find ACM papers that have citations in 2018
acm_citations = []
for title in acm_papers:
    if title in citation_dict:
        acm_citations.append({
            'title': title,
            'citation_count': citation_dict[title]
        })

# Calculate statistics
if acm_citations:
    total_citations = sum(p['citation_count'] for p in acm_citations)
    avg_citations = total_citations / len(acm_citations)
    
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': len(acm_citations),
        'total_citations': total_citations
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

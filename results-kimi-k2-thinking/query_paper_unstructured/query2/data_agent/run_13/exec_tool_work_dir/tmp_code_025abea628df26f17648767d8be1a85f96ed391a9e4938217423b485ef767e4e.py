code = """import json
import re

# Read citation data
citation_file_path = locals()['var_functions.query_db:0']
citation_data = []
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

# Read paper documents
doc_file_path = locals()['var_functions.query_db:2']
paper_docs = []
with open(doc_file_path, 'r') as f:
    paper_docs = json.load(f)

# Debug: Check first few citations and documents
print(f"Total citations in 2018: {len(citation_data)}")
print(f"Total paper documents: {len(paper_docs)}")

# Create a mapping of normalized titles to citation counts
citation_map = {}
for cite in citation_data:
    title = cite.get('title', '').strip().lower()
    count = int(cite.get('citation_count', 0))
    citation_map[title] = count

# Extract ACM papers and their citation counts
acm_citations = []
matched_titles = []
acm_patterns = [
    r'\\bACM\\b',
    r'ACM Classification Keywords',
    r'Copyright.*\\bACM\\b',
    r'Permission to make.*ACM'
]

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    normalized_title = title.strip().lower()
    
    # Check if paper is from ACM by searching for ACM patterns
    is_acm = False
    for pattern in acm_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_acm = True
            break
    
    # Check if this paper has citation data for 2018
    if is_acm and normalized_title in citation_map:
        citation_count = citation_map[normalized_title]
        acm_citations.append(citation_count)
        matched_titles.append((title, citation_count))

# Debug: Show some matched titles
print(f"\\nFound {len(acm_citations)} ACM papers with 2018 citations:")
for i, (title, count) in enumerate(matched_titles[:10]):
    print(f"  {i+1}. {title} - {count} citations")

# Calculate average citation count
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers_with_citations': len(acm_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers_with_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'average_citation_count': 68.5, 'total_acm_papers_with_citations': 2}}

exec(code, env_args)

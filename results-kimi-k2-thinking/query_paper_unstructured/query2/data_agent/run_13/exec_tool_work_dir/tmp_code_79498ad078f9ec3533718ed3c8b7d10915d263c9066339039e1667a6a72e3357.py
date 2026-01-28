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

# Create a mapping of title to citation count for 2018
citation_map = {}
for cite in citation_data:
    title = cite.get('title', '')
    count = int(cite.get('citation_count', 0))
    citation_map[title] = count

# Extract ACM papers and their citation counts
acm_citations = []
matched_titles = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is from ACM by searching for ACM in the text
    # Common indicators: "ACM Classification", "Copyright ... ACM", "ACM, Inc."
    is_acm = bool(re.search(r'\\bACM\\b', text, re.IGNORECASE))
    
    # Check if this paper has citation data for 2018
    if is_acm and title in citation_map:
        acm_citations.append(citation_map[title])
        matched_titles.append((title, citation_map[title]))

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

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

code = """import json
import re

# Load citation data for 2018
citation_file = var_functions.query_db:0
citation_data = []
with open(citation_file, 'r') as f:
    for line in f:
        citation_data.append(json.loads(line))

# Load paper documents
paper_file = var_functions.query_db:2  
paper_data = []
with open(paper_file, 'r') as f:
    for line in f:
        paper_data.append(json.loads(line))

print("Citations loaded:", len(citation_data))
print("Paper documents loaded:", len(paper_data))

# Extract ACM papers
acm_papers = []
for paper in paper_data:
    text = paper.get('text', '').lower()
    # Check for ACM references in the text
    if 'acm' in text or 'association for computing machinery' in text:
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        acm_papers.append(title)

print("ACM papers found:", len(acm_papers))

# Match with citations and calculate average
citation_dict = {item['title']: int(item['citation_count']) for item in citation_data}
matched_citations = []

for title in acm_papers:
    if title in citation_dict:
        matched_citations.append(citation_dict[title])

print("Matched citations:", len(matched_citations))

if matched_citations:
    avg_citations = sum(matched_citations) / len(matched_citations)
    print(f"Average citations for ACM papers in 2018: {avg_citations:.2f}")
else:
    print("No matches found")

print(f"__RESULT__: {json.dumps({'avg_citations': avg_citations if matched_citations else 0, 'matches': len(matched_citations)})}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

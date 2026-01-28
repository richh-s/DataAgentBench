code = """import json
import re

# Load citation data for 2018
citation_file = locals()['var_functions.query_db:0']
citation_data = []
with open(citation_file, 'r') as f:
    for line in f:
        citation_data.append(json.loads(line))

# Load paper documents
paper_file = locals()['var_functions.query_db:2']
paper_data = []
with open(paper_file, 'r') as f:
    for line in f:
        paper_data.append(json.loads(line))

# Extract ACM papers
acm_titles = set()
for paper in paper_data:
    text = paper.get('text', '').lower()
    if 'acm' in text or 'association for computing machinery' in text:
        filename = paper.get('filename', '')
        if filename:
            title = filename.replace('.txt', '')
            acm_titles.add(title)

# Create citation dictionary
citation_dict = {}
for item in citation_data:
    citation_dict[item['title']] = int(item['citation_count'])

# Find matching citations for ACM papers
matched_citations = []
matched_titles = []

for title in acm_titles:
    if title in citation_dict:
        matched_citations.append(citation_dict[title])
        matched_titles.append(title)

# Calculate average
avg_citations = 0
if matched_citations:
    avg_citations = sum(matched_citations) / len(matched_citations)

result = {
    'avg_citations': avg_citations,
    'matched_papers': len(matched_citations),
    'total_acm_papers': len(acm_titles),
    'total_citations_2018': len(citation_data)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

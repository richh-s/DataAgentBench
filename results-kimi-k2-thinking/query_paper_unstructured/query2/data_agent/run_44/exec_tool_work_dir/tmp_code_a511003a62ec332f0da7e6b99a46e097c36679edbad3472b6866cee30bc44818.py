code = """import json
import os
import re

# Load citation data for 2018
citation_file = locals()['var_functions.query_db:0']
citation_data = None

with open(citation_file, 'r') as f:
    content = f.read().strip()
    if content.startswith('[') and content.endswith(']'):
        citation_data = json.loads(content)
    else:
        citation_data = []
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line:
                try:
                    citation_data.append(json.loads(line))
                except:
                    continue

# Load paper documents
paper_file = locals()['var_functions.query_db:2']
paper_data = None

with open(paper_file, 'r') as f:
    content = f.read().strip()
    if content.startswith('[') and content.endswith(']'):
        paper_data = json.loads(content)
    else:
        paper_data = []
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line:
                try:
                    paper_data.append(json.loads(line))
                except:
                    continue

# Extract ACM papers and their titles
acm_titles = set()
for paper in paper_data:
    text = paper.get('text', '').lower()
    # Check for ACM in the text
    if 'acm' in text:
        filename = paper.get('filename', '')
        if filename:
            title = filename.replace('.txt', '')
            acm_titles.add(title)

# Create citation dictionary for easy lookup
citation_dict = {}
for item in citation_data:
    citation_dict[item['title']] = int(item['citation_count'])

# Find matching citations for ACM papers
matched_citations = []
for title in acm_titles:
    if title in citation_dict:
        matched_citations.append(citation_dict[title])

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

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'status': 'files_checked'}}

exec(code, env_args)

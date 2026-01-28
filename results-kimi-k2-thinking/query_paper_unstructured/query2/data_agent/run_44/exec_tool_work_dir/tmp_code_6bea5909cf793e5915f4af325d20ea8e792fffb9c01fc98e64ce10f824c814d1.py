code = """import json
import re

# Load citation data for 2018
citation_key = 'var_functions.query_db:0'
citation_content = locals()[citation_key]

# Load paper documents
paper_key = 'var_functions.query_db:2'
paper_content = locals()[paper_key]

# For file paths, we need to read the files
citation_data = []
paper_data = []

if isinstance(citation_content, str) and citation_content.endswith('.json'):
    with open(citation_content, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                citation_data.append(json.loads(line))

if isinstance(paper_content, str) and paper_content.endswith('.json'):
    with open(paper_content, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                paper_data.append(json.loads(line))

# Extract ACM papers
acm_titles = set()
for paper in paper_data:
    text = paper.get('text', '').lower()
    if 'acm' in text:
        filename = paper.get('filename', '')
        if filename:
            title = filename.replace('.txt', '')
            acm_titles.add(title)

# Create citation dictionary
citation_dict = {}
for item in citation_data:
    citation_dict[item['title']] = int(item['citation_count'])

# Find matches
matched_citations = []
for title in acm_titles:
    if title in citation_dict:
        matched_citations.append(citation_dict[title])

avg_citations = sum(matched_citations) / len(matched_citations) if matched_citations else 0

result = {
    'avg_citations': avg_citations,
    'matched_papers': len(matched_citations),
    'total_citations': len(citation_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'status': 'files_checked'}}

exec(code, env_args)

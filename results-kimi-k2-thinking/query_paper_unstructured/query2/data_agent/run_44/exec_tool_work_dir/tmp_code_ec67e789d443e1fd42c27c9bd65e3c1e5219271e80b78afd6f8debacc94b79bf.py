code = """import json
import os

# Load the citation data for 2018
citation_file = locals()['var_functions.query_db:0']
citation_data = []
with open(citation_file, 'r') as f:
    content = f.read().strip()
    if content.startswith('[') and content.endswith(']'):
        citation_data = json.loads(content)
    else:
        for line in content.split('\n'):
            line = line.strip()
            if line and line != 'null' and line != 'None':
                try:
                    citation_data.append(json.loads(line))
                except:
                    continue

# Load the ACM papers from the query
acm_file = locals()['var_functions.query_db:26']
acm_papers = []
with open(acm_file, 'r') as f:
    content = f.read().strip()
    if content.startswith('[') and content.endswith(']'):
        acm_papers = json.loads(content)
    else:
        for line in content.split('\n'):
            line = line.strip()
            if line and line != 'null' and line != 'None':
                try:
                    acm_papers.append(json.loads(line))
                except:
                    continue

# Extract titles from ACM papers
acm_titles = set()
for paper in acm_papers:
    filename = paper.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        acm_titles.add(title)

# Create citation dictionary for 2018
citation_dict = {}
for item in citation_data:
    citation_dict[item['title']] = int(item['citation_count'])

# Find matching citations
matched_citations = []
for title in acm_titles:
    if title in citation_dict:
        matched_citations.append(citation_dict[title])

# Calculate average citation count
avg_citations = 0
if matched_citations:
    avg_citations = sum(matched_citations) / len(matched_citations)

result = {
    'average_citation_count_2018': round(avg_citations, 2),
    'acm_papers_with_citations': len(matched_citations),
    'total_acm_papers_identified': len(acm_titles),
    'total_citation_records_2018': len(citation_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'status': 'files_checked'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

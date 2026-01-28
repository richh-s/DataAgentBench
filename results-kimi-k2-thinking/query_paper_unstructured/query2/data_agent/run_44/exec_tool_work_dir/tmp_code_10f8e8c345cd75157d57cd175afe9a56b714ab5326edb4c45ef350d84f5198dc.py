code = """import json

# Load citations for 2018 - these are JSON array format
citation_file = locals()['var_functions.query_db:0']
with open(citation_file, 'r') as f:
    citation_data = json.load(f)

# Load ACM papers - these are also JSON array format
acm_file = locals()['var_functions.query_db:26']
with open(acm_file, 'r') as f:
    acm_data = json.load(f)

# Extract ACM paper titles
acm_titles = set()
for paper in acm_data:
    filename = paper.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        acm_titles.add(title)

# Create dictionary of citations for 2018
citation_dict = {item['title']: int(item['citation_count']) for item in citation_data}

# Find matching ACM papers that have citations in 2018
matched_citations = []
for title in acm_titles:
    if title in citation_dict:
        matched_citations.append(citation_dict[title])

# Calculate average
if matched_citations:
    avg_citations = sum(matched_citations) / len(matched_citations)
else:
    avg_citations = 0

result = {
    'average_citation_count': round(avg_citations, 2),
    'acm_papers_with_citations_2018': len(matched_citations),
    'total_acm_papers_identified': len(acm_titles),
    'total_citation_records_2018': len(citation_data)
}

# Print in expected format
print('__RESULT__')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'status': 'files_checked'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

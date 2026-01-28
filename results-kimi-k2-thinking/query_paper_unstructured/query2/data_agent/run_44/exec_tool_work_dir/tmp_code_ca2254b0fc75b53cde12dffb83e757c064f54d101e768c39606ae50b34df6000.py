code = """import json

# Load citations for 2018
citation_file = locals()['var_functions.query_db:0']
citation_data = []
with open(citation_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            citation_data.append(json.loads(line))

# Load ACM papers
acm_file = locals()['var_functions.query_db:26']
acm_data = []
with open(acm_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            acm_data.append(json.loads(line))

# Get ACM titles
acm_titles = set()
for paper in acm_data:
    fname = paper.get('filename', '')
    if fname:
        acm_titles.add(fname.replace('.txt', ''))

# Match with citations
citation_dict = {item['title']: int(item['citation_count']) for item in citation_data}
matched = [citation_dict[title] for title in acm_titles if title in citation_dict]

avg_citations = sum(matched) / len(matched) if matched else 0

print('__RESULT__')
print(json.dumps({'avg': round(avg_citations, 2), 'papers': len(matched), 'total_acm': len(acm_titles)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'status': 'files_checked'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

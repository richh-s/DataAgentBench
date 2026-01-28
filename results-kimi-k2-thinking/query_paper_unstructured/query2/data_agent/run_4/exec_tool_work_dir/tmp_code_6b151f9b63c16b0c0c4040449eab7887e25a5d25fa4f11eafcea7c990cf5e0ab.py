code = """import json

# Get citation data
cit_data = locals().get('var_functions.query_db:0', [])

# Get paper documents
paper_data = locals().get('var_functions.query_db:2', [])

# Check if they're file paths
if isinstance(cit_data, str) and '.json' in cit_data:
    with open(cit_data) as f:
        cit_data = json.load(f)

if isinstance(paper_data, str) and '.json' in paper_data:
    with open(paper_data) as f:
        paper_data = json.load(f)

# Build paper title map
paper_map = {}
for p in paper_data:
    fn = p.get('filename', '')
    title = fn[:-4] if fn.endswith('.txt') else fn
    paper_map[title] = p

# Find ACM papers
acm_counts = []
for cit in cit_data:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    paper = paper_map.get(title)
    if paper:
        text = paper.get('text', '').upper()
        if 'ACM' in text and ('10.1145' in text or 'PERMISSION' in text):
            acm_counts.append(count)

# Calculate average
avg = sum(acm_counts) / len(acm_counts) if acm_counts else None
result = {'average_citation_count': avg, 'acm_papers_count': len(acm_counts)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

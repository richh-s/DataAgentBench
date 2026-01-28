code = """import json

# Load data from previous queries
cit_2018 = var_functions.query_db:0
paper_docs = var_functions.query_db:2

# Handle file paths if results are large
if isinstance(cit_2018, str) and '.json' in cit_2018:
    with open(cit_2018) as f:
        cit_2018 = json.load(f)

if isinstance(paper_docs, str) and '.json' in paper_docs:
    with open(paper_docs) as f:
        paper_docs = json.load(f)

# Build map of paper titles to documents
paper_map = {}
for p in paper_docs:
    fn = p.get('filename', '')
    title = fn[:-4] if fn.endswith('.txt') else fn
    paper_map[title] = p

# Find ACM papers among 2018 citations
acm_citations = []
for cit in cit_2018:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    
    paper = paper_map.get(title)
    if paper:
        text = paper.get('text', '').upper()
        # Check for ACM publication indicators
        has_acm = 'ACM' in text
        has_doi = '10.1145' in text
        has_permission = 'PERMISSION' in text
        
        if has_acm and (has_doi or has_permission):
            acm_citations.append(count)

# Calculate average
total = sum(acm_citations)
count = len(acm_citations)
avg = total / count if count > 0 else None

print('__RESULT__:')
print(json.dumps({'average': avg, 'count': count}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

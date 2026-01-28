code = """import json

# Load cit 2018 data
cit_2018 = var_functions.query_db:0
if isinstance(cit_2018, str) and '.json' in cit_2018:
    with open(cit_2018) as f:
        cit_2018 = json.load(f)

# Load paper docs
paper_docs = var_functions.query_db:2
if isinstance(paper_docs, str) and '.json' in paper_docs:
    with open(paper_docs) as f:
        paper_docs = json.load(f)

# Build paper title map (filename without .txt)
paper_map = {}
for p in paper_docs:
    fn = p.get('filename', '')
    if fn:
        title = fn[:-4] if fn.endswith('.txt') else fn
        paper_map[title] = p

# Find ACM papers and their 2018 citations
acm_papers = []
for cit in cit_2018:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    
    paper = paper_map.get(title)
    if paper:
        text = paper.get('text', '').upper()
        # Check ACM indicators
        if 'ACM' in text:
            if any(x in text for x in ['10.1145', 'PERMISSION TO', 'ACM CLASSIFICATION']):
                acm_papers.append(count)

total = sum(acm_papers) if acm_papers else 0
avg = total / len(acm_papers) if acm_papers else None

print('__RESULT__:')
print(json.dumps({'avg': avg, 'count': len(acm_papers)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

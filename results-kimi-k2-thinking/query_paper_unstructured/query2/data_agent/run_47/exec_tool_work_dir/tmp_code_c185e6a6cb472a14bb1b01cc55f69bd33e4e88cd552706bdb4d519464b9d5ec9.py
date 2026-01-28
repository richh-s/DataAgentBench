code = """import json

# Get the data using locals() since variable names have colons
citations = locals()['var_functions.query_db:0']
papers = locals()['var_functions.query_db:5']

# If they're file paths, load them
if isinstance(citations, str):
    with open(citations) as f:
        citations = json.load(f)

if isinstance(papers, str):
    with open(papers) as f:
        papers = json.load(f)

# Find ACM papers
acm_titles = set()
for paper in papers:
    text = paper.get('text', '').upper()
    if 'ACM' in text:
        fname = paper.get('filename', '')
        if fname:
            title = fname.replace('.txt', '')
            acm_titles.add(title)

# Match with citations
citation_counts = []
for cit in citations:
    title = cit.get('title', '')
    if title in acm_titles:
        citation_counts.append(int(cit.get('citation_count', 0)))

# Calculate average
if citation_counts:
    total = sum(citation_counts)
    count = len(citation_counts)
    avg = total / count
    result = {
        'average': round(avg, 2),
        'papers': count,
        'citations': total
    }
else:
    result = {'average': 0, 'papers': 0, 'citations': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

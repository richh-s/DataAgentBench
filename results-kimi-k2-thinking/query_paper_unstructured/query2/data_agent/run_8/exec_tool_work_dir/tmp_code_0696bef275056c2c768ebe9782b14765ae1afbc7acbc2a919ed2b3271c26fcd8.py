code = """import json

# Load data
citations_2018 = json.load(open('var_functions.query_db:18'))
paper_docs = json.load(open('var_functions.query_db:20'))

# Simple checks
print('Citations loaded:', len(citations_2018))
print('Papers loaded:', len(paper_docs))

# Find ACM papers
acm_papers = []
for doc in paper_docs:
    text = doc.get('text', '')
    title = doc.get('filename', '').replace('.txt', '')
    
    # Check ACM
    is_acm = ('ACM' in text) or ('10.1145' in text) or ('Association for Computing Machinery' in text)
    
    if is_acm:
        acm_papers.append(title)

print('ACM papers:', len(acm_papers))

# Map citations
citation_dict = {}
for item in citations_2018:
    citation_dict[item['title']] = int(item['citation_count'])

# Match
matches = []
for paper in acm_papers:
    if paper in citation_dict:
        matches.append(citation_dict[paper])

print('Matches:', len(matches))

# Calculate
if matches:
    avg = sum(matches) / len(matches)
    result = {'avg': round(avg, 2), 'papers': len(matches), 'total': sum(matches)}
else:
    result = {'avg': 0, 'papers': 0, 'total': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'average_citations': 0, 'total_papers': 0, 'total_citations': 0}}

exec(code, env_args)

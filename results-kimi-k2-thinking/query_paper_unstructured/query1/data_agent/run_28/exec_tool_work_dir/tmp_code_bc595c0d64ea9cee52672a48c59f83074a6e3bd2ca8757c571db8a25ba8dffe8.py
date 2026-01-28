code = """import json

# Load the data
citations = json.load(open(locals()['var_functions.query_db:2'])) if isinstance(locals()['var_functions.query_db:2'], str) else locals()['var_functions.query_db:2']
papers = json.load(open(locals()['var_functions.query_db:22'])) if isinstance(locals()['var_functions.query_db:22'], str) else locals()['var_functions.query_db:22']

print('Papers:', len(papers), 'Citations:', len(citations))

# Find food papers
food_papers = []
for doc in papers:
    if 'food' in doc.get('text','').lower() or 'eating' in doc.get('text','').lower():
        food_papers.append(doc.get('filename',''))
print('Food papers:', len(food_papers))

# Check titles in citations for food
food_citations = []
for c in citations:
    title = c.get('title','').lower()
    if 'food' in title or 'diet' in title:
        food_citations.append(int(c.get('citation_count',0)))

print('Food citation total:', sum(food_citations))

result = {'total_citation_count': sum(food_citations)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}, 'var_functions.execute_python:38': {'total_citation_count': 0}, 'var_functions.execute_python:42': {'total_citation_count': 0, 'matched_papers': 0}}

exec(code, env_args)

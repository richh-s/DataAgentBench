code = """import json

# Access the data by reading from storage keys
citations_data = locals()['var_functions.query_db:2']
paper_docs_data = locals()['var_functions.query_db:22']

# Load the data (they might be file paths or direct data)
if citations_data.__class__ is str and citations_data.endswith('.json'):
    with open(citations_data) as f:
        citations = json.load(f)
else:
    citations = citations_data

if paper_docs_data.__class__ is str and paper_docs_data.endswith('.json'):
    with open(paper_docs_data) as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

print('Paper documents count:', len(paper_docs))
print('Citation records count:', len(citations))

# Look for food papers
food_papers = []
for doc in paper_docs:
    text_lower = doc.get('text', '').lower()
    if 'food' in text_lower:
        title = doc.get('filename', '').replace('.txt', '')
        food_papers.append(title)

print('Food papers found:', len(food_papers))
for fp in food_papers[:10]:
    print('-', fp)

# Check citation data structure
print('\nCitation data keys:', list(citations[0].keys()))
print('Sample titles:', [c['title'] for c in citations[:5]])

# Search for food-related titles in citations
food_in_citations = []
for c in citations:
    title_lower = c.get('title', '').lower()
    if 'food' in title_lower or 'eating' in title_lower or 'diet' in title_lower:
        food_in_citations.append(c)

print('\nFood-related citations by title:', len(food_in_citations))
for fc in food_in_citations[:5]:
    print('-', fc['title'], fc['citation_count'])

# Sum food-related citations
food_citation_total = sum(int(c.get('citation_count', 0)) for c in food_in_citations)
print('\nTotal food citations from title matching:', food_citation_total)

result = {'total_citation_count': food_citation_total}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}, 'var_functions.execute_python:38': {'total_citation_count': 0}, 'var_functions.execute_python:42': {'total_citation_count': 0, 'matched_papers': 0}}

exec(code, env_args)

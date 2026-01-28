code = """import json

# Load data
citations_var = locals()['var_functions.query_db:2']
paper_docs_var = locals()['var_functions.query_db:22']

citations = citations_var
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    citations = json.load(open(citations_var))

paper_docs = paper_docs_var
if isinstance(paper_docs_var, str) and paper_docs_var.endswith('.json'):
    paper_docs = json.load(open(paper_docs_var))

# Check paper papers
print('Paper documents:')
print('Total papers:', len(paper_docs))
print('First paper filename:', paper_docs[0].get('filename'))
print('First paper text preview (first 500 chars):')
print(paper_docs[0].get('text')[:500])
print('---')

# Look for food in papers
food_found = []
for i, doc in enumerate(paper_docs[:20]):  # Check first 20
    text = doc.get('text', '').lower()
    if 'food' in text:
        food_found.append(doc.get('filename'))
        print(f'Food found in paper {i}:', doc.get('filename'))

print('\nFood papers found (first 20):', len(food_found))

# Check citations structure
print('\nCitations:')
print('Total citations:', len(citations))
if len(citations) > 0:
    print('Sample citation titles:')
    for i in range(min(5, len(citations))):
        print(f"  {citations[i].get('title', 'NO TITLE')}")

# Check for exact title matches between papers and citations
paper_titles = [doc.get('filename', '').replace('.txt', '') for doc in paper_docs]
citation_titles = [c.get('title', '') for c in citations]

common = set(paper_titles).intersection(set(citation_titles))
print('\nExact title matches between papers and citations:', len(common))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}, 'var_functions.execute_python:38': {'total_citation_count': 0}, 'var_functions.execute_python:42': {'total_citation_count': 0, 'matched_papers': 0}}

exec(code, env_args)

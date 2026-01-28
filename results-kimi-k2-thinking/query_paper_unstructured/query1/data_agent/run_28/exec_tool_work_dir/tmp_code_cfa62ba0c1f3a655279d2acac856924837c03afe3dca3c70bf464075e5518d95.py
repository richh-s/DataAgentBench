code = """import json
import pandas as pd
from difflib import get_close_matches

# Access stored data
citations_var = locals()['var_functions.query_db:2']
paper_docs_var = locals()['var_functions.query_db:22']

# Load citations
citations = citations_var
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    citations = json.load(open(citations_var))

# Load paper documents
paper_docs = paper_docs_var
if isinstance(paper_docs_var, str) and paper_docs_var.endswith('.json'):
    paper_docs = json.load(open(paper_docs_var))

# Build citation map
citation_map = {}
for c in citations:
    title = c.get('title', '')
    count = int(c.get('citation_count', 0))
    citation_map[title] = citation_map.get(title, 0) + count

# Process papers
food_titles = []
for doc in paper_docs:
    text = doc.get('text', '').lower()
    if 'food' in text or 'eating' in text or 'diet' in text:
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '')
        food_titles.append(title)

# Match with fuzzy matching
citation_titles = list(citation_map.keys())
total_citations = 0
matched_papers = 0

for food_title in food_titles:
    matches = get_close_matches(food_title, citation_titles, n=1, cutoff=0.6)
    if matches:
        total_citations += citation_map[matches[0]]
        matched_papers += 1

result = {"total_citation_count": total_citations, "matched_papers": matched_papers}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}, 'var_functions.execute_python:38': {'total_citation_count': 0}}

exec(code, env_args)

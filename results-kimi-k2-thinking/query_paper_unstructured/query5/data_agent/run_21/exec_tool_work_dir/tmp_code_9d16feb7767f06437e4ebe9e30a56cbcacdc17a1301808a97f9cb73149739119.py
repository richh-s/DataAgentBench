code = """import json
import re

# Get data from storage
citations_file = locals()['var_functions.query_db:2']
paper_docs_file = locals()['var_functions.query_db:5']

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_file, 'r') as f:
    paper_docs_data = json.load(f)

# Find CHI papers in the corpus
chi_titles = set()
for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Check if this is a CHI paper
    text_sample = text[:2000]
    if 'CHI' in text_sample.upper():
        chi_titles.add(title)

# Count citations for CHI papers in 2020
total_citations = 0
matched = 0
for citation in citations_data:
    if citation.get('title') in chi_titles:
        total_citations += int(citation.get('citation_count', 0))
        matched += 1

result = {'total_citations_2020': total_citations, 'chi_papers_matched': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

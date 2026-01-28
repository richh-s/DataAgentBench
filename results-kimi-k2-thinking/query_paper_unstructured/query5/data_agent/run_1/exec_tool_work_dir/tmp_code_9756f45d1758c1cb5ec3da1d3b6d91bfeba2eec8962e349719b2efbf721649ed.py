code = """import json
import re

# Load citation data for 2020
citations_path = locals()['var_functions.query_db:0']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Load paper documents
papers_path = locals()['var_functions.query_db:2']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Map paper titles to venues
paper_venues = {}
for paper in papers_data:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Check if this is a CHI paper
    if re.search(r'CHI\s*\'?\d{2}|CHI\s+Conference|Proceedings of CHI', text, re.IGNORECASE):
        paper_venues[title] = 'CHI'

# Calculate total citations for CHI papers in 2020
total_citations = 0
for citation in citations_data:
    title = citation['title']
    if title in paper_venues and paper_venues[title] == 'CHI':
        total_citations += int(citation['citation_count'])

# Return result
print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

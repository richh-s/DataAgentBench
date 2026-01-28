code = """import json
import re

# Load citation data for 2020
citations_file = locals()['var_functions.query_db:0']
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents data
papers_file = locals()['var_functions.query_db:2']
with open(papers_file, 'r') as f:
    all_papers = json.load(f)

# Create a mapping from title to venue
chi_papers = set()
for paper in all_papers:
    title = paper['filename'].replace('.txt', '')
    text_content = paper['text']
    
    # Detect CHI conference papers from the text
    if re.search(r'CHI', text_content, re.IGNORECASE):
        chi_papers.add(title)

# Sum up citations for CHI papers
chi_total_citations = 0
for citation in citations_2020:
    paper_title = citation['title']
    if paper_title in chi_papers:
        chi_total_citations += int(citation['citation_count'])

# Print result in required format
print('__RESULT__:')
print(json.dumps(chi_total_citations))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

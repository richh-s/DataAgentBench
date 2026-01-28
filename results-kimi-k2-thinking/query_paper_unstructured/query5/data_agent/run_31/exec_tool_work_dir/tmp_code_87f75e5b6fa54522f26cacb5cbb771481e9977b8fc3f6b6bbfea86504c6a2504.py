code = """import json
import re

# Get variables with proper names
citations_data = locals()['var_functions.query_db:10']
papers_data = locals()['var_functions.query_db:5']

# Read data
with open(citations_data, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_data, 'r') as f:
    papers = json.load(f)

# Find CHI papers
chi_titles = set()
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    if not text or not filename:
        continue
    if 'CHI' in text:
        title = filename[:-4] if filename.endswith('.txt') else filename
        chi_titles.add(title)

# Sum citations
total = 0
count = 0
for cit in citations_2020:
    if cit['title'] in chi_titles:
        total += int(cit['citation_count'])
        count += 1

result = json.dumps({
    'total_citations': total,
    'chi_papers_cited': count,
    'chi_papers_found': len(chi_titles)
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

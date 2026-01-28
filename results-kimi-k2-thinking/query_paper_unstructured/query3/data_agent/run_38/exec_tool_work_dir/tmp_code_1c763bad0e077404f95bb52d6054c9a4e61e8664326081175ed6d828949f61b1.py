code = """import json
import re

# Access and load the data
paper_docs_file = locals()['var_functions.query_db:30']
citations_file = locals()['var_functions.query_db:28']

# Load the JSON data
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

# Process papers
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    has_empirical = 'empirical' in text.lower()
    
    papers_info.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Filter: empirical and after 2016
filtered_papers = [p for p in papers_info if p['has_empirical'] and p['year'] and p['year'] > 2016]

# Sum citations by title
citation_sums = {}
for cit in citations:
    title = cit['title']
    count = int(cit['total_citations'])
    citation_sums[title] = count

# Match papers with citations
results = []
for paper in filtered_papers:
    title = paper['title']
    if title in citation_sums:
        results.append({
            'title': title,
            'total_citations': citation_sums[title]
        })

# Sort and format
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)
output = [f"{item['title']}: {item['total_citations']} citations" for item in results_sorted]

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)

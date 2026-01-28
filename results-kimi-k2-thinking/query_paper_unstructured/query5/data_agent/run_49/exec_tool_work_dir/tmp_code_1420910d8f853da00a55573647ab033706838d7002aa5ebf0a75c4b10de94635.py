code = """import json
import re

# Access the file paths from storage
citations_var = 'var_functions.query_db:0'
chi_papers_var = 'var_functions.query_db:12'

citations_file = globals()[citations_var]
chi_papers_file = globals()[chi_papers_var]

# Load citation data from 2020
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load CHI papers data
with open(chi_papers_file, 'r') as f:
    chi_papers = json.load(f)

# Extract CHI paper titles (filename without .txt extension)
chi_titles = set()
for paper in chi_papers:
    filename = paper['filename']
    # Remove .txt extension
    title = filename.replace('.txt', '')
    chi_titles.add(title)

# Create a dictionary of citation data for easy lookup
citation_dict = {record['title']: int(record['citation_count']) for record in citations_2020}

# Find matching papers and sum citations
matching_papers = []
total_citations = 0

for title in chi_titles:
    if title in citation_dict:
        count = citation_dict[title]
        matching_papers.append({
            'title': title,
            'citation_count': count
        })
        total_citations += count

# Prepare result
result = {
    'total_chi_papers': len(chi_titles),
    'chi_papers_cited_in_2020': len(matching_papers),
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.execute_python:10': {'papers_cited_in_2020': 188, 'total_citation_count': 9576, 'status': 'Loaded citation data, ready to query MongoDB for CHI papers'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

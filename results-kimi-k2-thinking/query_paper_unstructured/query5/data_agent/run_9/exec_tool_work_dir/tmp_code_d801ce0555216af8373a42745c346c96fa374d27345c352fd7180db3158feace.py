code = """import json
import re

# Read the citations data (file path stored in var)
citation_file = locals()['var_functions.query_db:4']
paper_file = locals()['var_functions.query_db:6']

# Load citation data for 2020
with open(citation_file, 'r') as f:
    citations_2020 = json.load(f)

# Load paper documents
with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

# Create a list to store CHI paper titles
chi_paper_titles = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Check if this is a CHI paper
    chi_patterns = [
        r'CHI\s*\'\d{2}',
        r'CHI\s*\d{4}',
        r'Conference on Human Factors in Computing Systems',
        r'Proceedings of the .*CHI',
        r'ACM.*CHI'
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        chi_paper_titles.append(title)

# Create citation lookup dictionary
citation_dict = {}
for item in citations_2020:
    citation_dict[item['title']] = int(item['citation_count'])

# Count citations for CHI papers
total_citation_count = 0
matching_papers = []

for title in chi_paper_titles:
    if title in citation_dict:
        count = citation_dict[title]
        total_citation_count += count
        matching_papers.append({'title': title, 'citation_count': count})

result = {
    'total_citations': total_citation_count,
    'chi_papers_count': len(matching_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

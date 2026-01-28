code = """import json
import re

# Load CHI papers data
chi_papers_file_path = locals()['var_functions.execute_python:18']
with open(chi_papers_file_path, 'r') as f:
    chi_papers_data = json.load(f)

chi_papers = []
chi_titles_set = set()

# Identify CHI papers and extract titles
for doc in chi_papers_data:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    # Check for CHI venue patterns
    pattern1 = re.search(r'CHI\s*\'?\d{2}', text, re.IGNORECASE)
    pattern2 = re.search(r'CHI\s*20\d{2}', text, re.IGNORECASE)
    pattern3 = re.search(r'CHI\s+Conference', text, re.IGNORECASE)
    pattern4 = re.search(r'Proceedings of the.*?CHI', text, re.IGNORECASE)
    pattern5 = re.search(r'ACM.*?CHI', text, re.IGNORECASE)
    
    if pattern1 or pattern2 or pattern3 or pattern4 or pattern5:
        chi_papers.append(title)
        chi_titles_set.add(title)

# Load citations data
citations_file_path = "file_storage/functions.query_db:4.json"
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Calculate total citations for CHI papers in 2020
total_citations = 0
cited_chi_papers = []

for citation in citations_data:
    paper_title = citation['title']
    cite_count = int(citation['citation_count'])
    
    if paper_title in chi_titles_set:
        total_citations += cite_count
        cited_chi_papers.append(paper_title)

result = {
    'total_citations_2020': total_citations,
    'chi_papers_identified': len(chi_papers),
    'chi_papers_cited_in_2020': len(cited_chi_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:18': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

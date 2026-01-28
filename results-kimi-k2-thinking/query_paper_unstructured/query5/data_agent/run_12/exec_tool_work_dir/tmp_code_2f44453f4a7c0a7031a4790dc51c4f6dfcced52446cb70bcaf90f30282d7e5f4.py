code = """import json
import re

citations_file_path = locals()['var_functions.query_db:0']
papers_file_path = locals()['var_functions.query_db:1']

citations_data = []
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

papers_data = []
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

citation_counts = {}
for citation in citations_data:
    title = citation['title']
    count = int(citation['citation_count'])
    citation_counts[title] = count

chi_papers = []
for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    lowercase_text = text.lower()
    if 'chi' in lowercase_text:
        # Check for common CHI patterns more carefully
        if 'proceedings' in lowercase_text and 'chi' in lowercase_text:
            if re.search(r'chi\s*\d{2}|chi\s*\'\d{2}|chi\s+conference', lowercase_text):
                chi_papers.append(title)
        elif 'acm' in lowercase_text and 'chi' in lowercase_text:
            chi_papers.append(title)
            
chi_citations = {}
total_citations = 0
found_chi_papers = []

for title in chi_papers:
    if title in citation_counts:
        count = citation_counts[title]
        chi_citations[title] = count
        total_citations += count
        found_chi_papers.append(title)

print('__RESULT__:')
print(json.dumps({
    'total_chi_papers': len(found_chi_papers),
    'chi_papers_with_citations': len(chi_citations),
    'total_citation_count': total_citations,
    'chi_papers_list': found_chi_papers
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'citations_count': 188, 'papers_count': 5}}

exec(code, env_args)

code = """import json
import re
from collections import defaultdict

# Read both datasets
citations_file = locals()['var_functions.query_db:0']
papers_file = locals()['var_functions.query_db:6']

with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Extract CHI papers
chi_papers = []
for doc in paper_docs:
    text = doc.get('text', '').lower()
    filename = doc.get('filename', '')
    
    # Check if this is a CHI paper (case insensitive)
    if 'chi' in text:
        # Extract title from filename (remove .txt)
        title = re.sub(r'\.txt$', '', filename)
        chi_papers.append(title)

# Create a set for faster lookup
chi_titles = set(chi_papers)

# Match citations in 2020 with CHI papers
total_citations = 0
matched_citations = []

for citation in citations_2020:
    citation_title = citation['title']
    if citation_title in chi_titles:
        count = int(citation['citation_count'])
        total_citations += count
        matched_citations.append({
            'title': citation_title,
            'citations': count
        })

print('__RESULT__:')
print(json.dumps({
    "total_chi_citations_2020": total_citations,
    "num_chi_papers_matched": len(matched_citations),
    "sample_matches": matched_citations[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 188}, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'num_papers': 99}}

exec(code, env_args)

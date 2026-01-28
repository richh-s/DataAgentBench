code = """import json
import re
import os

# Access the stored variables properly
citations_data = locals()['var_functions.query_db:0']
papers_data = locals()['var_functions.query_db:2']

# Create a dictionary of citation counts by title
citation_counts = {}
for citation in citations_data:
    citation_counts[citation['title']] = int(citation['citation_count'])

# Process papers to find CHI papers
chi_papers = []
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Check if CHI venue is mentioned in the paper text
    if 'CHI' in text.upper():
        chi_papers.append(title)

# Match CHI papers with citations and sum counts
total_citations = 0
matched_papers = []

for paper_title in chi_papers:
    if paper_title in citation_counts:
        count = citation_counts[paper_title]
        total_citations += count
        matched_papers.append({'title': paper_title, 'citation_count': count})

# Sort matched papers by citation count (descending)
matched_papers.sort(key=lambda x: x['citation_count'], reverse=True)

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': len(matched_papers),
    'chi_papers_with_citations': matched_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

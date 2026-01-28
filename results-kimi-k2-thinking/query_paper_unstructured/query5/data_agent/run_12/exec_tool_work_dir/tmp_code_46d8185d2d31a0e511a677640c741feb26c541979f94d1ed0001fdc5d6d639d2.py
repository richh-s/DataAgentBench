code = """import json
import re

# Get the file paths from the stored variables
citations_file_path = locals()['var_functions.query_db:0']
papers_file_path = locals()['var_functions.query_db:1']

# Load the citations data
citations_data = []
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Load the paper docs data
papers_data = []
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Create a dictionary of citation counts from 2020
citation_counts = {}
for citation in citations_data:
    title = citation['title']
    count = int(citation['citation_count'])
    citation_counts[title] = count

# Process papers to find CHI papers
chi_papers = []
for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Look for CHI venue indicators in the text
    lowercase_text = text.lower()
    if 'chi' in lowercase_text:
        # Additional checks to reduce false positives
        if re.search(r'chi\s+\'\d{2}|proceedings of.*chi|acm.*chi conference', lowercase_text):
            chi_papers.append(title)
            
# Find CHI papers that have citations in 2020
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

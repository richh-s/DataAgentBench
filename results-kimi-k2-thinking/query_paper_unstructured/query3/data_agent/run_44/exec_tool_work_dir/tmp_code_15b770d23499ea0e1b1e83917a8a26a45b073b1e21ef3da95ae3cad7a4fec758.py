code = """import json
import re

citations_path = locals()['var_functions.query_db:5']
papers_path = locals()['var_functions.query_db:6']

# Load the data
with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Process papers
for paper in papers:
    # Extract title from filename
    if 'filename' in paper:
        paper['title'] = paper['filename'].replace('.txt', '')
    
    # Extract year from text
    if 'text' in paper:
        text = paper['text']
        # Look for year patterns like 20XX
        year_match = re.search(r'\b(20\d{2})\b', text)
        if year_match:
            paper['year'] = int(year_match.group(1))
        
        # Extract contribution type (look for empirical)
        contribution_match = re.search(r'empirical', text, re.IGNORECASE)
        if contribution_match:
            paper['contribution'] = ['empirical']
        else:
            paper['contribution'] = []

# Filter papers: empirical contribution and published after 2016
empirical_papers = []
for paper in papers:
    if paper.get('year') and paper['year'] > 2016:
        if 'empirical' in paper.get('contribution', []):
            empirical_papers.append(paper)

# Calculate total citations per paper
total_citations = {}
for cite in citations:
    title = cite['title']
    count = int(cite['citation_count'])
    if title not in total_citations:
        total_citations[title] = 0
    total_citations[title] += count

# Get results for empirical papers
results = []
for paper in empirical_papers:
    title = paper['title']
    citation_count = total_citations.get(title, 0)
    results.append({
        'title': title,
        'total_citation_count': citation_count
    })

# Sort by citation count (descending)
results_sorted = sorted(results, key=lambda x: x['total_citation_count'], reverse=True)

# Print results
print('__RESULT__:')
print(json.dumps(results_sorted, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'num_citations': 1405, 'num_papers': 5}}

exec(code, env_args)

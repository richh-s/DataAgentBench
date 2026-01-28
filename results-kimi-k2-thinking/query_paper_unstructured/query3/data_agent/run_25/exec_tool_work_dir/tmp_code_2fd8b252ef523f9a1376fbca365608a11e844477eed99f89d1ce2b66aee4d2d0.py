code = """import json
import re

# Load the data from stored file paths
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Process papers to extract info
paper_details = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Find year (2017+)
    year_match = re.search(r'\b(201[7-9]|202[0-9])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical contribution
    empirical = 'empirical' in text.lower()
    
    # Extract venue
    venue_match = re.search(r'(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST)', text)
    venue = venue_match.group(1) if venue_match else None
    
    # Extract source
    source_match = re.search(r'(ACM|IEEE|PubMed)', text)
    source = source_match.group(1) if source_match else None
    
    if title and year and empirical:
        paper_details.append({
            'title': title,
            'year': year,
            'venue': venue,
            'source': source
        })

# Map titles to citation counts
title_to_citations = {}
for c in citations:
    title_to_citations[c['title']] = int(c['total_citations'])

# Join and filter results
results = []
for paper in paper_details:
    citations_count = title_to_citations.get(paper['title'], 0)
    if citations_count > 0:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citations_count,
            'venue': paper['venue'],
            'source': paper['source']
        })

# Sort by citations
def get_citations(item):
    return item['total_citations']

results.sort(key=get_citations, reverse=True)

output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

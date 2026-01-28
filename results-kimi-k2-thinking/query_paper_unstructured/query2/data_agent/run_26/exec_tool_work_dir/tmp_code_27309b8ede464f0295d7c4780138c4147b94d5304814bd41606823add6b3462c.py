code = """import json
import re

# Load citations data from 2018
citations_key = 'var_functions.query_db:0'
citations_file = locals()[citations_key]
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load paper documents data
papers_key = 'var_functions.query_db:2'
papers_file = locals()[papers_key]
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Create a dictionary to store paper title -> citation count
citation_dict = {}
for item in citations_data:
    title = item['title']
    citation_count = int(item['citation_count'])
    citation_dict[title] = citation_count

# Process paper documents to find ACM papers and their citation counts
acm_citations = []
acm_titles = []

for paper in papers_data:
    # Extract title from filename
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Check if paper was published by ACM
    text = paper.get('text', '')
    
    # Look for ACM indicators in the text
    # Common patterns: ACM Copyright, ACM Classification, etc.
    acm_indicators = [
        'ACM Classification',
        'ACM Copyright',
        'Copyright © ACM',
        'Copyright 2015 © ACM',
        'Copyright 2016 © ACM',
        'Copyright 2017 © ACM',
        'Copyright 2018 © ACM',
        'Copyright 2014 © ACM',
        'Copyright 2013 © ACM',
        'ACM References',
        'Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee'
    ]
    
    is_acm = False
    for indicator in acm_indicators:
        if indicator in text:
            is_acm = True
            break
    
    # Also check for ACM copyright pattern with varying years
    if not is_acm and 'Copyright' in text and 'ACM' in text:
        # Look for copyright pattern with ACM
        if re.search(r'Copyright\s*[^\n]*ACM', text):
            is_acm = True
    
    # If it's an ACM paper and has citations in 2018, add to our list
    if is_acm and title in citation_dict:
        acm_citations.append(citation_dict[title])
        acm_titles.append(title)

# Calculate average citation count
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': len(acm_citations),
        'total_citations': sum(acm_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

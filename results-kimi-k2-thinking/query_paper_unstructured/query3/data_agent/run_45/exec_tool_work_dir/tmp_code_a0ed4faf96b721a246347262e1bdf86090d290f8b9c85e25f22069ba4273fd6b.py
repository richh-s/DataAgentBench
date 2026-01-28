code = """import json
import re
import os

# Based on the file paths shown in the output, directly load the files
# The system indicates these are the file paths
citations_file = '/tmp/tmpq8p4r5e1.json'
papers_file = '/tmp/tmp7x1o3w2y.json'

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded citations:', len(citations))
print('Loaded papers:', len(papers))

# Process papers to extract key information
paper_info = []
for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for patterns like 2015, 2016, 2017 etc
    year = None
    year_matches = re.findall(r'\b(20[012][0-9])\b', text)
    if year_matches:
        year = min(map(int, year_matches))  # Use earliest year found
    
    # Check if paper has empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Extract venue (common HCI venues)
    venue = None
    venue_patterns = re.findall(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST)', text, re.IGNORECASE)
    if venue_patterns:
        venue = venue_patterns[0].upper()
    
    paper_info.append({
        'title': title,
        'year': year,
        'venue': venue,
        'empirical': has_empirical
    })

# Filter for empirical papers after 2016
empirical_papers = [p for p in paper_info if p['empirical'] and p['year'] and p['year'] > 2016]

print('Empirical papers after 2016:', len(empirical_papers))

# Aggregate citations per paper
citation_totals = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    citation_totals[title] = citation_totals.get(title, 0) + count

# Combine paper info with citation counts
results = []
for paper in empirical_papers:
    title = paper['title']
    total_citations = citation_totals.get(title, 0)
    results.append({
        'title': title,
        'year': paper['year'],
        'venue': paper['venue'],
        'total_citations': total_citations
    })

# Sort by citation count descending  
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

print('Top 3 papers:')
for i, paper in enumerate(results_sorted[:3], 1):
    print(f"{i}. {paper['title']} ({paper['year']}, {paper['venue']}) - {paper['total_citations']} citations")

output = {'papers': results_sorted}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)

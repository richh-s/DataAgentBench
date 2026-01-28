code = """import json
import re

# Debug: check the type of citations data
citations_debug = locals()['var_functions.query_db:16']
print('Type of citations_data:', type(citations_debug))
print('First 200 chars:', str(citations_debug)[:200])

# If it's a string (file path), load it
if isinstance(citations_debug, str) and 'json' in citations_debug:
    with open(citations_debug, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_debug

# Load the paper documents data from the file
papers_file_path = locals()['var_functions.query_db:17']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Debug info
print('_Debug: Total citations:', len(citations_data))
print('_Debug: Total papers:', len(papers_data))

# Extract paper titles and domains from the documents
paper_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract domain information from text
    # Look for domain mentions in the text
    domain = None
    
    # Check if 'food' appears in the text
    if re.search(r'food\b', text, re.IGNORECASE):
        domain = 'food'
    
    if domain:
        paper_info.append({
            'title': title,
            'domain': domain
        })

# Create a dictionary mapping titles to domains for easy lookup
title_to_domain = {}
for paper in paper_info:
    title_to_domain[paper['title'].lower()] = paper['domain']

# Debug: check title mappings
print('_Debug: Papers with food domain:', len(paper_info))
for p in paper_info[:5]:
    print('_Debug:', p['title'])

# Filter citations for papers in the 'food' domain and sum citation counts
food_citation_total = 0
food_papers_count = 0
matched_titles = []

for citation in citations_data:
    citation_title = citation.get('title', '').lower()
    citation_count = int(str(citation.get('citation_count', 0)))
    
    # Check if this paper is in the food domain
    if citation_title in title_to_domain:
        domain = title_to_domain[citation_title]
        if domain == 'food':
            food_citation_total += citation_count
            food_papers_count += 1
            matched_titles.append(citation.get('title', ''))

print('__RESULT__:')
print(json.dumps({
    'total_citation_count': food_citation_total,
    'papers_in_food_domain': food_papers_count,
    'matched_paper_titles': matched_titles
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)

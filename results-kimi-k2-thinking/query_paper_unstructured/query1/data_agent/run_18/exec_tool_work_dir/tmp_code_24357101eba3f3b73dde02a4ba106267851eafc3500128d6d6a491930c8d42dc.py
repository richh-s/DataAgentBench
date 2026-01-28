code = """import json
import re

# Load the citations data (direct list from previous query)
citations_data = locals()['var_functions.query_db:16']

# Load the paper documents data from the file
papers_file_path = locals()['var_functions.query_db:17']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

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
    
    # Common domain patterns to search for
    domain_patterns = [
        r'food\b',
        r'physical activity\b',
        r'sleep\b',
        r'mental\b',
        r'finances\b',
        r'location\b',
        r'weight\b'
    ]
    
    # Check if any domain patterns appear in the text
    for pattern in domain_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            domain = pattern.replace('\\b', '')
            break
    
    if domain:
        paper_info.append({
            'title': title,
            'domain': domain
        })

# Create a dictionary mapping titles to domains for easy lookup
title_to_domain = {paper['title'].lower(): paper['domain'] for paper in paper_info}

# Filter citations for papers in the 'food' domain and sum citation counts
food_citation_total = 0
food_papers_count = 0

for citation in citations_data:
    citation_title = citation.get('title', '').lower()
    citation_count = int(citation.get('citation_count', 0))
    
    # Check if this paper is in the food domain
    if citation_title in title_to_domain:
        domain = title_to_domain[citation_title]
        if domain == 'food':
            food_citation_total += citation_count
            food_papers_count += 1

result = {
    'total_citation_count': food_citation_total,
    'papers_in_food_domain': food_papers_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)

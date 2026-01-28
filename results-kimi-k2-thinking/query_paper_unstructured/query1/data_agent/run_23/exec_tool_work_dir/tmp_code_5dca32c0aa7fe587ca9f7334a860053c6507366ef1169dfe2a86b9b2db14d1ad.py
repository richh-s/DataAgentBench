code = """import json
import re

# Load citations from the file
citations_file = locals()['var_functions.query_db:14']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load papers from the file  
papers_file = locals()['var_functions.query_db:8']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Extract paper information looking for food domain
food_papers = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if 'food' is mentioned in domain context
    has_food_domain = bool(re.search(r'\bfood\b', text, re.IGNORECASE))
    
    # Look more specifically for domain listings
    domain_section = re.search(r'(?:domains?|topics?|areas?):?\s*([\w\s,;-]+)', text, re.IGNORECASE)
    if domain_section:
        domains_text = domain_section.group(1).lower()
        if 'food' in domains_text:
            has_food_domain = True
    
    if has_food_domain:
        food_papers.append({'title': title, 'filename': filename})

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers),
    'food_domain_papers': food_papers,
    'food_papers_count': len(food_papers)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json'}

exec(code, env_args)

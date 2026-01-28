code = """import json
import re

# Load citations
with open(locals()['var_functions.query_db:14'], 'r') as f:
    citations = json.load(f)

# Load papers
with open(locals()['var_functions.query_db:8'], 'r') as f:
    papers = json.load(f)

# Extract titles and domains from papers
papers_info = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for domain mentions in the text
    # Common pattern is "domain: ..." or mentions of various domains
    # Looking for 'food' specifically
    has_food = bool(re.search(r'\bfood\b', text, re.IGNORECASE))
    
    # Also check if food is mentioned in a domains list
    domain_match = re.search(r'domain[\s:]*([^\n.]+)', text, re.IGNORECASE)
    domains = []
    if domain_match:
        domains_text = domain_match.group(1).strip()
        # Split by common separators
        domains = [d.strip().lower() for d in re.split(r'[,;\n]', domains_text)]
    
    papers_info.append({
        'title': title,
        'filename': filename,
        'has_food': has_food,
        'domains': domains,
        'id': str(paper.get('_id', ''))
    })

print('__RESULT__:')
print(json.dumps({
    'papers_analyzed': papers_info,
    'total_food_papers': len([p for p in papers_info if p['has_food'] or 'food' in p['domains']])
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json'}

exec(code, env_args)

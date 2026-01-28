code = """import json
import re

# Load all papers from the file
papers_file = locals()['var_functions.query_db:22']
with open(papers_file, 'r') as f:
    all_papers = json.load(f)

# Initialize list to track food domain papers
food_papers = []

for paper in all_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Multiple patterns to identify food domain papers
    is_food_paper = False
    
    # Pattern 1: Check if paper mentions food tracking/journals specifically
    if re.search(r'food (journal|tracking|diary|intake|consumption|logging)', text, re.IGNORECASE):
        is_food_paper = True
    
    # Pattern 2: Check if this is a food-focused study (not just mentioning food as an example)
    if re.search(r'study.*food|food.*study|track.*food|food.*track', text, re.IGNORECASE):
        is_food_paper = True
    
    # Pattern 3: Check for specific food-related terms in context
    food_context_patterns = [
        r'nutrition',
        r'dietary',
        r'eating habits',
        r'meal logging',
        r'calorie intake',
        r'food consumption',
        r'diet tracking'
    ]
    
    for pattern in food_context_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_food_paper = True
            break
    
    # Pattern 4: Check if domains include food
    # Look for domain listings in the paper metadata/introduction
    domain_indicators = re.findall(r'(?:domains?|topics?|areas?|focus):?\s*([^\n.]{0,200})', text, re.IGNORECASE)
    for domain_section in domain_indicators:
        if 'food' in domain_section.lower():
            is_food_paper = True
            break
    
    if is_food_paper:
        food_papers.append({
            'title': title,
            'filename': filename
        })

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(all_papers),
    'food_papers': food_papers,
    'food_papers_count': len(food_papers),
    'sample_paper_domains': domain_indicators[:2] if all_papers else []
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:20': {'total_papers': 5, 'food_domain_papers': [], 'food_papers_count': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

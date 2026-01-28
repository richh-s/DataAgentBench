code = """import json
import re

# Load papers
papers_file = locals()['var_functions.query_db:22']
with open(papers_file, 'r') as f:
    all_papers = json.load(f)

food_papers = []

for paper in all_papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    is_food = False
    
    # Look for food-related research
    if 'food' in text:
        # Check if it's in a research context, not just an example
        contexts = [
            'track food', 'food track',
            'food journal', 'food diary',
            'food intake', 'food consumption',
            'study of food', 'food study',
            'nutrition', 'dietary', 'eating habits',
            'meal logging', 'calorie intake'
        ]
        
        for context in contexts:
            if context in text:
                is_food = True
                break
        
        # Also check if food is in domain list
        if not is_food:
            # Look for domain listings
            domain_matches = re.findall(r'(?:domains?|topics?|areas?):\s*([^\n.]+)', text)
            for match in domain_matches:
                if 'food' in match:
                    is_food = True
                    break
    
    if is_food:
        food_papers.append({'title': title, 'filename': filename})

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(all_papers),
    'food_papers_count': len(food_papers),
    'food_papers': food_papers
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:20': {'total_papers': 5, 'food_domain_papers': [], 'food_papers_count': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

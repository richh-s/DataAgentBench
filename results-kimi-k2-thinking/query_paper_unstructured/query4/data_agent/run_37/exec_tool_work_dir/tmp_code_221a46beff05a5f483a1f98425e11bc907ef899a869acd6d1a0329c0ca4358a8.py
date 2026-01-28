code = """import json
import re

# Read the MongoDB query results from file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    papers = json.load(f)

# Process papers to extract title, year, and domain
processed_papers = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for 2016 in various patterns
    year = None
    year_match = re.search(r'\b2016\b', text)
    if year_match:
        year = 2016
    
    # Check if physical activity domain
    is_physical_activity = False
    if text:
        text_lower = text.lower()
        # Check for domain indicators
        pa_indicators = [
            'physical activity',
            'activity tracker', 
            'fitness tracker',
            'exercise',
            'steps per day',
            'step count',
            'sedentary behavior'
        ]
        
        for indicator in pa_indicators:
            if indicator in text_lower:
                is_physical_activity = True
                break
    
    if title and year == 2016 and is_physical_activity:
        processed_papers.append(title)

print('__RESULT__:')
print(json.dumps({'titles': processed_papers, 'count': len(processed_papers)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.execute_python:14': {'count': 38}, 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)

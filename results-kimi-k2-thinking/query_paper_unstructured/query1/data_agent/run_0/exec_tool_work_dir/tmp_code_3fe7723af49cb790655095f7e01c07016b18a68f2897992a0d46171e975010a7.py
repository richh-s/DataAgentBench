code = """import json
import os

# Access the MongoDB file using locals
mongo_file = locals()['var_functions.query_db:30']

# Load paper documents
with open(mongo_file, 'r') as f:
    papers = json.load(f)

print(f'Loaded {len(papers)} papers')

# Extract food domain paper titles
food_titles = set()
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'dietary', 'cuisine']

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if it's a food research paper
    for keyword in food_keywords:
        if keyword in text:
            food_titles.add(title)
            break

print(f'Found {len(food_titles)} food papers')

# Return as JSON string
result = {'food_titles': list(food_titles)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:26': {'food_paper_titles': [], 'food_paper_count': 0, 'citation_sample': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)

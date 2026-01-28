code = """import json
import os

print('=== Loading data ===')

# Load MongoDB results from file
mongo_file = var_functions_query_db_30
print('MongoDB file path:', mongo_file)

if os.path.exists(mongo_file):
    with open(mongo_file, 'r') as f:
        paper_docs = json.load(f)
    print(f'Loaded {len(paper_docs)} documents')
else:
    print('MongoDB file not found')
    paper_docs = []

# Find papers in food domain
food_papers = []
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'dietary', 'cuisine']

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '').lower()
    title = filename.replace('.txt', '')
    
    # Look for indicators of food domain research
    # Check if text mentions food in context of research domain or tracking
    for keyword in food_keywords:
        if keyword in text:
            # Additional context check to ensure it's a food research paper
            context_indicators = ['domain', 'track', 'tracking', 'self-track', 'informatic']
            if any(indicator in text for indicator in context_indicators):
                food_papers.append(title)
                break

print(f'\nFound {len(food_papers)} food domain papers')
print('Sample food papers:', food_papers[:10])

# Prepare result
result = {
    'food_paper_titles': food_papers,
    'food_paper_count': len(food_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:26': {'food_paper_titles': [], 'food_paper_count': 0, 'citation_sample': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)

code = """import json
import os

print('=== Checking available variables ===')
# Get all variables that start with var_
available = [v for v in dir() if v.startswith('var_')]
print('Available variables:', available)

# Check each variable
for var_name in available:
    var_value = eval(var_name)
    print(f'\n{var_name}:')
    print(f'  Type: {type(var_value)}')
    if isinstance(var_value, str):
        print(f'  Value (first 100 chars): {var_value[:100]}')
        # Check if it's a file path
        if os.path.exists(var_value):
            print(f'  File exists at: {var_value}')
    elif isinstance(var_value, list):
        print(f'  List length: {len(var_value)}')
        if len(var_value) > 0:
            print(f'  First item type: {type(var_value[0])}')

# Try to find the MongoDB results
mongo_file = None
if 'var_functions.query_db:2' in dir():
    temp_val = var_functions.query_db:2
    if isinstance(temp_val, str) and 'tmp' in temp_val:
        mongo_file = temp_val
        
if 'var_functions.query_db:4' in dir():
    temp_val = var_functions.query_db:4
    if isinstance(temp_val, str) and 'tmp' in temp_val:
        mongo_file = temp_val

print('\n=== MongoDB file ===')
if mongo_file and os.path.exists(mongo_file):
    print(f'Found MongoDB file: {mongo_file}')
    try:
        with open(mongo_file, 'r') as f:
            mongo_data = json.load(f)
        print(f'Loaded {len(mongo_data)} documents')
        # Extract food paper titles
        food_titles = []
        for doc in mongo_data:
            filename = doc.get('filename', '')
            title = filename.replace('.txt', '')
            # Check if it's a food paper
            text = doc.get('text', '').lower()
            if 'food' in text:
                food_titles.append(title)
        print(f'Found {len(food_titles)} food papers')
        print('Food papers sample:', food_titles[:10])
        
        # Save for next step
        result = {'food_titles': food_titles, 'count': len(food_titles)}
    except Exception as e:
        print(f'Error: {e}')
        result = None
else:
    print('MongoDB file not found')
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)

code = """import json
import os

print('Checking available variables')

# List all variables
all_vars = dir()
paper_vars = []
for v in all_vars:
    if v.startswith('var_'):
        paper_vars.append(v)

print('Available variables: ' + str(paper_vars))

# Look for MongoDB results
mongo_data = None
mongo_file = None

if 'var_functions_query_db_2' in paper_vars:
    val = var_functions_query_db_2
    if isinstance(val, str) and os.path.exists(val):
        mongo_file = val

if 'var_functions_query_db_4' in paper_vars and mongo_data is None:
    val = var_functions_query_db_4
    if isinstance(val, str) and os.path.exists(val):
        mongo_file = val

print('Mongo file path: ' + str(mongo_file))

if mongo_file and os.path.exists(mongo_file):
    print('Loading MongoDB data from file')
    with open(mongo_file, 'r') as f:
        mongo_data = json.load(f)
    print('Loaded ' + str(len(mongo_data)) + ' documents')

# Extract food paper titles
food_titles = []
if mongo_data:
    for doc in mongo_data:
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '')
        text = doc.get('text', '').lower()
        
        # Check if food-related
        if 'food' in text:
            food_titles.append(title)

print('Found ' + str(len(food_titles)) + ' food papers')

# Check citations data
citation_data = []
if 'var_functions_query_db_20' in paper_vars:
    citation_data = var_functions_query_db_20
    print('Citation data length: ' + str(len(citation_data)))

result = {
    'food_paper_titles': food_titles,
    'food_paper_count': len(food_titles),
    'citation_sample': citation_data[:3] if citation_data else []
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)

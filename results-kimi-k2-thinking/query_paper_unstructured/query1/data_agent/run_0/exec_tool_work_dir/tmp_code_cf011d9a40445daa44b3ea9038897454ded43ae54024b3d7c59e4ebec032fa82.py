code = """import json
import os

print('Checking available variables...')
# Check what variables are in the environment
all_vars = dir()
paper_vars = [v for v in all_vars if v.startswith('var_')]
print('Paper-related variables:', paper_vars)

# Check if there's a result file from the query
for var in paper_vars:
    value = eval(var)
    print(f"\n{var}: type={type(value)}")
    if isinstance(value, str) and os.path.exists(value):
        print(f"  - File path exists: {value}")
        # Try to load it
        try:
            with open(value, 'r') as f:
                data = json.load(f)
            print(f"  - JSON loaded, length: {len(data)}")
            if len(data) > 0:
                print(f"  - Sample item: {data[0].keys()}")
        except Exception as e:
            print(f"  - Error loading: {e}")
    elif isinstance(value, list):
        print(f"  - List with {len(value)} items")
        if len(value) > 0:
            print(f"  - Sample item: {value[0].keys()}")

# Also check citation data
citation_vars = [v for v in all_vars if 'citation' in v.lower() or 'Citations' in v]
print('\nCitation-related variables:', citation_vars)

for var in citation_vars:
    value = eval(var)
    print(f"\n{var}: type={type(value)}")
    if isinstance(value, list):
        print(f"  - List with {len(value)} items")
        if len(value) > 0:
            print(f"  - Sample item: {value[0]}")

print('__RESULT__:')
print(json.dumps('check_complete'))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)

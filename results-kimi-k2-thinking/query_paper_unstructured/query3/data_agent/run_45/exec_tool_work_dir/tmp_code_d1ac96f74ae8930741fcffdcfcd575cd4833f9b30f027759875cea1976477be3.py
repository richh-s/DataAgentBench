code = """# Access the stored data - it should be available as a variable
import json

# Get citations data (it should be a file path string)
if isinstance(var_functions.query_db:13, str) and '.json' in var_functions.query_db:13:
    with open(var_functions.query_db:13, 'r') as f:
        citations = json.load(f)
    print(f'Loaded {len(citations)} citations records')
else:
    citations = var_functions.query_db:13
    print(f'Citations is type {type(citations)}, length {len(citations)}')

# Get MongoDB data  
if isinstance(var_functions.query_db:12, str) and '.json' in var_functions.query_db:12:
    with open(var_functions.query_db:12, 'r') as f:
        papers = json.load(f)
    print(f'Loaded {len(papers)} paper records')
else:
    papers = var_functions.query_db:12
    print(f'Papers is type {type(papers)}, length {len(papers)}')

# Sample data
print('\nSample citations:', citations[:3])
print('\nSample papers:', papers[:1])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)

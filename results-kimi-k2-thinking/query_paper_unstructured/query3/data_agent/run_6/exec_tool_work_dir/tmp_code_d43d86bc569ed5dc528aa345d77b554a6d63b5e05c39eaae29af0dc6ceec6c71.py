code = """import json, re, os

print("Current directory files:", os.listdir('/tmp')[:10])

# Let's try to access the data correctly
# The results are stored in variables named after the tool calls
# We need to see what's available

# Try direct variable access
papers_var_name = 'var_functions.query_db:38'
citations_var_name = 'var_functions.query_db:36'

# Check what's in locals
local_vars = list(locals().keys())
print("Local variables (first 20):", local_vars[:20])

# Look for variables with query_db in name
query_vars = [v for v in local_vars if 'query_db' in v]
print("Query DB variables:", query_vars)

# Try to access them
for var_name in query_vars:
    var_value = locals()[var_name]
    print(f"{var_name}: {type(var_value)}")
    if isinstance(var_value, str) and '.json' in var_value:
        print(f"  File path: {var_value}")
        if os.path.exists(var_value):
            with open(var_value, 'r') as f:
                data = json.load(f)
            print(f"  Loaded {len(data)} records")
        else:
            print(f"  File does not exist")
    elif isinstance(var_value, list):
        print(f"  List with {len(var_value)} items")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)

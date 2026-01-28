code = """# Let's see what's actually in the stored variables
import json
import os

# Access the query result (NASDAQ Capital Market stocks)
query_result = locals()['var_functions.query_db:4']
print("Query result type:", type(query_result))
print("Query result (first 200 chars):", str(query_result)[:200])

# Access the list result (trade tables)
list_result = locals()['var_functions.list_db:8']
print("\nList result type:", type(list_result))  
print("List result (first 200 chars):", str(list_result)[:200])

# Check if these are actual file paths
if isinstance(query_result, str) and query_result.startswith('/'):
    print("\nQuery result appears to be a file path:", query_result)
    if os.path.exists(query_result):
        print("File exists, size:", os.path.getsize(query_result))
    else:
        print("File does NOT exist")

if isinstance(list_result, str) and list_result.startswith('/'):
    print("\nList result appears to be a file path:", list_result)
    if os.path.exists(list_result):
        print("File exists, size:", os.path.getsize(list_result))
    else:
        print("File does NOT exist")"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)

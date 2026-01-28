code = """import json

# Check what variables are available
available_vars = list(globals().keys())
print("Available global variables:", available_vars[:20])

# Check for the specific variable
if 'var_functions.query_db:0' in globals():
    print("Found var_functions.query_db:0")
    data = globals()['var_functions.query_db:0']
    print("Type:", type(data))
    if isinstance(data, str):
        print("String value:", data[:100])
    else:
        print("List length:", len(data))
        print("First item:", data[0] if data else "Empty")
else:
    print("var_functions.query_db:0 not found in globals")
    print("All var keys:", [k for k in globals().keys() if 'var_functions' in k])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)

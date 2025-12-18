code = """'''
import pandas as pd
import json

# Load the data from the file
with open(locals()['var_function-call-17579827535322472138'], 'r') as f:
    package_info_data = json.load(f)

df_packageinfo = pd.DataFrame(package_info_data)

# Creating a list of (System, Name, Version) tuples for the IN clause
values_list = []
for _, row in df_packageinfo.iterrows():
    # Escape single quotes in Name to prevent SQL syntax errors
    escaped_name = row['Name'].replace("'", "''")
    values_list.append(f"('{row['System']}', '{escaped_name}', '{row['Version']}')")

if values_list:
    in_clause = ", ".join(values_list)
    query_project_packageversion = f"""
    SELECT System, Name, Version, ProjectName
    FROM project_packageversion
    WHERE (System, Name, Version) IN ({in_clause})
    """
    print("__RESULT__:")
    print(json.dumps({"query": query_project_packageversion}))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "No package identifiers to query."}))
''"""

env_args = {'var_function-call-17579827535322472138': 'file_storage/function-call-17579827535322472138.json'}

exec(code, env_args)

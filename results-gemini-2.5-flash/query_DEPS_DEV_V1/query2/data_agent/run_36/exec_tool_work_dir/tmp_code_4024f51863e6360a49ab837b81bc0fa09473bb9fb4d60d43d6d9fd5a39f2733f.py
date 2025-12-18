code = """import pandas as pd
import json

with open(locals()['var_function-call-8290876752391305925'], 'r') as f:
    package_info = json.load(f)

df_package_info = pd.DataFrame(package_info)

# Prepare the WHERE IN clause for the project_packageversion table
package_versions = []
for _, row in df_package_info.iterrows():
    package_versions.append(f"('{row['Name']}', '{row['Version']}')")

# Remove duplicates to optimize the query
unique_package_versions = list(set(package_versions))

# Construct the query string
query_in_clause = ", ".join(unique_package_versions)

# If no packages are found, prevent an empty IN clause
if not query_in_clause:
    query_in_clause = "('__NONE__', '__NONE__')" # A dummy value that won't match anything


print("__RESULT__:")
print(json.dumps(query_in_clause))"""

env_args = {'var_function-call-8290876752391305925': 'file_storage/function-call-8290876752391305925.json'}

exec(code, env_args)

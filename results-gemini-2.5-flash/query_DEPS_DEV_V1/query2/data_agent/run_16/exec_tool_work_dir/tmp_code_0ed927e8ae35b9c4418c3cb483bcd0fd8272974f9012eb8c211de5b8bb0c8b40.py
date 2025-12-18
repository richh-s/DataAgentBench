code = """import pandas as pd
import json

with open(locals()['var_function-call-13362115444070003509'], 'r') as f:
    npm_packages = json.load(f)

# Convert the list of dictionaries to a DataFrame
df_npm_packages = pd.DataFrame(npm_packages)

# Remove duplicate entries for Name and Version
df_npm_packages_unique = df_npm_packages.drop_duplicates(subset=['Name', 'Version'])

# Generate SQL query for project_packageversion
# This will be a large query, so we'll construct it in parts
name_version_pairs = [f"(Name = '{row['Name'].replace("'", "''")}' AND Version = '{row['Version'].replace("'", "''")}')" for index, row in df_npm_packages_unique.iterrows()]
query_condition = " OR ".join(name_version_pairs)

# Limit the number of conditions in the WHERE clause for very large queries
# For this query, we'll process it in chunks if necessary.
# For now, let's assume the current list is manageable.
# If the query becomes too long, this part needs to be adjusted to query in chunks.

sql_query = f"SELECT Name, Version, ProjectName FROM project_packageversion WHERE System = 'NPM' AND ({query_condition})"

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-13362115444070003509': 'file_storage/function-call-13362115444070003509.json'}

exec(code, env_args)

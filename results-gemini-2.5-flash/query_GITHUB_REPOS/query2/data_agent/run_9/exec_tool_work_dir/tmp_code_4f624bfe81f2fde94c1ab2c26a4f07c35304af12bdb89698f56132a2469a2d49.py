code = """import pandas as pd

swift_repos_data = locals()['var_function-call-14350241680965922799']
swift_repo_names = [repo['repo_name'] for repo in swift_repos_data]

# Construct a WHERE clause for the repo_names
# This might exceed the SQL query limit if there are too many repos.
# For now, let's assume it's fine. If not, we'll need to split the query.
repo_names_str = ", ".join([f"'{name}'" for name in swift_repo_names])

# Now, let's query the artifacts_database for relevant files.
# We're looking for non-binary Swift files.
# The `repo_data_description` field contains information about "binary" and "copies".
# We will filter for files that are not binary and potentially have multiple copies.
# We will do the filtering in python after fetching all the data, due to `repo_data_description` being a string.

# The current approach is to retrieve all contents from artifacts_database and then filter in python
# as direct filtering on `repo_data_description` for "swift" and "non-binary" might be complex in SQL.
# Also, it's important to ensure uniqueness of files by ID.
# The question asks for "most frequently copied non-binary Swift file", which means we need to count file IDs.
# So, a single query for file IDs from contents table that are in swift_repo_names, then filter and count.

# Due to the size of swift_repos_data, fetching all content at once is not feasible.
# I need to get the file IDs first, then filter. I will first select all files in `artifacts_database.contents`
# that are non-binary, then count their occurrences.

# This will get all files. I will then filter for swift_repos in python.
# However, it is more efficient to filter by repo_name directly in the query to DuckDB.

print("__RESULT__:")
print({"repo_names": swift_repo_names})"""

env_args = {'var_function-call-14350241680965922799': 'file_storage/function-call-14350241680965922799.json'}

exec(code, env_args)

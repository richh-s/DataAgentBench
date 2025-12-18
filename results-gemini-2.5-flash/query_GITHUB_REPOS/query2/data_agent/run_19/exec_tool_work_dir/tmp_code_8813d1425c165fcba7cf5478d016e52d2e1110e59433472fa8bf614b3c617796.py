code = """import pandas as pd
import json

swift_repos_raw = json.loads(open(locals()['var_function-call-12808188931182023107'], 'r').read())
swift_repo_names = [repo['repo_name'] for repo in swift_repos_raw]

# Create a comma-separated string of repo names, each individually quoted and escaped for SQL
# Double single quotes are used to escape single quotes within a SQL string literal.
quoted_repo_names = [f"'{name.replace("'", "''")}'" for name in swift_repo_names]
repo_names_str_for_sql = ", ".join(quoted_repo_names)

# Construct the DuckDB query using standard string formatting
duckdb_query = (
    "SELECT sample_repo_name, id, COUNT(id) AS copy_count "
    "FROM contents "
    "WHERE repo_data_description NOT LIKE '%binary%' "
    f"AND sample_repo_name IN ({repo_names_str_for_sql}) "
    "GROUP BY sample_repo_name, id "
    "ORDER BY copy_count DESC "
    "LIMIT 1;"
)
print("__RESULT__:")
print(json.dumps(duckdb_query))"""

env_args = {'var_function-call-12808188931182023107': 'file_storage/function-call-12808188931182023107.json'}

exec(code, env_args)

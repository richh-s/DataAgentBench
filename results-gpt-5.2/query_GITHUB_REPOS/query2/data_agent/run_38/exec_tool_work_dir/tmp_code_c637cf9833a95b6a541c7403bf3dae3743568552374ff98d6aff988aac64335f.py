code = """import json
path = var_call_4DQLRbCkpAIx9v5CWFZjfsNG
with open(path, 'r') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]
repo_list_sql = ','.join(["'" + r.replace("'","''") + "'" for r in repo_list])

query = (
    "WITH swift_repos AS (\n"
    f"  SELECT UNNEST([{repo_list_sql}]) AS repo_name\n"
    "), swift_files AS (\n"
    "  SELECT f.repo_name, f.id\n"
    "  FROM files f\n"
    "  JOIN swift_repos r ON r.repo_name = f.repo_name\n"
    "  WHERE lower(f.path) LIKE '%.swift'\n"
    "), nonbinary AS (\n"
    "  SELECT id\n"
    "  FROM contents\n"
    "  WHERE lower(repo_data_description) NOT LIKE '%binary%'\n"
    ")\n"
    "SELECT sf.id,\n"
    "       COUNT(DISTINCT sf.repo_name) AS repo_count,\n"
    "       MIN(sf.repo_name) AS example_repo\n"
    "FROM swift_files sf\n"
    "JOIN nonbinary nb ON nb.id = sf.id\n"
    "GROUP BY sf.id\n"
    "ORDER BY repo_count DESC\n"
    "LIMIT 1;"
)

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_LMQpplzaYiVDFYkQt0pzXdjh': ['languages', 'repos', 'licenses'], 'var_call_Vurf5Xhgn2wHkPjIC3HFsuxG': ['commits', 'contents', 'files'], 'var_call_4DQLRbCkpAIx9v5CWFZjfsNG': 'file_storage/call_4DQLRbCkpAIx9v5CWFZjfsNG.json'}

exec(code, env_args)

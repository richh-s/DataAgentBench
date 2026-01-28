code = """import json, pandas as pd

path = var_call_4DQLRbCkpAIx9v5CWFZjfsNG
with open(path, 'r') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]

# Build an IN clause safely by escaping single quotes
repo_list_sql = ','.join(["'" + r.replace("'","''") + "'" for r in repo_list])

query = f"""
WITH swift_repos AS (
  SELECT UNNEST([{repo_list_sql}]) AS repo_name
), swift_files AS (
  SELECT f.repo_name, f.id
  FROM files f
  JOIN swift_repos r ON r.repo_name = f.repo_name
  WHERE lower(f.path) LIKE '%.swift'
), nonbinary AS (
  SELECT id
  FROM contents
  WHERE lower(repo_data_description) NOT LIKE '%binary%'
)
SELECT sf.id,
       COUNT(DISTINCT sf.repo_name) AS repo_count,
       MIN(sf.repo_name) AS example_repo
FROM swift_files sf
JOIN nonbinary nb ON nb.id = sf.id
GROUP BY sf.id
ORDER BY repo_count DESC
LIMIT 1;
"""

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_LMQpplzaYiVDFYkQt0pzXdjh': ['languages', 'repos', 'licenses'], 'var_call_Vurf5Xhgn2wHkPjIC3HFsuxG': ['commits', 'contents', 'files'], 'var_call_4DQLRbCkpAIx9v5CWFZjfsNG': 'file_storage/call_4DQLRbCkpAIx9v5CWFZjfsNG.json'}

exec(code, env_args)

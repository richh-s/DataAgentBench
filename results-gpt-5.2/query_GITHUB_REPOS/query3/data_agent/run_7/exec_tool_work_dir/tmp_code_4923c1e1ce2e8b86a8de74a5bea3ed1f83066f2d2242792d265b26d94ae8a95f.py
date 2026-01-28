code = """import json, pandas as pd

# Load repo list from file if needed
repo_res = var_call_IuvllIfQ3K12ghu1YxsTUHca
if isinstance(repo_res, str):
    with open(repo_res, 'r') as f:
        repo_res = json.load(f)
repos = [r['repo_name'] for r in repo_res]

# Build SQL IN clause safely by escaping single quotes
repos_escaped = ["'" + r.replace("'","''") + "'" for r in repos]

# DuckDB has a practical limit on query length; chunk the IN list
chunk_size = 5000
chunks = [repos_escaped[i:i+chunk_size] for i in range(0, len(repos_escaped), chunk_size)]

queries = []
for ch in chunks:
    in_list = ",".join(ch)
    q = f"""
    SELECT COUNT(*) AS cnt
    FROM commits
    WHERE message IS NOT NULL
      AND length(message) < 1000
      AND lower(message) NOT LIKE 'merge%'
      AND lower(message) NOT LIKE 'update%'
      AND lower(message) NOT LIKE 'test%'
      AND repo_name IN ({in_list});
    """
    queries.append(q)

out = json.dumps({"queries": queries})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_IuvllIfQ3K12ghu1YxsTUHca': 'file_storage/call_IuvllIfQ3K12ghu1YxsTUHca.json'}

exec(code, env_args)

code = """import json, pandas as pd

# Load repo list from previous result file
path = var_call_yBgoLI7vx8huym8DOYHbmPcx
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build a DuckDB-compatible IN list (escape single quotes)
repo_names_esc = [rn.replace("'", "''") for rn in repo_names]
# If empty, count is 0
if not repo_names_esc:
    out = json.dumps({"count": 0})
else:
    # Chunk to avoid too-long query strings
    chunks = []
    chunk_size = 500
    for i in range(0, len(repo_names_esc), chunk_size):
        chunk = repo_names_esc[i:i+chunk_size]
        in_list = ",".join([f"'{x}'" for x in chunk])
        chunks.append(in_list)

    # Store queries to run (as list of SQL strings)
    queries = []
    for in_list in chunks:
        q = (
            "SELECT COUNT(*) AS cnt FROM commits c "
            f"WHERE c.repo_name IN ({in_list}) "
            "AND c.message IS NOT NULL "
            "AND length(c.message) < 1000 "
            "AND lower(c.message) NOT LIKE 'merge%' "
            "AND lower(c.message) NOT LIKE 'update%' "
            "AND lower(c.message) NOT LIKE 'test%';"
        )
        queries.append(q)

    out = json.dumps({"queries": queries})

print('__RESULT__:')
print(out)"""

env_args = {'var_call_yBgoLI7vx8huym8DOYHbmPcx': 'file_storage/call_yBgoLI7vx8huym8DOYHbmPcx.json'}

exec(code, env_args)

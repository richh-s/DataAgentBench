code = """import json

p = var_call_w084PNVwsgr7OJGySoIsAbrX
with open(p, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]
repo_names_escaped = [rn.replace("'", "''") for rn in repo_names]

if not repo_names_escaped:
    out = json.dumps({"count": 0, "repo_count": 0})
    print('__RESULT__:')
    print(out)
else:
    chunk_size = 500
    clauses = []
    for i in range(0, len(repo_names_escaped), chunk_size):
        chunk = repo_names_escaped[i:i+chunk_size]
        in_list = ",".join(["'"+x+"'" for x in chunk])
        clauses.append("repo_name IN ("+in_list+")")
    where_repo = " OR ".join(["("+c+")" for c in clauses])
    query = "SELECT COUNT(*) AS cnt FROM commits WHERE message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%' AND ("+where_repo+")"
    out = json.dumps({"repo_count": len(repo_names_escaped), "duckdb_query": query})
    print('__RESULT__:')
    print(out)"""

env_args = {'var_call_w084PNVwsgr7OJGySoIsAbrX': 'file_storage/call_w084PNVwsgr7OJGySoIsAbrX.json'}

exec(code, env_args)

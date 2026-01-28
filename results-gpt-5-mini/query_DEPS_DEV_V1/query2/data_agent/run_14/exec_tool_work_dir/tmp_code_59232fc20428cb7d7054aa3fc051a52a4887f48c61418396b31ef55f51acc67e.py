code = """import json
# Read the packageinfo query result file path from storage
fp = var_call_TiqTJ2qgioCLSYHkIik7ZSys
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)
# Extract unique (System, Name, Version) triples
triples = set()
for r in data:
    triples.add((r['System'], r['Name'], r['Version']))
# Build SQL IN clause with tuples, limit number if extremely large
tuples = []
for s, n, v in triples:
    # escape single quotes
    n_esc = n.replace("'", "''")
    v_esc = v.replace("'", "''")
    s_esc = s.replace("'", "''")
    tuples.append(f"('{s_esc}','{n_esc}','{v_esc}')")
# To avoid overly long SQL, if too many tuples, truncate to first 2000
MAX_TUPLES = 2000
if len(tuples) > MAX_TUPLES:
    tuples = tuples[:MAX_TUPLES]
in_clause = ",".join(tuples)
sql = (
    "SELECT DISTINCT ppv.ProjectName, pi.Project_Information "
    "FROM project_packageversion AS ppv "
    "JOIN project_info AS pi ON pi.Project_Information LIKE '%' || ppv.ProjectName || '%' "
    f"WHERE (ppv.System, ppv.Name, ppv.Version) IN ({in_clause});"
)
import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_Tg084gBAp439zBv6nyGVDZv7': ['packageinfo'], 'var_call_JC9jizmvdS8ELnpNsf7ahvqd': ['project_info', 'project_packageversion'], 'var_call_TiqTJ2qgioCLSYHkIik7ZSys': 'file_storage/call_TiqTJ2qgioCLSYHkIik7ZSys.json'}

exec(code, env_args)

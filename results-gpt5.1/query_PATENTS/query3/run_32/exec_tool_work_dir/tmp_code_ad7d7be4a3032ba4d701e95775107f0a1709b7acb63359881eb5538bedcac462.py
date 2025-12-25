code = """import json, re, pandas as pd, os
path = var_call_FpjW3JkfXY92mTexLxFyRjkQ
with open(path) as f:
    rows = json.load(f)
assignees = []
for r in rows:
    m = re.search(r"assignee_harmonized: ([^,]+)", r.get("Patents_info",""))
    if m:
        a = m.group(1).strip()
        if a and a.upper() != "UNIV CALIFORNIA":
            assignees.append(a)
assignees = sorted(set(assignees))
result = json.dumps(assignees)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Kk9OwxZzHt7q7EX4uGFvSV8A': [], 'var_call_NrprOQv2RjHwJd2LED8LpNUs': ['cpc_definition'], 'var_call_FpjW3JkfXY92mTexLxFyRjkQ': 'file_storage/call_FpjW3JkfXY92mTexLxFyRjkQ.json'}

exec(code, env_args)

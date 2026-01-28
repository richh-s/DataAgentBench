code = """import json
p = var_call_NsFrNkBDJk2jBADn9JnQ5O8P
# p is a file path to the JSON result
with open(p, 'r') as f:
    data = json.load(f)
repo_names = [r['repo_name'] for r in data]
# Escape single quotes
def esc(s):
    return s.replace("'", "''")
in_list = ",".join("'{}'".format(esc(r)) for r in repo_names)
in_clause = f"({in_list})"
# Output the in_clause as JSON string
import json
print('__RESULT__:')
print(json.dumps(in_clause))"""

env_args = {'var_call_NsFrNkBDJk2jBADn9JnQ5O8P': 'file_storage/call_NsFrNkBDJk2jBADn9JnQ5O8P.json'}

exec(code, env_args)

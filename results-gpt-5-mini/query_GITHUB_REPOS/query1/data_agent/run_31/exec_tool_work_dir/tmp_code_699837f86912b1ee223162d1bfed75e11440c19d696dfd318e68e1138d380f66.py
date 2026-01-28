code = """import json
# var_call_o9nNR0lnbP7iyPnxPMBkLHgN contains the file path to the JSON result
path = var_call_o9nNR0lnbP7iyPnxPMBkLHgN
with open(path, 'r') as f:
    repos = json.load(f)
# Extract unique repo names
repo_list = sorted({r['repo_name'] for r in repos})
# Prepare JSON string to pass to next steps
output = json.dumps(repo_list)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_o9nNR0lnbP7iyPnxPMBkLHgN': 'file_storage/call_o9nNR0lnbP7iyPnxPMBkLHgN.json'}

exec(code, env_args)

code = """import json
# Load previous large results from storage file paths
with open(var_call_NfKgLnluRX6tzrTZCtixkVlJ, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_KsNQl0x3YG8j2u5gYKDx102k, 'r') as f:
    tables = json.load(f)

tables_set = set(tables)
# Filter symbols that are ETFs and present in trade database tables
candidates = [rec['Symbol'] for rec in stockinfo if rec.get('ETF', '').upper() == 'Y' and rec['Symbol'] in tables_set]

# Output the list as JSON string
print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_call_NfKgLnluRX6tzrTZCtixkVlJ': 'file_storage/call_NfKgLnluRX6tzrTZCtixkVlJ.json', 'var_call_KsNQl0x3YG8j2u5gYKDx102k': 'file_storage/call_KsNQl0x3YG8j2u5gYKDx102k.json'}

exec(code, env_args)

code = """import json
# Read the large results from the provided storage file paths
with open(var_call_HGxGds5f8SCXsL6NTr9BiGCQ, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_v1NFBApJOAiRiTEJJ90yq5aL, 'r') as f:
    tables = json.load(f)

# Extract symbols and company descriptions from stockinfo
stockinfo_map = {rec['Symbol']: rec.get('Company Description') for rec in stockinfo}
# Intersection with tables in stocktrade_database
symbols_in_both = [s for s in stockinfo_map.keys() if s in tables]

output = {'symbols': sorted(symbols_in_both), 'company_map': {s: stockinfo_map[s] for s in symbols_in_both}}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_HGxGds5f8SCXsL6NTr9BiGCQ': 'file_storage/call_HGxGds5f8SCXsL6NTr9BiGCQ.json', 'var_call_v1NFBApJOAiRiTEJJ90yq5aL': 'file_storage/call_v1NFBApJOAiRiTEJJ90yq5aL.json'}

exec(code, env_args)

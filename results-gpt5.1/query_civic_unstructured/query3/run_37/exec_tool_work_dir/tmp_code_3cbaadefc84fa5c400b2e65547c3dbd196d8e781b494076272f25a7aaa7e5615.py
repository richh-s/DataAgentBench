code = """import re, json, pandas as pd

# Load full funding data
path_funding = var_call_bLMWKGU1IOOAqnZ8IDf5zzuv
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Filter funding for emergency/FEMA-related projects by name keywords
pattern = re.compile(r'(emergency|fema)', re.IGNORECASE)
filtered = [row for row in funding if pattern.search(row['Project_Name'])]

result = json.dumps(filtered)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_bLMWKGU1IOOAqnZ8IDf5zzuv': 'file_storage/call_bLMWKGU1IOOAqnZ8IDf5zzuv.json', 'var_call_Bq27f8DruYBmurY1sLhdEhiO': 'file_storage/call_Bq27f8DruYBmurY1sLhdEhiO.json'}

exec(code, env_args)

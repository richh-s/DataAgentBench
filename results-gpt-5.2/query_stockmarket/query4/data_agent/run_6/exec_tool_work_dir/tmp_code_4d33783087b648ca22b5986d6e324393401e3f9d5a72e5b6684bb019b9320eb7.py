code = """import json, pandas as pd

path = var_call_FQnZeeqY6jpP92SSHDkMcZsR
with open(path, 'r') as f:
    syms = json.load(f)

df = pd.DataFrame(syms)
# extract company name as text before ' specializes'/' is '/ etc? keep full name portion before ' specializes' or ' is '
# We'll take substring before ' specializes' or ' is ' or ' offers' or ' operates' or ' provides' etc, but safest: take before first ' specializes' else before first ' is '.
import re

def clean_name(desc):
    if desc is None:
        return None
    # Sometimes description starts with company name then verb.
    m = re.split(r"\s+(specializes|is|offers|operates|provides|manufactures|develops|focuses)\b", desc, maxsplit=1)
    if len(m) > 1:
        return m[0].strip().rstrip(',')
    return desc.strip()

df['company_clean'] = df['company_name'].map(clean_name)

symbols = df['symbol'].dropna().unique().tolist()
# output as JSON list
print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'company_map': dict(zip(df['symbol'], df['company_clean']))}))"""

env_args = {'var_call_FQnZeeqY6jpP92SSHDkMcZsR': 'file_storage/call_FQnZeeqY6jpP92SSHDkMcZsR.json'}

exec(code, env_args)

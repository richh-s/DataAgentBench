code = """import json, pandas as pd, os, re

biz = var_call_Oyv4PO0Kl0k0DVkRRjMyCod7

# Convert business_ids to corresponding business_ref format
biz_ids = [b['business_id'] for b in biz]
refs = set(['businessref_' + re.sub('^businessid_', '', bid) for bid in biz_ids])

# Load full review table from file
path = var_call_lY2NTFDJBb0oz3fnPIOIhJea
with open(path, 'r') as f:
    reviews = json.load(f)

# Filter reviews for Indianapolis businesses
filtered = [r for r in reviews if r['business_ref'] in refs]

if filtered:
    df = pd.DataFrame(filtered)
    df['rating'] = pd.to_numeric(df['rating'])
    avg = df['rating'].mean()
else:
    avg = None

result = json.dumps(avg)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_NWg5UzdDt98LVSzPzsXte5ua': [], 'var_call_lY2NTFDJBb0oz3fnPIOIhJea': 'file_storage/call_lY2NTFDJBb0oz3fnPIOIhJea.json', 'var_call_R6NCyxp1aHHX7loXLKNjJs0R': ['checkin', 'business'], 'var_call_Oyv4PO0Kl0k0DVkRRjMyCod7': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)

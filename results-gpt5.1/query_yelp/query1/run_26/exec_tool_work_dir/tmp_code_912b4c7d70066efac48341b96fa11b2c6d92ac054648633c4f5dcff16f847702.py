code = """import json, pandas as pd

biz = pd.DataFrame(var_call_zMJvWIhnJRW27roGOkd1YOhO)

path = var_call_JQp1Clm9hfOYS74AcD9TSctc
with open(path, 'r') as f:
    reviews = json.load(f)
rev = pd.DataFrame(reviews)

# map business_id -> business_ref
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

merged = rev.merge(biz[['business_ref']], on='business_ref')
merged['rating'] = merged['rating'].astype(float)
avg = merged['rating'].mean()

result = json.dumps(round(avg, 4) if pd.notna(avg) else None)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_BfkfHlHPoBqbimHATvn7UgTQ': [], 'var_call_JQp1Clm9hfOYS74AcD9TSctc': 'file_storage/call_JQp1Clm9hfOYS74AcD9TSctc.json', 'var_call_zMJvWIhnJRW27roGOkd1YOhO': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)

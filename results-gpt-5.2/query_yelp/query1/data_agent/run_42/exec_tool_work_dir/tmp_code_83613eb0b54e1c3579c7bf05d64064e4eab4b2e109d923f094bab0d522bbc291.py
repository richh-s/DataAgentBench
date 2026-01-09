code = """import json
import pandas as pd

biz = pd.DataFrame(var_call_AS0T5EnkZLhU5EXvqj4WOVnf)
ids = biz['business_id'].dropna().unique().tolist()
# map businessid_X -> businessref_X
refs = [i.replace('businessid_','businessref_',1) for i in ids]
result = json.dumps({'business_refs': refs, 'n_businesses': len(refs)})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_OQqQZFUSaEFIYDNPrNQOlra7': [], 'var_call_AS0T5EnkZLhU5EXvqj4WOVnf': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)

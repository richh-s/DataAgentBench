code = """import json, pandas as pd
biz1 = pd.DataFrame(var_call_iUOEG1ETAKP8lPmXt7VMUhr5)
biz2 = pd.DataFrame(var_call_H9CWVFTuyDfJE5SObAKZ8on5)
allbiz = pd.concat([biz1,biz2], ignore_index=True).drop_duplicates()
# map businessid_x -> businessref_x
allbiz['business_ref'] = allbiz['business_id'].str.replace('businessid_', 'businessref_', regex=False)
refs = allbiz['business_ref'].dropna().unique().tolist()
print('__RESULT__:')
print(json.dumps({'business_refs': refs, 'n_businesses': len(refs)}))"""

env_args = {'var_call_iUOEG1ETAKP8lPmXt7VMUhr5': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}], 'var_call_H9CWVFTuyDfJE5SObAKZ8on5': []}

exec(code, env_args)

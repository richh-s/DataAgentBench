code = """import json
import pandas as pd

biz = pd.DataFrame(var_call_02VsxCSAlytTCJS8Dp5Dyj9y)
# map businessid_X -> businessref_X
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)
refs = biz['business_ref'].dropna().unique().tolist()

out = json.dumps({'refs': refs})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_02VsxCSAlytTCJS8Dp5Dyj9y': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)

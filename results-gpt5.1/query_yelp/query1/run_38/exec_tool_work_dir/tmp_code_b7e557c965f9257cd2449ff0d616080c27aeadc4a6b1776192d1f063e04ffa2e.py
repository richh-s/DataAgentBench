code = """import json, pandas as pd

biz_ids_records = var_call_sc67ZDE1ySsMyS9kgw6TPxPH

# convert business_ids (businessid_X) to review business_refs (businessref_X)
ids = [r['business_id'] for r in biz_ids_records]
refs = ['businessref_' + bid.split('_',1)[1] for bid in ids]

# Build a small lookup dict to filter in SQL via IN clause string
placeholders = ','.join(["'"+r+"'" for r in refs])

result = json.dumps({'business_refs_in_clause': placeholders})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_g9ZLYGTD6wAxPSzqM3YRWw1M': [], 'var_call_66hUyn5590TGca15cs5PHGGy': 'file_storage/call_66hUyn5590TGca15cs5PHGGy.json', 'var_call_sc67ZDE1ySsMyS9kgw6TPxPH': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)

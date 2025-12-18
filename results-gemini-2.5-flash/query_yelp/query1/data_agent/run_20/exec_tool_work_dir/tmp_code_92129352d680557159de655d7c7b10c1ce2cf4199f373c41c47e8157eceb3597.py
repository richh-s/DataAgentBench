code = """import pandas as pd
business_ids = [item['business_id'] for item in locals()['var_function-call-2087227944074609892']]
business_refs = [biz_id.replace('businessid_', 'businessref_') for biz_id in business_ids]
print('__RESULT__:')
print(pd.Series(business_refs).to_json(orient='records'))"""

env_args = {'var_function-call-1474791726440311094': [], 'var_function-call-2087227944074609892': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)

code = """import pandas as pd

business_ids_raw = locals()['var_function-call-17961695521575343046']
business_refs = [f"businessref_{bid['business_id'].split('_')[1]}" for bid in business_ids_raw]

print("__RESULT__:")
print(pd.Series(business_refs).to_json(orient='records'))"""

env_args = {'var_function-call-7021930956165168662': [], 'var_function-call-1143041231733152687': ['checkin', 'business'], 'var_function-call-17961695521575343046': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)

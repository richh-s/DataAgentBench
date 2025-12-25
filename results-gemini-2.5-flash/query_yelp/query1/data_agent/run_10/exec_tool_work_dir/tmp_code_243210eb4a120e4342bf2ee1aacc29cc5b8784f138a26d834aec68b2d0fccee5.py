code = """import pandas as pd

business_data = locals()['var_function-call-9405198780013962292']
business_ids = [item['business_id'].replace('businessid_', 'businessref_') for item in business_data]

print('__RESULT__:')
print(pd.Series(business_ids).to_json(orient='records'))"""

env_args = {'var_function-call-4683152080029477937': [], 'var_function-call-9405198780013962292': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)

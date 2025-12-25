code = """import pandas as pd
businesses_with_parking_info = locals()['var_function-call-3617225813010664277']['query_db_response']['results']
business_ids = [b['business_id'].replace('businessid_', 'businessref_') for b in businesses_with_parking_info]
business_ids_str = ', '.join(f"'{bid}'" for bid in business_ids)
print("__RESULT__:")
print(business_ids_str)"""

env_args = {'var_function-call-3617225813010664277': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}]}

exec(code, env_args)

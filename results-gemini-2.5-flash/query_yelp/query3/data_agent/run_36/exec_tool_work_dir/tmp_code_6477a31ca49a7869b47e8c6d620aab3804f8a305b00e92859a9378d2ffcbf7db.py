code = """import pandas as pd
import json

business_with_parking_raw = locals()['var_function-call-6581138237843065961']['query_db_response']['results'][0].strip().replace('\n', '')
business_with_parking_data = json.loads(business_with_parking_raw)
business_ids_with_parking = [item['business_id'] for item in business_with_parking_data]
business_refs_with_parking = [bid.replace('businessid_', 'businessref_') for bid in business_ids_with_parking]

__RESULT__:
print(json.dumps(business_refs_with_parking))"""

env_args = {'var_function-call-6581138237843065961': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}]}

exec(code, env_args)

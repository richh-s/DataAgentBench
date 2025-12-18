code = """import json
import pandas as pd
businesses_with_parking_raw = locals()['var_function-call-5487041508530290549']['results'][0]
businesses_with_parking = json.loads(businesses_with_parking_raw)
business_ids = [b['business_id'] for b in businesses_with_parking]
business_refs = [b.replace('businessid_', 'businessref_') for b in business_ids]
print('__RESULT__:')
print(business_refs)"""

env_args = {'var_function-call-5487041508530290549': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}]}

exec(code, env_args)

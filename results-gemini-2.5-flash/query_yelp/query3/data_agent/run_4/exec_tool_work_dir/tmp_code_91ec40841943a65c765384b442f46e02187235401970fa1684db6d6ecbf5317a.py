code = """import json
import pandas as pd

business_refs_2018 = locals()['var_function-call-11225216062189703582']
business_ids_2018 = [d['business_ref'].replace('businessref_', 'businessid_') for d in business_refs_2018]

# Prepare the filter for the MongoDB query
filter_query = {'business_id': {'$in': business_ids_2018}}

# Construct the MongoDB query string
query_string = json.dumps({
    'collection': 'business',
    'filter': filter_query,
    'projection': {'_id': 0, 'business_id': 1, 'attributes': 1}
})

print("__RESULT__:")
print(query_string)"""

env_args = {'var_function-call-11225216062189703582': [{'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_92'}]}

exec(code, env_args)

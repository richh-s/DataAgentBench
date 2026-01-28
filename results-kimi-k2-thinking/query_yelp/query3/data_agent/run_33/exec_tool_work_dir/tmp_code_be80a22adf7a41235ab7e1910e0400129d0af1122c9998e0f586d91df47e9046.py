code = """# Get the business references from the query
business_refs = var_functions.query_db:0

# Convert businessref_ to businessid_ format
business_ids = []
for ref in business_refs:
    business_ref = ref['business_ref']
    # Replace 'businessref_' with 'businessid_'
    business_id = business_ref.replace('businessref_', 'businessid_')
    business_ids.append(business_id)

# Let's also create a mapping for reference
business_mapping = {}
for ref in business_refs:
    business_ref = ref['business_ref']
    business_id = business_ref.replace('businessref_', 'businessid_')
    business_mapping[business_id] = business_ref

import json
result_dict = {
    'business_ids': business_ids,
    'business_mapping': business_mapping
}

# Print result in the required format
print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}]}

exec(code, env_args)

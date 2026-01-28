code = """import json

# Get the businesses that received reviews in 2018
reviewed_businesses = var_functions_query_0

# Debug: print the structure
print("Debug: reviewed_businesses type and sample:", type(reviewed_businesses), reviewed_businesses[:2])

# Convert business_ref to business_id format
business_ids = []
for biz in reviewed_businesses:
    business_ref = biz['business_ref']
    business_id = business_ref.replace('businessref_', 'businessid_')
    business_ids.append(business_id)

print("Debug: Number of business IDs:", len(business_ids))
print("Debug: Sample business IDs:", business_ids[:5])

# Print the result as JSON
print("__RESULT__:")
print(json.dumps({"business_ids": business_ids}))"""

env_args = {'var_functions.query_db:0': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}]}

exec(code, env_args)

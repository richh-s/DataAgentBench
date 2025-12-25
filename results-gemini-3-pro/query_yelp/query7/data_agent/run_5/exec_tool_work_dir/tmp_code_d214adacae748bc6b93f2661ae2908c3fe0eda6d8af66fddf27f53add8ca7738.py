code = """import json

# Load the SQL result
data = locals()['var_function-call-6423373186792015285']

# Extract business_ref and convert to businessid_ format
# business_ref is like "businessref_13", we need "businessid_13"
business_ids = []
for row in data:
    ref = row['business_ref']
    # replace 'ref' with 'id' in the string if it follows the pattern
    if 'businessref_' in ref:
        new_id = ref.replace('businessref_', 'businessid_')
        business_ids.append(new_id)

print("__RESULT__:")
print(json.dumps(business_ids))"""

env_args = {'var_function-call-6423373186792016074': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-6423373186792015285': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_9', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '2'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}]}

exec(code, env_args)

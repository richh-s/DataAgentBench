code = """import json

data = locals()['var_function-call-17723116888847404317']
# data is a list of dicts: {'business_ref': '...', 'review_count': ...}

business_ids = []
ref_to_count = {}

for row in data:
    ref = row['business_ref']
    count = row['review_count']
    # Convert ref to id
    # "businessref_79" -> "businessid_79"
    if ref.startswith('businessref_'):
        bid = ref.replace('businessref_', 'businessid_')
        business_ids.append(bid)
        ref_to_count[bid] = count

print("__RESULT__:")
print(json.dumps({"business_ids": business_ids, "ref_to_count": ref_to_count}))"""

env_args = {'var_function-call-3544115677963916868': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-6297594079857768035': [{'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-7818004591109711849': [{'yelping_since': '15 Jan 2009, 16:40'}], 'var_function-call-17723116888847404317': [{'business_ref': 'businessref_79', 'review_count': '4'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_44', 'review_count': '2'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '3'}, {'business_ref': 'businessref_37', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '4'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_21', 'review_count': '2'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_88', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '4'}, {'business_ref': 'businessref_82', 'review_count': '1'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '2'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '1'}, {'business_ref': 'businessref_40', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '4'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_67', 'review_count': '1'}, {'business_ref': 'businessref_9', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '1'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}]}

exec(code, env_args)

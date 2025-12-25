code = """import json
businesses = locals()['var_function-call-10703595747403902291']
res = []
for b in businesses:
    res.append(f"{b['business_id']}: {b.get('review_count')}")

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-10993106196706656500': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-10703595747403902291': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}], 'var_function-call-17102920022403647496': ['businessref_52', 'businessref_84', 'businessref_76', 'businessref_87', 'businessref_65'], 'var_function-call-12518728840551582511': [{'average_rating': '3.86046511627907'}], 'var_function-call-9150006835087032086': [], 'var_function-call-5161785089993530396': [{'avg(business_avg)': '3.977777777777778'}]}

exec(code, env_args)

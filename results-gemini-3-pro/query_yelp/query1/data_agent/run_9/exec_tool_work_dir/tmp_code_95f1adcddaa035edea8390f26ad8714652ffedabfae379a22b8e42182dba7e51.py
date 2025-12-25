code = """import json
results = locals()['var_function-call-2187998930099803768']
avg_ratings = [float(r['avg_rating']) for r in results]
final_avg = sum(avg_ratings) / len(avg_ratings)
print(f"Final Average: {final_avg}")
print("__RESULT__:")
print(json.dumps(final_avg))"""

env_args = {'var_function-call-9642591605442475710': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-16298312231672309133': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}], 'var_function-call-11591525252039133883': ['businessref_52', 'businessref_84', 'businessref_76', 'businessref_87', 'businessref_65'], 'var_function-call-13157971539831329583': [], 'var_function-call-2187998930099803768': [{'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554'}]}

exec(code, env_args)

code = """import json
records = var_call_AgJIsY1bu9f5BMKyVvGiyadd
ratings = [int(r['rating']) for r in records if r.get('rating') is not None and str(r.get('rating')).strip()!='']
if ratings:
    avg = sum(ratings)/len(ratings)
else:
    avg = None
result = {"average_rating": avg, "review_count": len(ratings)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_n2DXcLWkvEWNE33OgYrpw5qs': ['checkin', 'business'], 'var_call_m7nhZXHTO2XYksoYsIIjxkt6': ['review', 'tip', 'user'], 'var_call_AyN6VWJBoPp85SQ4rAQbC2VQ': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}], 'var_call_AgJIsY1bu9f5BMKyVvGiyadd': [{'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '3'}, {'rating': '2'}, {'rating': '4'}, {'rating': '5'}, {'rating': '3'}, {'rating': '3'}, {'rating': '5'}, {'rating': '1'}, {'rating': '3'}, {'rating': '1'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '1'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}]}

exec(code, env_args)

code = """import json
reviews = var_call_W1HkKPbuoxh3Mp70H6EZL3aW
# compute overall average across the businesses
avg_sum = 0.0
n = 0
for r in reviews:
    avg_sum += float(r['avg_rating'])
    n += 1
overall_avg = avg_sum / n if n>0 else None
out = {'top_state': 'PA', 'business_count': 8, 'average_rating_across_these_businesses': overall_avg, 'per_business': reviews}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_woj4tIn0U10exCkWbYaBd5Yf': ['checkin', 'business'], 'var_call_ijrp6giWNGCVcjhdTof3zBx6': ['review', 'tip', 'user'], 'var_call_qAmoAqh3sTe1FeETR7N45GKP': 'file_storage/call_qAmoAqh3sTe1FeETR7N45GKP.json', 'var_call_7RDsQJ4weAgqRJhZMU3kruDs': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json', 'var_call_XEkgfmj9JwPP0dFeduO2a8QB': {'path': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json'}, 'var_call_kRcVlphYJmwX9QzJFiWyAekI': {'top_state': 'PA', 'count': 8, 'business_refs': ['businessref_40', 'businessref_44', 'businessref_67', 'businessref_77', 'businessref_82', 'businessref_86', 'businessref_89', 'businessref_97']}, 'var_call_W1HkKPbuoxh3Mp70H6EZL3aW': [{'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}]}

exec(code, env_args)

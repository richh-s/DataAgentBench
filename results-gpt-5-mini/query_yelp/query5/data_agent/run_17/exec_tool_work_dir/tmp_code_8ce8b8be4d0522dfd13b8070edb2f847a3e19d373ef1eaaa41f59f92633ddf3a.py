code = """import json
# read previous results from storage variables
reviews = var_call_JQ85sruMgUCENx4HohG1XYbG
info = var_call_drGYZeIeSJsJVHtCKDLrYVyJ

# compute average of averages weighted by reviews? The question: average rating for those businesses (likely average of their avg_ratings equally weighted)
# We'll compute the simple mean of the per-business average ratings.
avg_ratings = [float(r['avg_rating']) for r in reviews]
if avg_ratings:
    overall_avg = sum(avg_ratings)/len(avg_ratings)
else:
    overall_avg = None

out = {
    'top_state': info['top_state'],
    'wifi_business_count': info['wifi_business_count'],
    'average_rating': overall_avg
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KaKUAMBmDPbvGrZNP2DEddeW': 'file_storage/call_KaKUAMBmDPbvGrZNP2DEddeW.json', 'var_call_drGYZeIeSJsJVHtCKDLrYVyJ': {'top_state': 'PA', 'wifi_business_count': 8, 'business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82']}, 'var_call_JQ85sruMgUCENx4HohG1XYbG': [{'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}]}

exec(code, env_args)

code = """import json

rl = var_call_ISZr64LiK3JXf2QusuaIJydT
# parse avg_rating as float and compute weighted or simple average? The question asks: "Which U.S. state has the highest number of businesses that offer WiFi, and what is the average rating for those businesses?"
# We'll compute the average of the per-business average ratings (simple mean across these businesses).
ratings = [float(r['avg_rating']) for r in rl]
if ratings:
    overall_avg = sum(ratings)/len(ratings)
else:
    overall_avg = None

result = {'state': var_call_Qux0hOR7O3LE2PajHqby0wba['top_state'], 'business_count': var_call_Qux0hOR7O3LE2PajHqby0wba['count'], 'average_rating': overall_avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_AVnID2AbtzsoF3Z1fKps5TMD': ['business', 'checkin'], 'var_call_vRlvrfnRNcacz2jHCK6xlI8N': ['review', 'tip', 'user'], 'var_call_iZU5oKUxuDZXG7cXh0BjQZ4L': 'file_storage/call_iZU5oKUxuDZXG7cXh0BjQZ4L.json', 'var_call_Qux0hOR7O3LE2PajHqby0wba': {'top_state': 'PA', 'business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82'], 'count': 8}, 'var_call_ISZr64LiK3JXf2QusuaIJydT': [{'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}]}

exec(code, env_args)

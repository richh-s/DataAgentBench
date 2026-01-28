code = """import json

rows = var_call_sXO4EYDrjLiHsVYjCSUdZZxK
# Convert strings to numeric types and compute weighted average across all reviews
total_reviews = 0
sum_weighted = 0.0
for r in rows:
    cnt = int(r['review_count'])
    avg = float(r['avg_rating'])
    total_reviews += cnt
    sum_weighted += avg * cnt

if total_reviews > 0:
    overall_avg = sum_weighted / total_reviews
else:
    overall_avg = None

result = {
    'state': var_call_JvJjBtIiQKntaLerjMWGloBp['top_state'],
    'wifi_business_count': var_call_JvJjBtIiQKntaLerjMWGloBp['count'],
    'average_rating_for_those_businesses': round(overall_avg, 4) if overall_avg is not None else None,
    'total_reviews_used': total_reviews
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_JRUGsLhZlnZfE5uV936pZ5Gh': ['checkin', 'business'], 'var_call_PDKzz43tZVOCr1DQNtifamwW': 'file_storage/call_PDKzz43tZVOCr1DQNtifamwW.json', 'var_call_JvJjBtIiQKntaLerjMWGloBp': {'top_state': 'PA', 'count': 8, 'business_refs': ['businessref_40', 'businessref_44', 'businessref_67', 'businessref_77', 'businessref_82', 'businessref_86', 'businessref_89', 'businessref_97']}, 'var_call_iqeda4TLZrWuXK2KhZtboLlN': ['review', 'tip', 'user'], 'var_call_Z3rq0LcnYnXoIuRHnYGq7ady': [{'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}], 'var_call_ctIEiEDwnWLuv3JpjErMFFMu': {'note': 'needs counts; please query for counts'}, 'var_call_sXO4EYDrjLiHsVYjCSUdZZxK': [{'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'review_count': '42'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392', 'review_count': '46'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609', 'review_count': '46'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823', 'review_count': '17'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04', 'review_count': '25'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476', 'review_count': '21'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809', 'review_count': '42'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474', 'review_count': '42'}]}

exec(code, env_args)

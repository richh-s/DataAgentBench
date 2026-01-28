code = """import json

# load state result
res = json.loads(var_call_pkQIPURIEnZ2UAbmKI0gOl4E)
# load review aggregates
rev = var_call_N3Q4ytw5Qco2Pugr7ThdnUMf

# compute weighted average across businesses in top state
total_reviews = 0
weighted_sum = 0.0
bus_avg = {}
for r in rev:
    br = r['business_ref']
    avg = float(r['avg_rating'])
    cnt = int(r['cnt'])
    bus_avg[br] = {'avg': avg, 'cnt': cnt}
    total_reviews += cnt
    weighted_sum += avg * cnt

if total_reviews>0:
    state_avg = weighted_sum/total_reviews
else:
    state_avg = None

output = {
    'top_state': res['top_state'],
    'business_count_with_wifi': res['count'],
    'average_rating_for_those_businesses': round(state_avg, 4) if state_avg is not None else None,
    'per_business': bus_avg
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_Ph2sjADjdgLcbK7lQLedGUrw': ['checkin', 'business'], 'var_call_LXxAdUGFtNaGYmRaX9ahBRVR': 'file_storage/call_LXxAdUGFtNaGYmRaX9ahBRVR.json', 'var_call_IZ7Xl8OO6uQmBAMPvEWebOej': 'file_storage/call_IZ7Xl8OO6uQmBAMPvEWebOej.json', 'var_call_ujs7pHQTlXU6RQF5ifNLqS2w': {'top_state': None, 'count': 0, 'business_refs': []}, 'var_call_bm10a556i5bCp1IdhOAbOqfo': 'file_storage/call_bm10a556i5bCp1IdhOAbOqfo.json', 'var_call_pkQIPURIEnZ2UAbmKI0gOl4E': {'top_state': 'PA', 'count': 8, 'business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82']}, 'var_call_3o86iocOfMTQdoDdFndGa7gf': ['review', 'tip', 'user'], 'var_call_N3Q4ytw5Qco2Pugr7ThdnUMf': [{'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476', 'cnt': '21'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809', 'cnt': '42'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609', 'cnt': '46'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823', 'cnt': '17'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474', 'cnt': '42'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'cnt': '42'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04', 'cnt': '25'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392', 'cnt': '46'}]}

exec(code, env_args)

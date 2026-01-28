code = """import json
path = var_call_1iSgJE8fijHGNgMc03OOvUzn
with open(path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Convert ratings to numeric and compute average for all reviews
ratings = []
for r in reviews:
    try:
        ratings.append(float(r.get('rating')))
    except:
        pass

import statistics, json
avg = statistics.mean(ratings) if ratings else None

res = {'average_rating': avg, 'num_reviews_considered': len(ratings)}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_YW0MNUIpy8qimuQlLtlvK3rN': ['checkin', 'business'], 'var_call_GETMSgFVgDBmQ75wBV0Y1PYD': 'file_storage/call_GETMSgFVgDBmQ75wBV0Y1PYD.json', 'var_call_naYdQG9WAYX2oOPQtnG3Gsme': {'top_state': 'PA', 'count': 8, 'business_ids': ['businessid_89', 'businessid_97', 'businessid_67', 'businessid_77', 'businessid_86', 'businessid_40', 'businessid_44', 'businessid_82']}, 'var_call_1iSgJE8fijHGNgMc03OOvUzn': 'file_storage/call_1iSgJE8fijHGNgMc03OOvUzn.json'}

exec(code, env_args)

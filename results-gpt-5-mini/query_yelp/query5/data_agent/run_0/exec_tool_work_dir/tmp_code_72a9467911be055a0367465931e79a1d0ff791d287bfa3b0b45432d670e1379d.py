code = """import json
path = var_call_ske7VE9Yow897AWMPWceGeev
with open(path,'r',encoding='utf-8') as f:
    reviews = json.load(f)
# convert ratings to ints and aggregate by business_ref
from collections import defaultdict
agg = defaultdict(list)
for r in reviews:
    br = r.get('business_ref')
    rating = r.get('rating')
    try:
        rating = int(rating)
    except:
        continue
    agg[br].append(rating)
# compute average rating per business_ref
business_avg = {br: sum(vals)/len(vals) for br,vals in agg.items()}
# load businesses with wifi and state from previous step
bizlist = json.loads(var_call_bnbXeQ5H6ZomTGDICSSp1qnG)
# map state counts and collect ratings
state_counts = {}
state_ratings = {}
for b in bizlist:
    br = b['business_ref']
    state = b['state']
    state_counts[state] = state_counts.get(state,0)+1
    if br in business_avg:
        state_ratings.setdefault(state,[]).append(business_avg[br])
# compute average rating per state (average of business averages?)
state_avg = {}
for s,vals in state_ratings.items():
    if vals:
        state_avg[s] = sum(vals)/len(vals)
# find state with max wifi businesses
if not state_counts:
    result = {"state": None}
else:
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    result = {"state": max_state, "wifi_business_count": state_counts[max_state], "average_rating": round(state_avg.get(max_state, None),2) if max_state in state_avg else None}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LUR2w8pX0VJCm0Quj5CqYIer': 'file_storage/call_LUR2w8pX0VJCm0Quj5CqYIer.json', 'var_call_bnbXeQ5H6ZomTGDICSSp1qnG': [{'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'state': 'MO'}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'state': 'FL'}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'state': 'LA'}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'state': 'IL'}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'state': 'FL'}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'state': 'PA'}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'state': 'PA'}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'state': 'PA'}, {'business_id': 'businessid_51', 'business_ref': 'businessref_51', 'state': 'FL'}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'state': 'NV'}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'state': 'FL'}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'state': 'PA'}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'state': 'PA'}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'state': 'PA'}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'state': 'PA'}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'state': 'IN'}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'state': 'FL'}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'state': 'ID'}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'state': 'PA'}, {'business_id': 'businessid_12', 'business_ref': 'businessref_12', 'state': 'AB'}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'state': 'IN'}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'state': 'MO'}], 'var_call_PMokmCHkNdfNYo3R9oOkX8n7': ['review', 'tip', 'user'], 'var_call_ske7VE9Yow897AWMPWceGeev': 'file_storage/call_ske7VE9Yow897AWMPWceGeev.json'}

exec(code, env_args)

code = """import json
# var_call_ske7VE9Yow897AWMPWceGeev is a file path containing the reviews JSON list
reviews_path = var_call_ske7VE9Yow897AWMPWceGeev
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
# bizlist variable is available directly
bizlist = var_call_bnbXeQ5H6ZomTGDICSSp1qnG
# map business_ref to state
br_to_state = {b['business_ref']: b['state'] for b in bizlist}
# count wifi businesses per state
from collections import Counter, defaultdict
state_counts = Counter()
for b in bizlist:
    state_counts[b['state']] += 1
# find state with max count (if tie, pick one with highest count arbitrarily)
if not state_counts:
    result = {"state": None, "wifi_business_count": 0, "average_rating": None}
else:
    max_state, max_count = max(state_counts.items(), key=lambda x: x[1])
    # collect all ratings for reviews whose business_ref maps to max_state
    ratings = []
    for r in reviews:
        br = r.get('business_ref')
        if br in br_to_state and br_to_state[br] == max_state:
            try:
                ratings.append(int(r.get('rating')))
            except:
                pass
    avg_rating = round(sum(ratings)/len(ratings),2) if ratings else None
    result = {"state": max_state, "wifi_business_count": max_count, "average_rating": avg_rating}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LUR2w8pX0VJCm0Quj5CqYIer': 'file_storage/call_LUR2w8pX0VJCm0Quj5CqYIer.json', 'var_call_bnbXeQ5H6ZomTGDICSSp1qnG': [{'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'state': 'MO'}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'state': 'FL'}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'state': 'LA'}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'state': 'IL'}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'state': 'FL'}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'state': 'PA'}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'state': 'PA'}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'state': 'PA'}, {'business_id': 'businessid_51', 'business_ref': 'businessref_51', 'state': 'FL'}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'state': 'NV'}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'state': 'FL'}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'state': 'PA'}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'state': 'PA'}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'state': 'PA'}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'state': 'PA'}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'state': 'IN'}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'state': 'FL'}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'state': 'ID'}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'state': 'PA'}, {'business_id': 'businessid_12', 'business_ref': 'businessref_12', 'state': 'AB'}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'state': 'IN'}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'state': 'MO'}], 'var_call_PMokmCHkNdfNYo3R9oOkX8n7': ['review', 'tip', 'user'], 'var_call_ske7VE9Yow897AWMPWceGeev': 'file_storage/call_ske7VE9Yow897AWMPWceGeev.json'}

exec(code, env_args)

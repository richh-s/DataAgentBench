code = """import json
import pandas as pd

biz_records = var_call_btUpLhgb7yBiTkyDHYvEuigy
review_path = var_call_ZSSM0vvH8ADvqhVLRPTGMJrP

# Load all reviews
with open(review_path, 'r') as f:
    review_records = json.load(f)

# Convert business_ids to corresponding business_refs
biz_ids = [r['business_id'] for r in biz_records]
ref_map = {bid: 'businessref_' + bid.split('_', 1)[1] for bid in biz_ids}
valid_refs = set(ref_map.values())

# Filter reviews for these business_refs
ratings = [int(r['rating']) for r in review_records if r['business_ref'] in valid_refs]

avg_rating = sum(ratings) / len(ratings) if ratings else None

result = json.dumps(avg_rating)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_mbSr0xuuQRcgzr1ExMHqKnKw': [], 'var_call_ZSSM0vvH8ADvqhVLRPTGMJrP': 'file_storage/call_ZSSM0vvH8ADvqhVLRPTGMJrP.json', 'var_call_eEOizyBLGcqftFyGv1nwVQI4': ['checkin', 'business'], 'var_call_btUpLhgb7yBiTkyDHYvEuigy': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)

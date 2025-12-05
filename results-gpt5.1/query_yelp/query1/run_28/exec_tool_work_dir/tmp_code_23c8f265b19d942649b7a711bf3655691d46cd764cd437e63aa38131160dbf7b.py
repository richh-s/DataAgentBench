code = """import json, pandas as pd, os

biz_ids_records = var_call_JyVolma8zIa0axSna4Jm8Nk7

def convert_businessid_to_ref(bid):
    # businessid_52 -> businessref_52
    return bid.replace('businessid_', 'businessref_')

biz_ids = [convert_businessid_to_ref(r['business_id']) for r in biz_ids_records]

# read full review table from file
file_path = var_call_6XGmPJQMNIhvTIrfbr6JQ7BL
with open(file_path, 'r') as f:
    reviews = json.load(f)

# filter reviews for those business_refs
biz_set = set(biz_ids)
filtered = [r for r in reviews if r['business_ref'] in biz_set]

if not filtered:
    avg_rating = None
else:
    ratings = [float(r['rating']) for r in filtered]
    avg_rating = sum(ratings) / len(ratings)

result = json.dumps({'average_rating_indianapolis': avg_rating, 'business_refs': biz_ids})

print('__RESULT__:')
print(result)"""

env_args = {'var_call_6HaYJjaY9hRRLF1Sb5avB58P': [], 'var_call_6XGmPJQMNIhvTIrfbr6JQ7BL': 'file_storage/call_6XGmPJQMNIhvTIrfbr6JQ7BL.json', 'var_call_U79RKl8ZS3hutopeKLCjAgbd': ['checkin', 'business'], 'var_call_JyVolma8zIa0axSna4Jm8Nk7': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)

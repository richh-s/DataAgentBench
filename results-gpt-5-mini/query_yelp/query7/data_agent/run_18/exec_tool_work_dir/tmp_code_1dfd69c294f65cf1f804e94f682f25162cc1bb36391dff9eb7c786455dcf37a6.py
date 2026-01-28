code = """import json
# var_call_OyZAvKqaeA0cak02EIPNVXVZ is available from previous query
rows = var_call_OyZAvKqaeA0cak02EIPNVXVZ
# Extract unique numeric suffixes and map to businessid_
business_ids = []
for r in rows:
    ref = r.get('business_ref')
    if ref and ref.startswith('businessref_'):
        suffix = ref.split('_', 1)[1]
        bid = 'businessid_' + suffix
        business_ids.append(bid)
# Build the Mongo query dict
query_dict = {
    "collection": "business",
    "filter": {"business_id": {"$in": business_ids}},
    "projection": {"business_id": 1, "name": 1, "description": 1, "categories": 1},
    "limit": 1000
}
query_str = json.dumps(query_dict)
print("__RESULT__:")
print(query_str)"""

env_args = {'var_call_tVS7x3aoQ7nYhfziTVSmNTJ2': ['business', 'checkin'], 'var_call_GKO7iyfChH297dktylUcjbwM': ['review', 'tip', 'user'], 'var_call_fXQpYhlrwqdOyB4ixgrWCUVX': 'file_storage/call_fXQpYhlrwqdOyB4ixgrWCUVX.json', 'var_call_OyZAvKqaeA0cak02EIPNVXVZ': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}]}

exec(code, env_args)

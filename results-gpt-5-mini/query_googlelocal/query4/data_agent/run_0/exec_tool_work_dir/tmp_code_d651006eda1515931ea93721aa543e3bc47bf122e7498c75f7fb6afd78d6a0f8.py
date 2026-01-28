code = """import json
# data from previous query_db calls
data_counts = var_call_MbyrRQhcNFPCOtIUuJHp8bq1
data_names = var_call_tcQ9P8NZRsYCzeBdhvuZQPwR
# build mapping gmap_id -> name
name_map = {rec['gmap_id']: rec['name'] for rec in data_names}
# combine
combined = []
for rec in data_counts:
    gid = rec['gmap_id']
    count = int(rec['high_count'])
    combined.append({'name': name_map.get(gid, gid), 'high_rating_review_count_2019': count})
# ensure sorted by count desc
combined = sorted(combined, key=lambda x: x['high_rating_review_count_2019'], reverse=True)
result_json = json.dumps(combined)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_MbyrRQhcNFPCOtIUuJHp8bq1': [{'gmap_id': 'gmap_20', 'high_count': '8'}, {'gmap_id': 'gmap_53', 'high_count': '7'}, {'gmap_id': 'gmap_40', 'high_count': '6'}], 'var_call_tcQ9P8NZRsYCzeBdhvuZQPwR': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)

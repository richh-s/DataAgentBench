code = """import json

tracks = var_call_ota19o1ydf5Mr84WNCr2ItM6
sales = var_call_VkALhUdvwhmxM8EMjUeBeYML

# All these track variants clearly refer to the same real-world song "Street Hype" by Brucqe/Bruce Maginnis.
# Aggregate revenue by store across all these track_ids.

from collections import defaultdict
store_revenue = defaultdict(float)

for row in sales:
    store_revenue[row['store']] += float(row['total_revenue'])

# Find store with max revenue
best_store = max(store_revenue.items(), key=lambda x: x[1])
result = {"store": best_store[0], "total_revenue_usd": round(best_store[1], 2)}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_X7JIoH5kuBYpHPfq0bIzM1nf': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_ota19o1ydf5Mr84WNCr2ItM6': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_VkALhUdvwhmxM8EMjUeBeYML': [{'track_id': '4122', 'store': 'Amazon Music', 'total_revenue': '304.13'}, {'track_id': '13758', 'store': 'Apple Music', 'total_revenue': '477.06'}, {'track_id': '14080', 'store': 'Apple Music', 'total_revenue': '68.68'}, {'track_id': '4628', 'store': 'iTunes', 'total_revenue': '505.61'}, {'track_id': '13758', 'store': 'Google Play', 'total_revenue': '51.4'}, {'track_id': '4122', 'store': 'Apple Music', 'total_revenue': '47.52'}, {'track_id': '13758', 'store': 'Amazon Music', 'total_revenue': '378.1'}, {'track_id': '13758', 'store': 'iTunes', 'total_revenue': '148.95'}]}

exec(code, env_args)

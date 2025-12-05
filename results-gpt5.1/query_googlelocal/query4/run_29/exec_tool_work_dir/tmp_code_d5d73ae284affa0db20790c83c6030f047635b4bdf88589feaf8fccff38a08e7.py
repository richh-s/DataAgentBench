code = """import json

reviews = var_call_LhcbyPn8mlsqGQur2iz6uuxi
businesses = var_call_3mpLQd2nZkJg0qWaYkPViY49

# Convert high_review_count to int and index by gmap_id
count_map = {r['gmap_id']: int(r['high_review_count']) for r in reviews}

result = []
for b in businesses:
    gmap_id = b['gmap_id']
    result.append({
        'business_name': b['name'],
        'gmap_id': gmap_id,
        'high_rating_review_count_2019': count_map.get(gmap_id, 0)
    })

# Sort by count desc just to be safe
result_sorted = sorted(result, key=lambda x: x['high_rating_review_count_2019'], reverse=True)

output = json.dumps(result_sorted, ensure_ascii=False)

print("__RESULT__:")
print(output)"""

env_args = {'var_call_LhcbyPn8mlsqGQur2iz6uuxi': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_2L0F2Mh7mqbQyPl18CURTXuk': ['business_description'], 'var_call_3mpLQd2nZkJg0qWaYkPViY49': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)

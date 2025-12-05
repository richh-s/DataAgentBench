code = """import json
reviews = var_call_yERsXBMKQeUfiyIFrvBNzQ7s
businesses = var_call_baZ6LXHF9LBHMDlYJrWA74vm
# join on gmap_id
joined = []
for r in reviews:
    for b in businesses:
        if r['gmap_id'] == b['gmap_id']:
            joined.append({'business_name': b['name'], 'high_rating_review_count': int(r['high_review_count'])})
result = json.dumps(joined)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_yERsXBMKQeUfiyIFrvBNzQ7s': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_zDfbENDSTU6r1nMregfEEqnq': ['business_description'], 'var_call_baZ6LXHF9LBHMDlYJrWA74vm': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)

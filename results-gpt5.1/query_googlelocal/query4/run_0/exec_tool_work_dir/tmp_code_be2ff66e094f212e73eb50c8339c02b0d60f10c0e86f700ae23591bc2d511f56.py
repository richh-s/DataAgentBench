code = """import json
reviews = var_call_ZVsHfYQYYyvepElW0Y9jHFF5
businesses = var_call_ImQrY6D14to4eHlxFP4aMJEl

# convert review counts to int and merge on gmap_id
rev_map = {r['gmap_id']: int(r['high_review_count']) for r in reviews}
result = []
for b in businesses:
    g = b['gmap_id']
    result.append({'business_name': b['name'], 'high_rating_review_count_2019': rev_map.get(g, 0)})

# sort by count desc just in case
result_sorted = sorted(result, key=lambda x: x['high_rating_review_count_2019'], reverse=True)

out = json.dumps(result_sorted)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ZVsHfYQYYyvepElW0Y9jHFF5': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_5jZllgHV2c4IzJ6ajRaJXvqz': ['business_description'], 'var_call_ImQrY6D14to4eHlxFP4aMJEl': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)

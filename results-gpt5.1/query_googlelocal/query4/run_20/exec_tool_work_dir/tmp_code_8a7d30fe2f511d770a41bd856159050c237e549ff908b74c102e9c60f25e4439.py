code = """import json
high_ratings = var_call_EXppt79HoJp8iO7y0ldEZp9e
names = var_call_j85xLRFDS8qMuwPJ8fLhDyrG
name_map = {b['gmap_id']: b['name'] for b in names}
result = []
for r in high_ratings:
    result.append({
        'business_name': name_map.get(r['gmap_id'], r['gmap_id']),
        'high_rating_review_count_2019': int(r['high_rating_reviews'])
    })
out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_EXppt79HoJp8iO7y0ldEZp9e': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_call_X6NR3I4CiXLmjeQesPTxYcMi': ['business_description'], 'var_call_j85xLRFDS8qMuwPJ8fLhDyrG': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)

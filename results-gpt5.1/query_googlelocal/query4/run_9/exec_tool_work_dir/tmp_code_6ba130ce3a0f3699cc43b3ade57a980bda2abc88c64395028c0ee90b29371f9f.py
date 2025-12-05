code = """import json
reviews = var_call_4KkSlrjn7LE2I0QpYYNtBbXl
businesses = var_call_DtkuiLco80bLPMhOcaHnSp57
name_map = {b['gmap_id']: b['name'] for b in businesses}
result = []
for r in reviews:
    result.append({
        'business_name': name_map.get(r['gmap_id'], ''),
        'high_rating_review_count': int(r['high_review_count'])
    })
output = json.dumps(result)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_4KkSlrjn7LE2I0QpYYNtBbXl': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_aJvZ0WNmNtDbPFVRIQFW9mUz': ['business_description'], 'var_call_DtkuiLco80bLPMhOcaHnSp57': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)

code = """import json

reviews = var_call_wtRYPI7HywvGuCERd012l926
businesses = var_call_riyBDxyzK4hekz9NsC0TzX2A

biz_map = {b['gmap_id']: b['name'] for b in businesses}

result = []
for r in reviews:
    g = r['gmap_id']
    result.append({
        'business_name': biz_map.get(g, ''),
        'gmap_id': g,
        'high_rating_review_count': int(r['high_review_count'])
    })

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_wtRYPI7HywvGuCERd012l926': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_tipHFIibI3oRqIYXz1F0hAO4': ['business_description'], 'var_call_riyBDxyzK4hekz9NsC0TzX2A': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)

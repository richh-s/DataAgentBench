code = """import json
reviews = var_call_DQ0W6Yxx4IYVa3Xqx9SwFL04
businesses = var_call_WKulgG7QXaY3IgFuT5pQhauG

biz_map = {b['gmap_id']: b['name'] for b in businesses}
results = []
for r in reviews:
    g = r['gmap_id']
    results.append({
        'business_name': biz_map.get(g, ''),
        'gmap_id': g,
        'high_rating_review_count': int(r['high_review_count'])
    })

out = json.dumps(results)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_DQ0W6Yxx4IYVa3Xqx9SwFL04': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_coh10HcI2IGgmw1p2kbOoKhh': ['business_description'], 'var_call_WKulgG7QXaY3IgFuT5pQhauG': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)

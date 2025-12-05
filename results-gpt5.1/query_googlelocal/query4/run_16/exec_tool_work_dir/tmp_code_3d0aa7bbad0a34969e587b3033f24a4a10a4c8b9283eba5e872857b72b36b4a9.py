code = """import json
rev_data = var_call_WCucRFUMJpMeLA6PKPjxJmZx
biz_data = var_call_zlnlzVdmpkSYIC4bALQRdljW

biz_map = {b['gmap_id']: b['name'] for b in biz_data}

results = []
for r in rev_data:
    results.append({
        'business_name': biz_map.get(r['gmap_id'], r['gmap_id']),
        'high_rating_review_count': int(r['high_review_count'])
    })

result_json = json.dumps(results)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_WCucRFUMJpMeLA6PKPjxJmZx': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_0xn8YsrREWRlMFYgPLAfuQY2': ['business_description'], 'var_call_zlnlzVdmpkSYIC4bALQRdljW': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)

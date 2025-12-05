code = """import json

reviews = var_call_RfcBDMhaD2KpxdcQYbqxDugA
businesses = var_call_UdVMtYnaosTPXvJ5NGCm8QAV

biz_map = {b['gmap_id']: b['name'] for b in businesses}

result = []
for r in reviews:
    gmap_id = r['gmap_id']
    result.append({
        'business_name': biz_map.get(gmap_id, None),
        'gmap_id': gmap_id,
        'high_rating_review_count_2019': int(r['high_review_count'])
    })

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_RfcBDMhaD2KpxdcQYbqxDugA': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_taJIRQ6KTnW5Y34xerEFl0Kx': ['business_description'], 'var_call_UdVMtYnaosTPXvJ5NGCm8QAV': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)

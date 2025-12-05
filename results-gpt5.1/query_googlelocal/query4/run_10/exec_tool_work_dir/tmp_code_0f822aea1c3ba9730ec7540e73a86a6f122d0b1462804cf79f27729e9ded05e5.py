code = """import json
reviews = var_call_5YXsVIrFEZnfpBcGAjmde6X6
businesses = var_call_ddhRTumgmlU6eaSqCx2rQ322

# Map gmap_id to business name
id_to_name = {b['gmap_id']: b['name'] for b in businesses}

result = []
for r in reviews:
    gmap_id = r['gmap_id']
    result.append({
        'business_name': id_to_name.get(gmap_id, ''),
        'high_rating_review_count_2019': int(r['high_rating_count'])
    })

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_5YXsVIrFEZnfpBcGAjmde6X6': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}], 'var_call_n7i6gNtGT0j0mUsdIEn1vScB': ['business_description'], 'var_call_ddhRTumgmlU6eaSqCx2rQ322': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)

code = """import json

reviews = var_call_Ypcv6s21mlD9JYlVOhmGaAJx
businesses = var_call_TCoSx4xB2JaoCXpMuKTarFCm

biz_map = {b['gmap_id']: b['name'] for b in businesses}

result = []
for r in reviews:
    g = r['gmap_id']
    result.append({
        'business_name': biz_map.get(g, ''),
        'gmap_id': g,
        'high_rating_reviews_2019': int(r['high_rating_reviews'])
    })

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_Ypcv6s21mlD9JYlVOhmGaAJx': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_call_Rw6cQgQz9jir8bk4V0T8aG0A': ['business_description'], 'var_call_TCoSx4xB2JaoCXpMuKTarFCm': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)

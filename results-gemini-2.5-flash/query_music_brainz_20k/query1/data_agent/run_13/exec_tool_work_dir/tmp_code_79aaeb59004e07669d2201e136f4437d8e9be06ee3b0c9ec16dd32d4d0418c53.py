code = """import json

sales_data_str = locals()['var_function-call-8187558277852055998']['results'][0]
sales_data_list = json.loads(sales_data_str)
total_revenue = sum(float(sale['revenue_usd']) for sale in sales_data_list)

print('__RESULT__:')
print(json.dumps(total_revenue))"""

env_args = {'var_function-call-17568083950287885317': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}], 'var_function-call-8187558277852055998': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)

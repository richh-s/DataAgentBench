code = """import json

sales_data = locals()['var_function-call-7991456799067059916']
revenue = sales_data[0]['sum(revenue_usd)']

print("__RESULT__:")
print(json.dumps(revenue))"""

env_args = {'var_function-call-5550198362541354546': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}], 'var_function-call-8040066199163737438': ['4233', '12954'], 'var_function-call-7991456799067059916': [{'sum(revenue_usd)': '601.44'}]}

exec(code, env_args)

code = """import json
total_revenue = sum(float(item['revenue_usd']) for item in locals()['var_function-call-896087882458194953'])
print("__RESULT__:")
print(json.dumps(total_revenue))"""

env_args = {'var_function-call-11405576129785991393': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}], 'var_function-call-896087882458194953': [{'revenue_usd': '377.62'}, {'revenue_usd': '223.82'}]}

exec(code, env_args)

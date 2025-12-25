code = """total_revenue = float(locals()['var_function-call-2447849554389999421'][0]['revenue_usd']) + float(locals()['var_function-call-2447849554389999421'][1]['revenue_usd'])
print('__RESULT__:')
print(str(total_revenue))"""

env_args = {'var_function-call-18053992417469995005': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}], 'var_function-call-2447849554389999421': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)

code = """import json
import pandas as pd

tracks = var_call_EgUgdWmHUSEZs5oke5ODvNuP
sales = var_call_3SBI4uCRmIKBo20STu1PfpWE

# Collect track_ids from tracks results
track_ids = set([str(r['track_id']) for r in tracks])

# Sum revenue for those track_ids from sales results
total = 0.0
for r in sales:
    if str(r.get('track_id')) in track_ids:
        try:
            total += float(r.get('revenue_usd_sum', 0))
        except:
            total += 0.0

# Round to 2 decimal places
total = round(total, 2)

output = {'total_revenue_usd': total}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_EgUgdWmHUSEZs5oke5ODvNuP': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_3SBI4uCRmIKBo20STu1PfpWE': [{'track_id': '4233', 'revenue_usd_sum': '377.62'}, {'track_id': '12954', 'revenue_usd_sum': '223.82'}]}

exec(code, env_args)

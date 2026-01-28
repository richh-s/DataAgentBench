code = """import json
import pandas as pd

# Load data from previous tool calls
tracks = pd.DataFrame(var_call_JXdcaY7NINjb5qoxY8T817iR)
sales = pd.DataFrame(var_call_mi3UXgXX7po1W9mJd8XU99sf)

# Ensure proper types
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

# Sum revenue for the relevant track_ids (these were the ones returned from sales query)
total_revenue = sales['revenue_usd'].sum()

result = {
    'total_revenue_usd': round(float(total_revenue), 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'track_title': 'Get Me Bodied',
    'artist': 'Beyoncé',
    'component_track_ids_included': sales['track_id'].tolist()
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JXdcaY7NINjb5qoxY8T817iR': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '5281', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_mi3UXgXX7po1W9mJd8XU99sf': [{'track_id': '5281', 'revenue_usd': '458.02'}, {'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)

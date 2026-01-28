code = """import pandas as pd
import json

result = [{"track_id": "4233", "store": "Apple Music", "country": "Canada", "revenue": "377.62"}, {"track_id": "12954", "store": "Apple Music", "country": "Canada", "revenue": "223.82"}]

# Create a dataframe
df = pd.DataFrame(result)

# Convert revenue to numeric, handling any non-numeric values
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

# Sum the revenues

# Check if we have any valid numeric data
valid_revenues = df['revenue'].dropna()

if valid_revenues.empty:
    total_revenue = 0.0
else:
    total_revenue = valid_revenues.sum()

# Format and print the result
print('__RESULT__:')
print(json.dumps(total_revenue))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_functions.query_db:5': [{'total_revenue': 'nan'}], 'var_functions.query_db:6': [], 'var_functions.query_db:10': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_functions.list_db:12': ['sales'], 'var_functions.query_db:14': [{'track_id': '4233', 'store': 'Apple Music', 'country': 'Canada', 'revenue': '377.62'}, {'track_id': '12954', 'store': 'Apple Music', 'country': 'Canada', 'revenue': '223.82'}]}

exec(code, env_args)

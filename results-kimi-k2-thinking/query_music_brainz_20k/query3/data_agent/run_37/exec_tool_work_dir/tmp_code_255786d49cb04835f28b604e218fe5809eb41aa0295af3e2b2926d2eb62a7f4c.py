code = """import json
import pandas as pd

# Read sales data
with open(locals()['var_functions.query_db:6'], 'r') as f:
    sales_data = json.load(f)

# Create DataFrame
sales_df = pd.DataFrame(sales_data)

# Convert total_revenue to float and find max
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
max_revenue = sales_df['total_revenue'].max()
max_row = sales_df[sales_df['total_revenue'] == max_revenue].iloc[0]

print('__RESULT__:')
print(json.dumps({
    'track_id': str(max_row['track_id']),
    'total_revenue': float(max_revenue),
    'all_max_revenues': sales_df[sales_df['total_revenue'] == max_revenue].to_dict('records')
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'max_track_id': '17096', 'total_revenue': 999.8799999999999, 'track_info': {'title': 'Vinger Alleen (feat. Adriaan Brand) - Die Heuwels Fantasties', 'artist': 'Heuwels Fantasties', 'album': 'None', 'year': "'09"}}, 'var_functions.execute_python:12': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'total_revenue': 2522.82}, 'var_functions.execute_python:14': [{'track_id': '14719', 'total_revenue': 2522.82}, {'track_id': '5124', 'total_revenue': 2503.19}, {'track_id': '1344', 'total_revenue': 2500.72}, {'track_id': '6725', 'total_revenue': 2489.81}, {'track_id': '10377', 'total_revenue': 2466.71}, {'track_id': '5050', 'total_revenue': 2466.31}, {'track_id': '6667', 'total_revenue': 2452.7}, {'track_id': '7245', 'total_revenue': 2436.97}, {'track_id': '11641', 'total_revenue': 2428.22}, {'track_id': '964', 'total_revenue': 2425.61}], 'var_functions.execute_python:16': [{'track_id': '17096', 'total_revenue': '999.8799999999999'}, {'track_id': '13202', 'total_revenue': '999.75'}, {'track_id': '909', 'total_revenue': '999.73'}]}

exec(code, env_args)

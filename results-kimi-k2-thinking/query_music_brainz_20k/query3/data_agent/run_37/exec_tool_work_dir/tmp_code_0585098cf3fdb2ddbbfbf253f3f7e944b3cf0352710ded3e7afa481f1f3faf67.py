code = """import json
import pandas as pd

# Read sales data
with open(locals()['var_functions.query_db:6'], 'r') as f:
    sales_data = json.load(f)

# Create DataFrame and sort by revenue
sales_df = pd.DataFrame(sales_data)
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
top_10 = sales_df.sort_values('total_revenue', ascending=False).head(10)

print('__RESULT__:')
print(top_10.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'max_track_id': '17096', 'total_revenue': 999.8799999999999, 'track_info': {'title': 'Vinger Alleen (feat. Adriaan Brand) - Die Heuwels Fantasties', 'artist': 'Heuwels Fantasties', 'album': 'None', 'year': "'09"}}, 'var_functions.execute_python:12': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'total_revenue': 2522.82}}

exec(code, env_args)

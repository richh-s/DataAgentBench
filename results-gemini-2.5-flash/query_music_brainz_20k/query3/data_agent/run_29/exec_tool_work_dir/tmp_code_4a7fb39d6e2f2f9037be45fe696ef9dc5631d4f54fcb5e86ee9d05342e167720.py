code = """import pandas as pd
import json

# Load the full sales data from the file
with open(locals()['var_function-call-15600833846576879828'], 'r') as f:
    sales_data = json.load(f)

sales_df = pd.DataFrame(sales_data)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Group by track_id and sum revenue
total_revenue_per_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()

# Find the track_id with the highest total revenue
highest_revenue_track_id = total_revenue_per_track.loc[total_revenue_per_track['revenue_usd'].idxmax()]

print('__RESULT__:')
print(highest_revenue_track_id.to_json())"""

env_args = {'var_function-call-15600833846576879828': 'file_storage/function-call-15600833846576879828.json'}

exec(code, env_args)

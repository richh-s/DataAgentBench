code = """import pandas as pd
with open(locals()['var_function-call-6184612043248133134'], 'r') as f:
    sales_data = pd.read_json(f)

# Convert revenue_usd to numeric, handling potential non-numeric values
sales_data['revenue_usd'] = pd.to_numeric(sales_data['revenue_usd'], errors='coerce')

# Group by track_id and sum the revenue
total_revenue_per_track = sales_data.groupby('track_id')['revenue_usd'].sum().reset_index()

# Find the track with the highest total revenue
highest_revenue_track = total_revenue_per_track.loc[total_revenue_per_track['revenue_usd'].idxmax()]

print("__RESULT__:")
print(highest_revenue_track.to_json())"""

env_args = {'var_function-call-6184612043248133134': 'file_storage/function-call-6184612043248133134.json'}

exec(code, env_args)

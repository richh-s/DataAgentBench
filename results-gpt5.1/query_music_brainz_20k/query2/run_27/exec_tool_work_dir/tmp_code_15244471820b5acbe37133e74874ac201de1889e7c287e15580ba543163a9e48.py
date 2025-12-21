code = """import json, pandas as pd

# Load full sales data from file path in var_call_4l5NTMIyeG3EooPsnIJr4E4P
with open(var_call_4l5NTMIyeG3EooPsnIJr4E4P, 'r') as f:
    sales_data = json.load(f)

sales_df = pd.DataFrame(sales_data)

# Identify the track_id for 'Street Hype' by Brucqe Maginnis
track_row = pd.DataFrame(var_call_Tflv7tytw7CQLrodoSmmMpQq).iloc[0]
street_hype_track_id = track_row['track_id']

# Filter sales for this track_id
track_sales = sales_df[sales_df['track_id'] == street_hype_track_id]

# Aggregate revenue by store across all countries
agg = track_sales.groupby('store', as_index=False)['revenue_usd'].sum()

# Find the store with maximum revenue
if len(agg) == 0:
    result = None
else:
    max_row = agg.sort_values('revenue_usd', ascending=False).iloc[0]
    result = {
        'store': max_row['store'],
        'total_revenue_usd': float(max_row['revenue_usd'])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Tflv7tytw7CQLrodoSmmMpQq': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_4l5NTMIyeG3EooPsnIJr4E4P': 'file_storage/call_4l5NTMIyeG3EooPsnIJr4E4P.json'}

exec(code, env_args)

code = """import json, pandas as pd
from pathlib import Path

# Load full aggregated revenue data
with open(var_call_o2UwDeMI56h9OQOY7f4GAP0A, 'r') as f:
    sales_agg = json.load(f)

# Put into DataFrame
sales_df = pd.DataFrame(sales_agg)
# Convert to numeric
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)

# Find max revenue and corresponding track_id(s)
max_revenue = sales_df['total_revenue'].max()
max_tracks = sales_df[sales_df['total_revenue'] == max_revenue]['track_id'].tolist()

result = {'max_revenue_usd': max_revenue, 'track_ids': max_tracks}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_o2UwDeMI56h9OQOY7f4GAP0A': 'file_storage/call_o2UwDeMI56h9OQOY7f4GAP0A.json', 'var_call_US79COYSEKpwTi1vW9hB9P0h': 'file_storage/call_US79COYSEKpwTi1vW9hB9P0h.json'}

exec(code, env_args)

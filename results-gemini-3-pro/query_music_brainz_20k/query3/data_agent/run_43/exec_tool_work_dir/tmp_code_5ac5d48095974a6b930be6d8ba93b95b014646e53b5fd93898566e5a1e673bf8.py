code = """import json
import pandas as pd

# Get the file path from the variable
file_path = locals()['var_function-call-14714155237110464570']

# Load the result from the file
with open(file_path, 'r') as f:
    sales_data = json.load(f)

# Convert to DataFrame
df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_sales['track_id'] = df_sales['track_id'].astype(int)

# Sort by revenue just in case
df_sales = df_sales.sort_values('total_revenue', ascending=False)

# Get top 2000 track_ids
top_track_ids = df_sales['track_id'].head(2000).tolist()

print("__RESULT__:")
print(json.dumps(top_track_ids))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json'}

exec(code, env_args)

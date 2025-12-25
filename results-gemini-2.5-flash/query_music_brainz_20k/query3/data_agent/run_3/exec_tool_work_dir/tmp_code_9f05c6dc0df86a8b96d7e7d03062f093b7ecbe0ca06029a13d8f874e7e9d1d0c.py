code = """import json
import pandas as pd

# Load the full result from the file
with open(locals()['var_function-call-17443127908730789968'], 'r') as f:
    sales_data = json.load(f)

# Convert to pandas DataFrame
df_sales = pd.DataFrame(sales_data)

# Find the track_id with the highest total revenue
# Ensure total_revenue is numeric for proper sorting
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
highest_revenue_track_id = df_sales.loc[df_sales['total_revenue'].idxmax()]['track_id']

print('__RESULT__:')
print(json.dumps(highest_revenue_track_id))"""

env_args = {'var_function-call-17443127908730789968': 'file_storage/function-call-17443127908730789968.json'}

exec(code, env_args)

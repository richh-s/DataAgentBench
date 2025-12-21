code = """import json
import pandas as pd

# Load the result from the file
with open('var_function-call-14714155237110464570.json', 'r') as f:
    sales_data = json.load(f)

# Convert to DataFrame
df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_sales['track_id'] = df_sales['track_id'].astype(int)

# Sort by revenue just in case
df_sales = df_sales.sort_values('total_revenue', ascending=False)

# Let's take the top 2000 tracks. 
# If the revenue drops significantly, 2000 is enough.
# If the top revenue is 2500, and the 2000th is very small, we are good.
print(df_sales.head())
print(df_sales.iloc[1999] if len(df_sales) > 1999 else "Less than 2000 records")

top_track_ids = df_sales['track_id'].head(2000).tolist()

print("__RESULT__:")
print(json.dumps(top_track_ids))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json'}

exec(code, env_args)

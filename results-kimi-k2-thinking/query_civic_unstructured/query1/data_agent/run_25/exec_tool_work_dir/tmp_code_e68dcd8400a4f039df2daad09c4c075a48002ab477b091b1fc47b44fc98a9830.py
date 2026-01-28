code = """import json
import pandas as pd

# Load the full funding data from the file
with open('/tmp/tmp9f7l6j8x.json', 'r') as f:
    funding_data = json.load(f)

# Convert to DataFrame for easier processing
df_funding = pd.DataFrame(funding_data)

# Filter for Amount > 50000
df_funding_filtered = df_funding[df_funding['Amount'] > 50000]

print("__RESULT__:")
print(json.dumps({
    'total_funding_records': len(df_funding),
    'funding_gt_50k': len(df_funding_filtered),
    'sample_projects': df_funding_filtered['Project_Name'].head(10).tolist()
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

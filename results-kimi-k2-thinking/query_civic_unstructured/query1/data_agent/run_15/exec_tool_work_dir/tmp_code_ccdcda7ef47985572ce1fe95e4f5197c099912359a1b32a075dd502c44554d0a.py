code = """# Access the funding data from storage
funding_data = locals()['var_functions.query_db:5']

# Check if it's a file path (string) or direct data
if isinstance(funding_data, str):
    import json
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert to DataFrame for analysis
import pandas as pd
df_funding = pd.DataFrame(funding_data)

# Convert Amount to integer
df_funding['Amount'] = df_funding['Amount'].astype(int)

print(f"Number of funding records: {len(df_funding)}")
print(f"Columns: {list(df_funding.columns)}")
print(f"Sample data:")
print(df_funding.head(10).to_string())

# Filter for projects with funding > $50,000
high_funding = df_funding[df_funding['Amount'] > 50000]

print(f"\nProjects with >$50,000 funding: {len(high_funding)}")

# Save for later use
result = {
    "status": "funding_loaded",
    "total_count": len(df_funding),
    "high_funding_count": len(high_funding),
    "high_funding_projects": high_funding['Project_Name'].tolist(),
    "high_funding_data": high_funding.to_dict('records')
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

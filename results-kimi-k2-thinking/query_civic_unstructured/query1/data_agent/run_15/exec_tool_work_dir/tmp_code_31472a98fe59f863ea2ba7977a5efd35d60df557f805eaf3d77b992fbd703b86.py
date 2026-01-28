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

print(f"Number of funding records: {len(df_funding)}")
print(f"Columns: {list(df_funding.columns)}")
print(f"Sample data:")
print(df_funding.head(10).to_string())

# Save for later use
print("__DATA_SUMMARY__")
print(f"Total funding records: {len(df_funding)}")
print(f"Projects with >$50k: {len(df_funding[df_funding['Amount'] > 50000])}")


print("__RESULT__:")
print(json.dumps({"status": "funding_loaded", "count": len(df_funding)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

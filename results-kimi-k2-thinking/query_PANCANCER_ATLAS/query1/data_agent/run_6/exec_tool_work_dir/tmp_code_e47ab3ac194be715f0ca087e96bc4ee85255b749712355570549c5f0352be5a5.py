code = """import json
# Load the data from storage
with open(var_functions.query_db:2, 'r') as f:
    clinical_data = json.load(f)

# Show column names from the clinical data
if clinical_data:
    columns = list(clinical_data[0].keys())
    print("\n=== Clinical Info Table Columns ===")
    for i, col in enumerate(sorted(columns)):
        print(f"{i+1:3d}. {col}")
    
print(f"\nTotal records: {len(clinical_data)}")
print("=== Sample data (first record) ===")
for k, v in clinical_data[0].items():
    print(f"{k}: {v}")"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

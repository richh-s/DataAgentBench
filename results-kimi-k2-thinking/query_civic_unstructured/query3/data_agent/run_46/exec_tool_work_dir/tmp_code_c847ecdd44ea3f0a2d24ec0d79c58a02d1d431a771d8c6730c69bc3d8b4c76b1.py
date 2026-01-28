code = """import json

# Read the funding data
with open('funding_data.json', 'r') as f:
    funding_data = json.load(f)
    
# Check how many records we have
print(f"Total funding records: {len(funding_data)}")
print("First few records:")
for i, record in enumerate(funding_data[:5]):
    print(f"  {record}")
    
# Count projects with FEMA/emergency in the name
fema_projects = [r for r in funding_data if 'fema' in r['Project_Name'].lower() or 'emergency' in r['Project_Name'].lower()]
print(f"\nProjects with FEMA/emergency in name (funding): {len(fema_projects)}")
for p in fema_projects[:10]:
    print(f"  {p}")"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

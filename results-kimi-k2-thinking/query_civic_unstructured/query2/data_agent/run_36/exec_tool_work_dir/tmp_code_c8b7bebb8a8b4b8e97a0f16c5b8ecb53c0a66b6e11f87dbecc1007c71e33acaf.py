code = """import json
import pandas as pd

# Load funding data - the result is stored in a file for var_functions.query_db:13
funding_file_path = var_functions.query_db:13
if isinstance(funding_file_path, str):
    funding_data = []
    with open(funding_file_path, 'r') as f:
        # Read line by line since it's a JSON array in the file
        content = f.read().strip()
        if content.startswith('['):
            funding_data = json.loads(content)
    print(f"Loaded {len(funding_data)} funding records")
else:
    funding_data = funding_file_path

# Clean and prepare funding data
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print("Funding data preview:")
print(funding_df.head())

# Focus on park-related projects
park_projects = funding_df[funding_df['Project_Name'].str.contains('park|playground', case=False, na=False)]
print(f"\nFound {len(park_projects)} park-related projects in funding database")
print(park_projects.head(10))

result = json.dumps({
    'total_park_projects': len(park_projects),
    'park_project_names': park_projects['Project_Name'].tolist()
})
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)

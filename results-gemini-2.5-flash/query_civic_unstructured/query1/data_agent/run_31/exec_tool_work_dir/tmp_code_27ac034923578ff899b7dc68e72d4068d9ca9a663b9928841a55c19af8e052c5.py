code = """import json
import pandas as pd

# Load the extracted civic projects (capital, design status)
civic_projects = locals()['var_function-call-16195811276732115001']
df_civic = pd.DataFrame(civic_projects)

# Load the funding data
with open(locals()['var_function-call-7996456762374373958'], 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Convert 'Amount' to numeric, handling potential errors and setting non-numeric to NaN
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'], errors='coerce')

# Filter funding for amounts greater than $50,000
df_funded_projects = df_funding[df_funding['Amount'] > 50000]

# Join the two dataframes on Project_Name
# Using an inner join to get only projects that exist in both datasets
merged_df = pd.merge(df_civic, df_funded_projects, on='Project_Name', how='inner')

# Get the count of unique projects
count = merged_df['Project_Name'].nunique()

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-1231612348361666956': ['civic_docs'], 'var_function-call-9187705618575875999': 'file_storage/function-call-9187705618575875999.json', 'var_function-call-13415763849644264601': ['Funding'], 'var_function-call-16195811276732115001': [{'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'PCH Median Improvements Project', 'type': 'capital', 'status': 'design'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'capital', 'status': 'design'}], 'var_function-call-7996456762374373958': 'file_storage/function-call-7996456762374373958.json'}

exec(code, env_args)

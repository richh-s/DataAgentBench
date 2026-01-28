code = """import json
import pandas as pd
import re

# Read the civic documents from the file
with open('/tmp/tmp8a3n9p1s.json', 'r') as f:
    civic_docs = json.load(f)

print('Number of civic documents:', len(civic_docs))
keys = list(civic_docs[0].keys()) if civic_docs else []
print('First document keys:', keys)

# Load funding data using locals() - assign to variable first to avoid syntax issues
funding_var_key = 'var_functions.query_db:0'
if funding_var_key in locals():
    funding_data = locals()[funding_var_key]
    funding_df = pd.DataFrame(funding_data)
    
    print('Funding records shape:', funding_df.shape)
    print('Funding columns:', list(funding_df.columns))
    print('First funding record:')
    if not funding_df.empty:
        print(dict(funding_df.iloc[0]))
else:
    print(' Funding data not found in locals')"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

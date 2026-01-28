code = """import json
import re
import pandas as pd

# Load civic documents
civic_docs = []
with open('/tmp/civic_docs_results.json', 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = []
with open('/tmp/funding_results.json', 'r') as f:
    funding_data = json.load(f)

# Convert funding to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Look for 2022 disaster projects and sum their funding
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'recovery']
total_funding = 0
matched_projects = set()

# Process each funding record
for _, row in funding_df.iterrows():
    proj_name = row['Project_Name']
    amount = row['Amount']
    
    # Check if it's a 2022 disaster project
    if '2022' in proj_name and any(kw in proj_name for kw in disaster_keywords):
        total_funding += amount
        matched_projects.add(proj_name)
    # Check for partial matches with disaster context
    elif '2022' in proj_name:
        if 'disaster' in proj_name.lower() or 'recovery' in proj_name.lower():
            total_funding += amount
            matched_projects.add(proj_name)

# Create simple result dict
result_dict = {
    'total_funding': int(total_funding),
    'number_of_projects': len(matched_projects)
}

# Use standard print without f-strings
print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

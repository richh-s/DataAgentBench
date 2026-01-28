code = """import json
import re
import pandas as pd

# Access variables using the correct key names
civic_docs_path = locals()['var_functions.query_db:6']
funding_path = locals()['var_functions.query_db:8']

# Load civic documents
civic_docs = []
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = []
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Initialize disaster project names set
disaster_project_names = set()
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'recovery']

# Extract disaster projects from civic docs
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        is_disaster = False
        if any(kw in line for kw in disaster_keywords):
            is_disaster = True
        if re.search(r'\((FEMA|CalOES|CalJPIA)( Project)?\)', line):
            is_disaster = True
        
        if is_disaster:
            # Check if it's 2022 project
            project_name = line
            if '2022' in project_name:
                disaster_project_names.add(project_name)

# Add projects from funding data that have 2022 and disaster keywords
for _, row in funding_df.iterrows():
    proj_name = row['Project_Name']
    if '2022' in proj_name and any(kw in proj_name for kw in disaster_keywords):
        disaster_project_names.add(proj_name)

# Calculate total funding
total_funding = 0
matched_funding_projects = set()

for _, row in funding_df.iterrows():
    fund_proj = row['Project_Name']
    amount = row['Amount']
    
    # Check if this funding project matches any disaster project
    for disaster_proj in disaster_project_names:
        # Exact match
        if fund_proj == disaster_proj:
            total_funding += amount
            matched_funding_projects.add(fund_proj)
            break
        # Partial match with disaster keyword verification
        elif disaster_proj in fund_proj or fund_proj in disaster_proj:
            if any(kw in fund_proj for kw in disaster_keywords):
                total_funding += amount
                matched_funding_projects.add(fund_proj)
                break

# Prepare result
result = {
    'total_funding': int(total_funding),
    'number_of_projects': len(matched_funding_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

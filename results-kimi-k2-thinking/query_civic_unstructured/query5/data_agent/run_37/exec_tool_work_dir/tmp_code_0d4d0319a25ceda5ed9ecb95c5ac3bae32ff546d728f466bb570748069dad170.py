code = """import json
import pandas as pd
import re

# Load the data files
f_file = locals()['var_functions.query_db:9']
with open(f_file, 'r') as f:
    funding_data = json.load(f)

c_file = locals()['var_functions.query_db:5']
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract disaster projects with 2022 dates from civic documents
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'recovery']
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '2022' in line:
                context = ' '.join(lines[max(0,i-3):min(len(lines),i+4)])
                if any(keyword.lower() in context for keyword in disaster_keywords):
                    projects_2022.append(line)

print('Found disasters with 2022 references:', len(projects_2022))

# Find all disaster funding projects
disaster_funding = []
for _, row in funding_df.iterrows():
    if any(keyword.lower() in row['Project_Name'].lower() for keyword in disaster_keywords):
        disaster_funding.append(row)

disaster_funding_df = pd.DataFrame(disaster_funding)
total_all = disaster_funding_df['Amount'].sum()

# Check 2022 specific funding
funding_2022 = disaster_funding_df[disaster_funding_df['Project_Name'].str.contains('2022', case=False, na=False)]
total_2022 = funding_2022['Amount'].sum()

print('All disaster funding:', total_all)
print('2022 in name disaster funding:', total_2022)
print('Disaster project count:', len(disaster_funding_df))

result = {
    'total_disaster_funding_all': int(total_all),
    'disaster_funding_2022': int(total_2022),
    'projects_2022_count': len(projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:18': {'total_disaster_funding': 1410000, 'disaster_project_count': 27, 'sample_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': 85000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': 14000}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': 81000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': 43000}]}}

exec(code, env_args)

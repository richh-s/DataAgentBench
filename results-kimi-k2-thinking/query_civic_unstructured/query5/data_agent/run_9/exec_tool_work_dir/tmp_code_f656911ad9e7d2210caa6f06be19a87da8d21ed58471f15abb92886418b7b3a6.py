code = """import json
import re

# Load data from the stored results
civic_var = locals().get('var_functions.query_db:6')
funding_var = locals().get('var_functions.query_db:8')

# Read the files
with open(civic_var, 'r') as f:
    civic_docs = json.load(f)

with open(funding_var, 'r') as f:
    funding_data = json.load(f)

# Basic approach: Look for projects in both data sources
# that are disaster-related and started in 2022

disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'recovery']

# Extract project names from civic docs that are disaster projects with 2022 dates
disaster_2022_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for patterns like "2022 [Project Name]" or "[Project Name] 2022"
    # and check if they contain disaster keywords
    
    # Find potential project names (lines that are not too short, not bullet points)
    for line in text.split('\n'):
        line = line.strip()
        if len(line) > 15 and not line.startswith('•') and not line.startswith('('):
            # Check if it's a disaster project
            is_disaster = any(kw in line for kw in disaster_keywords)
            # Check if it has 2022
            has_2022 = '2022' in line
            if is_disaster and has_2022:
                disaster_2022_names.add(line)

# Also check funding data directly
for item in funding_data:
    proj_name = item['Project_Name']
    if '2022' in proj_name and any(kw in proj_name for kw in disaster_keywords):
        disaster_2022_names.add(proj_name)

# Calculate total funding
total = 0
for item in funding_data:
    if item['Project_Name'] in disaster_2022_names:
        total += int(item['Amount'])

result = {'total_funding': total, 'project_names': list(disaster_2022_names)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:20': {'total_funding': 0, 'projects_count': 0}}

exec(code, env_args)

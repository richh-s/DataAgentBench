code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:28
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Identify all disaster projects from funding data
# Disaster projects have FEMA, CalOES, or CalJPIA in their names
disaster_projects = {}
for item in funding_data:
    project_name = item['Project_Name']
    upper_name = project_name.upper()
    
    if 'FEMA' in upper_name or 'CALOES' in upper_name or 'CALJPIA' in upper_name:
        funding_id = item['Funding_ID']
        amount = int(item['Amount'])
        
        # Store project info
        disaster_projects[project_name] = {
            'funding_id': funding_id,
            'amount': amount,
            'started_2022': False,
            'date_evidence': []
        }

print(f"Found {len(disaster_projects)} disaster-related projects in funding data")

# Step 2: Extract start dates from civic documents
# We'll look for mentions of disaster projects with 2022 dates

# Create a mapping of base project names to full names
# This helps match projects with/without the disaster suffixes
project_name_map = {}
for project_name in disaster_projects.keys():
    # Extract base name without disaster suffix
    base_name = project_name.replace(' (FEMA Project)', '') \
                          .replace(' (CalOES Project)', '') \
                          .replace(' (FEMA/CalOES Project)', '') \
                          .replace(' (CalJPIA Project)', '') \
                          .replace(' (CalJPIA/FEMA Project)', '')
    
    if base_name != project_name:
        project_name_map[base_name] = project_name
    project_name_map[project_name] = project_name

# Search through civic documents for 2022 start dates
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if '2022' not in text:
        continue
    
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Check if this line mentions any of our disaster projects
        for base_name, full_name in project_name_map.items():
            if base_name in line or full_name in line:
                # Look for date information in this line and nearby lines
                for j in range(max(0, i-2), min(len(lines), i+5)):
                    date_line = lines[j].strip()
                    
                    if '2022' in date_line:
                        # Check if this is schedule/ timing information
                        schedule_indicators = ['Complete', 'Schedule', 'Advertise', 'Begin', 'Construction', 
                                             'Design', 'Complete Design', 'Project Schedule', 'Estimated Schedule']
                        
                        if any(indicator in date_line for indicator in schedule_indicators):
                            # Found evidence this project has 2022 dates
                            if full_name in disaster_projects:
                                disaster_projects[full_name]['started_2022'] = True
                                if date_line not in disaster_projects[full_name]['date_evidence']:
                                    disaster_projects[full_name]['date_evidence'].append(date_line)

# Also check for projects with 2022 in their name directly
for project_name in disaster_projects.keys():
    if '2022' in project_name:
        disaster_projects[project_name]['started_2022'] = True
        disaster_projects[project_name]['date_evidence'].append('2022 in project name')

# Step 3: Calculate total funding for disaster projects that started in 2022
total_2022_funding = 0
projects_2022 = []

for project_name, info in disaster_projects.items():
    if info['started_2022']:
        total_2022_funding += info['amount']
        projects_2022.append({
            'project_name': project_name,
            'amount': info['amount'],
            'funding_id': info['funding_id'],
            'date_evidence': info['date_evidence'][:3]  # Limit evidence shown
        })

# Prepare results
result = {
    'total_disaster_projects': len(disaster_projects),
    'disaster_projects_2022': len(projects_2022),
    'total_funding_2022': total_2022_funding,
    'projects': sorted(projects_2022, key=lambda x: x['amount'], reverse=True)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_disaster_projects_in_funding': 20, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_ID': '7', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_ID': '22', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_ID': '25', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_ID': '26', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_ID': '28', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_ID': '29', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_ID': '35', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_ID': '38', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_ID': '39', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_ID': '43', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)

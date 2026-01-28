code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:16
if isinstance(funding_file, str):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

# Load civic documents
civic_file = var_functions.query_db:5
if isinstance(civic_file, str):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

# Step 1: Identify disaster projects from funding data
disaster_keywords = ['FEMA', 'CALOES', 'CALJPIA']
disaster_projects_funding = {}

for item in funding_data:
    project_name = item['Project_Name']
    if any(keyword in project_name.upper() for keyword in disaster_keywords):
        funding_id = item['Funding_ID']
        amount = int(item['Amount'])
        disaster_projects_funding[project_name] = {
            'Funding_ID': funding_id,
            'Amount': amount,
            'started_2022': False  # Will update based on civic docs
        }

print(f"Found {len(disaster_projects_funding)} disaster projects in funding data")

# Step 2: Parse civic documents to find projects that started in 2022
# Store project start dates as we find them
project_start_dates = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project names that match our disaster projects
        for project_name in disaster_projects_funding.keys():
            # Check if project name (or base name without suffix) appears in line
            base_name = project_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA Project)', '')
            
            if project_name in line or (base_name != project_name and base_name in line):
                # Look ahead for date information
                for j in range(i, min(i+8, len(lines))):
                    date_line = lines[j].strip()
                    
                    # Look for 2022 dates
                    if '2022' in date_line:
                        # Look for start/completion schedule patterns
                        if any(keyword in date_line for keyword in ['Complete', 'Schedule', 'Advertise', 'Begin Construction', 'Complete Construction', 'Complete Design', 'Project Schedule']):
                            # Mark this project as having 2022 date
                            if project_name not in project_start_dates:
                                project_start_dates[project_name] = []
                            project_start_dates[project_name].append(date_line)
                            
                            # If this is about scheduling/completion/beginning in 2022, mark as started in 2022
                            if any(phrase in date_line for phrase in ['Complete: 2022', '2022-', '2022:']):
                                if project_name in disaster_projects_funding:
                                    disaster_projects_funding[project_name]['started_2022'] = True

# Identify clearly which disaster projects started in 2022
disaster_2022_projects = []
for project_name, details in disaster_projects_funding.items():
    base_name = project_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA Project)', '')
    
    # Check if we found 2022 dates for this project
    if project_name in project_start_dates:
        has_2022_schedule = any('2022' in date_entry for date_entry in project_start_dates[project_name])
        if has_2022_schedule:
            disaster_2022_projects.append({
                'Project_Name': project_name,
                'Base_Name': base_name,
                'Amount': details['Amount'],
                'Funding_ID': details['Funding_ID'],
                'Dates_Found': project_start_dates[project_name]
            })
    else:
        # Also check if the project name itself contains 2022
        if '2022' in project_name:
            disaster_2022_projects.append({
                'Project_Name': project_name,
                'Base_Name': base_name,
                'Amount': details['Amount'],
                'Funding_ID': details['Funding_ID'],
                'Dates_Found': ['2022 in project name']
            })

# Calculate total funding
total_funding = sum(p['Amount'] for p in disaster_2022_projects)

print('__RESULT__:')
print(json.dumps({
    'total_disaster_projects': len(disaster_projects_funding),
    'disaster_2022_projects_count': len(disaster_2022_projects),
    'total_funding_2022': total_funding,
    'projects': disaster_2022_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_disaster_projects_in_funding': 20, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_ID': '7', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_ID': '22', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_ID': '25', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_ID': '26', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_ID': '28', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_ID': '29', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_ID': '35', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_ID': '38', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_ID': '39', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_ID': '43', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

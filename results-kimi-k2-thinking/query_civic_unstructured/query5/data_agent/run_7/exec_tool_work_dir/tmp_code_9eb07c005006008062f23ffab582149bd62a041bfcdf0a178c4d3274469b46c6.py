code = """import json
import re

# Load the complete data
civic_docs_path = locals()['var_functions.query_db:8']
funding_path = locals()['var_functions.query_db:0']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

# Function to identify disaster projects
def is_disaster_project(project_name):
    return any(marker in project_name for marker in ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)'])

# Extract disaster projects from funding data
disaster_projects = []
for record in funding_data:
    if is_disaster_project(record['Project_Name']):
        disaster_projects.append(record)

# Parse civic docs to find 2022 start dates
disaster_2022_projects = []
disaster_2022_names = set()

# Look for specific patterns that indicate 2022 start
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern 1: Projects explicitly listed with 2022 prefix
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('2022') and any(marker in line for marker in ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)']):
            # Extract project name
            for marker in ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)']:
                if marker in line:
                    idx = line.find(marker)
                    project_name = line[:idx + len(marker)].strip()
                    # Remove the "2022 " prefix if present
                    if project_name.startswith('2022 '):
                        project_name = project_name[5:]
                    disaster_2022_names.add(project_name)
                    break
    
    # Pattern 2: Look for "2022" in context with disaster project markers
    if '2022' in text:
        # Find all sections that mention both 2022 and disaster markers
        sections = text.split('\n\n')
        for section in sections:
            if '(FEMA Project)' in section and '2022' in section:
                # Extract the project name based on line structure
                lines = section.split('\n')
                for i, line in enumerate(lines):
                    if '(FEMA Project)' in line and len(line.strip()) < 150:
                        disaster_2022_names.add(line.strip())

# Match disaster projects with 2022 funding records
matched_funding = []
total_funding = 0

for proj in disaster_projects:
    proj_name = proj['Project_Name']
    
    # Direct match
    if proj_name in disaster_2022_names:
        matched_funding.append(proj)
        total_funding += proj['Amount']
    else:
        # For projects with 2022 prefix in different format
        base_name = proj_name.replace('2022 ', '').strip()
        for name_2022 in disaster_2022_names:
            if name_2022.startswith(base_name[:30]):
                matched_funding.append(proj)
                total_funding += proj['Amount']
                break

print('__RESULT__:')  
result = {
    'total_disaster_projects': len(disaster_projects),
    'disaster_2022_projects': len(matched_funding),
    'total_funding_2022': total_funding,
    'fund_details': [{'name': p['Project_Name'], 'amount': p['Amount']} for p in matched_funding]
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records_count': 500, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.execute_python:16': {'disaster_projects_found': 27, 'total_disaster_funding': 1410000, 'sample_disaster_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)'], 'sample_funding_records': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}]}, 'var_functions.execute_python:18': {'total_disaster_2022_projects': 0, 'total_funding': 0, 'sample_projects': []}}

exec(code, env_args)

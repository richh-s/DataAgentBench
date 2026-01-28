code = """import json
import re

# Load data
civic_docs_path = locals()['var_functions.query_db:8']
funding_path = locals()['var_functions.query_db:0']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

def extract_project_info_from_docs():
    """Extract project information including start dates from civic docs"""
    projects = []
    
    for doc in civic_docs:
        text = doc.get('text', '')
        # Split by common project markers
        sections = re.split(r'\n\s*\n', text)
        
        for section in sections:
            section = section.strip()
            if not section or len(section) < 20:
                continue
            
            # Look for disaster projects
            disaster_markers = ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)']
            is_disaster = any(marker in section for marker in disaster_markers)
            
            if is_disaster:
                # Extract project name (usually first line or has markers)
                lines = section.split('\n')
                project_name = None
                
                for line in lines[:3]:  # Check first few lines
                    line = line.strip()
                    if any(marker in line for marker in disaster_markers):
                        # This is likely the project name
                        for marker in disaster_markers:
                            if marker in line:
                                # Extract up to the marker
                                idx = line.find(marker)
                                project_name = line[:idx + len(marker)].strip()
                                break
                        if not project_name:
                            project_name = line
                        break
                
                if not project_name:
                    # Try to find name in the section
                    for line in lines:
                        if any(marker in line for marker in disaster_markers):
                            project_name = line.strip()
                            break
                
                if project_name:
                    # Look for date information
                    st = None
n                    # Look for 2022 mentions
                    if '2022' in section:
                        # Look for schedule/project timeline
                        if 'Project Schedule:' in section or 'Schedule:' in section:
                            # Check if 2022 appears near schedule info
                            schedule_idx = section.find('Schedule:')
                            if schedule_idx > 0:
                                schedule_section = section[schedule_idx:schedule_idx+300]
                                if '2022' in schedule_section:
                                    st = '2022'
                    
                    projects.append({
                        'Project_Name': project_name,
                        'type': 'disaster',
                        'st': st,
                        'source_text': section[:200]
                    })
    
    return projects

# Extract project info
extracted_projects = extract_project_info_from_docs()

# Get all disaster project names from funding
all_disaster_projects = []
for record in funding_data:
    name = record['Project_Name']
    if '(FEMA Project)' in name or '(CalJPIA Project)' in name or '(CalOES Project)' in name:
        all_disaster_projects.append({
            'Project_Name': name,
            'Amount': record['Amount'],
            'Funding_ID': record['Funding_ID']
        })

# Try to find which disaster projects started in 202n2
projects_2022 = []
total_funding = 0

# Cross-reference extracted projects with start dates
for proj in extracted_projects:
    if proj['st'] == '2022':
        # Find matching funding record
        proj_name_base = proj['Project_Name'].split('(')[0].strip()
        for fund_proj in all_disaster_projects:
            if fund_proj['Project_Name'].startswith(proj_name_base):
                projects_2022.append(fund_proj)
                total_funding += fund_proj['Amount']

# Also check projects with 2022 in their name
for fund_proj in all_disaster_projects:
    if '2022' in fund_proj['Project_Name']:
        # Check if already added
        if fund_proj['Funding_ID'] not in [p['Funding_ID'] for p in projects_2022]:
            projects_2022.append(fund_proj)
            total_funding += fund_proj['Amount']

print('__RESULT__:')
result = {
    'extracted_projects_with_dates': len(extracted_projects),
    'disaster_projects_2022': len(projects_2022),
    'total_funding_2022': total_funding,
    'projects_2022': projects_2022
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records_count': 500, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.execute_python:16': {'disaster_projects_found': 27, 'total_disaster_funding': 1410000, 'sample_disaster_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)'], 'sample_funding_records': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}]}, 'var_functions.execute_python:18': {'total_disaster_2022_projects': 0, 'total_funding': 0, 'sample_projects': []}}

exec(code, env_args)

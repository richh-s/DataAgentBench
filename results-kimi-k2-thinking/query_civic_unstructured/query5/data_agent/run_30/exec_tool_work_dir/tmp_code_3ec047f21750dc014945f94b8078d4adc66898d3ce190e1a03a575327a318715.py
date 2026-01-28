code = """import json
import re

# Load full funding data
funding_file = locals()['var_functions.query_db:10']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents data
civic_file = locals()['var_functions.query_db:6']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Extract project information from civic documents
# Key pattern: Project names appear as titles, followed by Updates/Schedule sections
project_database = {}

disaster_markers = ['fema', 'caloes', 'caljpia', 'emergency', 'fire', 'disaster', 'warning', 'siren']
year_marker = '2022'

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip headers and noise
        if any(skip in line for skip in ['Page', 'Agenda Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
            continue
        
        # Detect project name (typically a descriptive title, not too short)
        if len(line) > 15 and not line.startswith('(') and not line.startswith('ï¿½') and 'Updates:' not in line and 'Schedule:' not in line:
            # This could be a project name
            current_project = line
            if current_project not in project_database:
                project_database[current_project] = {
                    'name': current_project,
                    'source_file': filename,
                    'is_disaster': False,
                    'start_year': None,
                    'mentions_2022': False
                }
        
        # Process project details if we have a current project
        if current_project:
            lower_line = line.lower()
            
            # Check for disaster markers
            if any(marker in lower_line for marker in disaster_markers):
                project_database[current_project]['is_disaster'] = True
            
            # Check for 2022 mentions
            if year_marker in line:
                project_database[current_project]['mentions_2022'] = True
                
                # Try to determine if it's a start date
                if any(schedule_word in lower_line for schedule_word in ['complete design:', 'begin construction:', 'advertise:', 'final design:', 'project schedule:', 'estimated schedule:']):
                    project_database[current_project]['start_year'] = year_marker

# Step 2: Identify disaster projects that started in 2022
disaster_2022_projects = [
    proj['name'] for proj in project_database.values() 
    if proj['is_disaster'] and (proj['start_year'] == '2022' or proj['mentions_2022'])
]

# Step 3: Match with funding records
total_funding = 0
matched_projects = []

for funding in funding_records:
    fund_name = funding.get('Project_Name', '')
    fund_amount = float(funding.get('Amount', 0))
    fund_name_lower = fund_name.lower()
    
    # Direct match check
    for disaster_proj in disaster_2022_projects:
        if disaster_proj.lower() in fund_name_lower or fund_name_lower in disaster_proj.lower():
            total_funding += fund_amount
            matched_projects.append({
                'project_name': disaster_proj,
                'funding_name': fund_name,
                'amount': fund_amount
            })
            break

# Alternative: Look for disaster-related projects with 2022 in funding name
alt_total = 0
alt_matches = []

for funding in funding_records:
    fund_name = funding.get('Project_Name', '')
    fund_amount = float(funding.get('Amount', 0))
    fund_name_lower = fund_name.lower()
    
    has_2022 = '2022' in fund_name
    is_disaster = any(marker in fund_name_lower for marker in disaster_markers)
    
    if has_2022 and is_disaster:
        alt_total += fund_amount
        alt_matches.append(fund_name)

# Also check infrastructure projects with 2022 that might be disaster recovery
infrastructure_2022_total = 0
for funding in funding_records:
    fund_name = funding.get('Project_Name', '')
    fund_amount = float(funding.get('Amount', 0))
    fund_name_lower = fund_name.lower()
    
    if fund_name.startswith('2022'):
        # Check for storm/drain/road keywords that could be disaster recovery
        if any(keyword in fund_name_lower for keyword in ['storm', 'drain', 'resurfacing', 'repair']):
            infrastructure_2022_total += fund_amount

print('__RESULT__:')
print(json.dumps({
    'civic_disaster_2022_count': len(disaster_2022_projects),
    'funding_matches': len(matched_projects),
    'total_matched_funding': total_funding,
    'alt_2022_disaster_funding': alt_total,
    'infrastructure_2022_funding': infrastructure_2022_total,
    'grand_total_estimate': total_funding + alt_total + infrastructure_2022_total
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:22': {'total_funding': 0, 'record_count': 0}, 'var_functions.execute_python:24': {'total_funding': 38000.0, 'project_list': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000.0}]}, 'var_functions.execute_python:26': {'total_disaster_funding_all_years': 1603000.0, 'total_disaster_2022_funding': 0, 'disaster_2022_projects': [], 'all_disaster_projects_count': 30}}

exec(code, env_args)

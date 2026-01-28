code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:6'], 'r') as f:
    funding_records = json.load(f)

with open(locals()['var_functions.query_db:8'], 'r') as f:
    civic_docs = json.load(f)

# Identify disaster-related projects by name patterns in funding data
disaster_suffixes = [
    '(FEMA Project)',
    '(FEMA/CalOES Project)', 
    '(CalOES Project)',
    '(CalJPIA Project)',
    '(FEMA)',
    '(FEMA/CalOES)'
]

disaster_project_names = set()
for record in funding_records:
    project_name = record['Project_Name']
    if any(project_name.endswith(suffix) for suffix in disaster_suffixes):
        disaster_project_names.add(project_name)

# Extract project info from civic documents
project_schedules = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    in_schedule_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project headers
        if len(line) > 10 and line == line.title() and not any(kw in line.lower() for kw in ['updates:', 'project schedule:', 'cip', 'public works']):
            if not any(line.startswith(prefix) for prefix in ['(', '-', '•', '·', 'c:', 'cid:']):
                current_project = line
                project_schedules[current_project] = {'st': None, 'et': None}
        
        # Look for schedule section
        if 'project schedule:' in line.lower() or 'estimated schedule:' in line.lower():
            in_schedule_section = True
            current_project_pos = i
            
        # Extract dates from schedule section
        if in_schedule_section and current_project:
            # Look for lines with dates
            if re.search(r'\d{4}', line):
                # Check for start-related keywords
                if any(kw in line.lower() for kw in ['begin', 'start', 'advertise', 'initiate']):
                    if project_schedules[current_project]['st'] is None:
                        project_schedules[current_project]['st'] = line
                # Check for end/completion keywords
                elif any(kw in line.lower() for kw in ['complete', 'end', 'finish', 'completion']):
                    if project_schedules[current_project]['et'] is None:
                        project_schedules[current_project]['et'] = line
                        
        # Reset schedule section when we hit empty lines or new sections
        if line == '' and in_schedule_section:
            in_schedule_section = False

disaster_projects_2022 = []

# Match disaster projects from funding with those that started in 2022
for record in funding_records:
    project_name = record['Project_Name']
    
    if any(project_name.endswith(suffix) for suffix in disaster_suffixes):
        # Check base name match
        base_name = project_name
        for suffix in disaster_suffixes:
            base_name = base_name.replace(suffix, '').strip()
        
        # Look for this base name in project schedules
        found_start_2022 = False
        
        for proj_name, schedule in project_schedules.items():
            if base_name in proj_name or proj_name in base_name:
                st_date = schedule['st']
                if st_date and '2022' in st_date:
                    found_start_2022 = True
                    break
        
        if found_start_2022:
            disaster_projects_2022.append({
                'Project_Name': project_name,
                'Amount': int(record['Amount'])
            })

total_funding = sum(p['Amount'] for p in disaster_projects_2022)

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'project_count': len(disaster_projects_2022),
    'projects': disaster_projects_2022
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_records_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:20': {'funding_records_count': 500, 'civic_docs_count': 5, 'first_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'first_civic_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_length': 9796}}, 'var_functions.execute_python:22': {'disaster_projects_count': 26, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 85000, 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 14000, 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Base_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': 81000, 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Base_Name': 'Clover Heights Storm Drain', 'Amount': 21000, 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 43000, 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 15000, 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 25000, 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 58000, 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 18000, 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 94000, 'Funding_Source': 'Private Sponsor'}]}}

exec(code, env_args)

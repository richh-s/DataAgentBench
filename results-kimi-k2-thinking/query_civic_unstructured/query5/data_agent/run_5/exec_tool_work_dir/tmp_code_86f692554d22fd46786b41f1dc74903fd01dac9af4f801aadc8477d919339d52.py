code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Define disaster indicators
DISASTER_SUFFIXES = [
    '(FEMA Project)',
    '(FEMA/CalOES Project)',
    '(CalOES Project)',
    '(CalJPIA Project)',
    '(FEMA)',
    '(FEMA/CalOES)'
]

# Extract disaster projects from funding data
disaster_projects_map = {}
for record in funding_records:
    proj_name = record['Project_Name']
    if any(proj_name.endswith(suffix) for suffix in DISASTER_SUFFIXES):
        # Get base name without suffix for matching
        base_name = proj_name
        for suffix in DISASTER_SUFFIXES:
            base_name = base_name.replace(suffix, '').strip()
        
        disaster_projects_map[base_name.lower()] = {
            'full_name': proj_name,
            'amount': int(record['Amount'])
        }

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Find projects that started in 2022
projects_starting_in_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Look for each disaster project in text
    for base_name_lower, proj_info in disaster_projects_map.items():
        if base_name_lower in text_lower:
            # Found the project, now find date info with 2022
            # Look for sections mentioning this project and dates
            lines = text.split('\n')
            
            for i, line in enumerate(lines):
                line_lower = line.lower()
                
                # If this line mentions the project
                if base_name_lower in line_lower:
                    # Look ahead for date information
                    for j in range(i, min(i + 10, len(lines))):
                        candidate_line = lines[j]
                        if '2022' in candidate_line and any(time_word in candidate_line.lower() 
                                                           for time_word in ['start', 'begin', 'advertise', 'initiate', 'complete', 'end']):
                            projects_starting_in_2022.add(proj_info['full_name'])
                            break
            
            # Also check if the filename contains 2022 and mentions the project
            filename = doc.get('filename', '')
            if '2022' in filename and base_name_lower in text_lower:
                projects_starting_in_2022.add(proj_info['full_name'])

# Calculate total funding
total_funding = 0
funded_projects = []

for proj_name in projects_starting_in_2022:
    for base_lower, proj_info in disaster_projects_map.items():
        if proj_info['full_name'] == proj_name:
            total_funding += proj_info['amount']
            funded_projects.append({
                'project': proj_name,
                'amount': proj_info['amount']
            })

result = {
    'total_funding': total_funding,
    'project_count': len(funded_projects),
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_records_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:20': {'funding_records_count': 500, 'civic_docs_count': 5, 'first_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'first_civic_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_length': 9796}}, 'var_functions.execute_python:22': {'disaster_projects_count': 26, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 85000, 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 14000, 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Base_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': 81000, 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Base_Name': 'Clover Heights Storm Drain', 'Amount': 21000, 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 43000, 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 15000, 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 25000, 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 58000, 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 18000, 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 94000, 'Funding_Source': 'Private Sponsor'}]}}

exec(code, env_args)

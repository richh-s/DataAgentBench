code = """import json
import re

# Load data
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Step 1: Get all funding records with FEMA/emergency
fema_projects = []
funding_dict = {}

for item in funding_data:
    proj_name = item['Project_Name']
    funding_dict[proj_name] = item
    
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        fema_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency',
            'Found_In': 'funding_table'
        })

print(f"Found {len(fema_projects)} FEMA/emergency projects in funding table")

# Step 2: Extract project status from civic documents
status_info = {}

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 5:
            continue
            
        # Look for project names (reasonable length, not headers)
        if 10 <= len(line) <= 150 and not line.startswith('('):
            # Skip common headers
            lower = line.lower()
            if any(keyword in lower for keyword in ['capital improvement', 'disaster recovery', 'status report', 'project schedule', 'updates:', 'recommended action', 'discussion:', 'agenda', 'commission', 'public works', 'page ', 'item #']):
                continue
            
            # Check if this project is in our funding list
            matched_project = None
            for proj_name in funding_dict.keys():
                if proj_name in line or line in proj_name:
                    if len(line) > len(proj_name) * 0.5:  # Reasonable match
                        matched_project = proj_name
                        break
            
            if matched_project:
                # Look for status in following lines
                status = 'unknown'
                for j in range(i+1, min(i+8, len(lines))):
                    next_line = lines[j].strip().lower()
                    
                    # Check for status patterns
                    if 'design' in next_line and ('complete' in next_line or 'finalize' in next_line or 'working' in next_line):
                        status = 'design'
                        break
                    elif 'construction' in next_line:
                        if 'under' in next_line or 'begin' in next_line:
                            status = 'construction'
                        elif 'complete' in next_line:
                            status = 'completed'
                        break
                    elif 'completed' in next_line or 'completion' in next_line:
                        status = 'completed'
                        break
                    elif 'not started' in next_line:
                        status = 'not started'
                        break
                
                status_info[matched_project] = status

# Step 3: Update FEMA projects with status information
final_results = []
for proj in fema_projects:
    proj_name = proj['Project_Name']
    if proj_name in status_info:
        proj['Status'] = status_info[proj_name]
    final_results.append(proj)

# Sort by amount (descending)
final_results.sort(key=lambda x: x['Amount'], reverse=True)

print(f"Total projects with status info: {len([p for p in final_results if p['Status'] != 'unknown'])}")

# Prepare final output
output = []
for proj in final_results:
    output.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': proj['Status'],
        'Topic': proj['Topic']
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:34': {'count': 20, 'sample': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}]}}

exec(code, env_args)

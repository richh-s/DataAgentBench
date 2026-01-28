code = """import json
import re

# Load the funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents data
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Step 1: Find all funding records with FEMA or emergency
fema_funding_projects = []
for item in funding_data:
    project_name = item['Project_Name']
    if 'FEMA' in project_name or 'emergency' in project_name.lower():
        fema_funding_projects.append({
            'Project_Name': project_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency',
            'Source': 'funding_table'
        })

# Create a lookup dictionary for funding data
funding_lookup = {item['Project_Name']: item for item in funding_data}

# Step 2: Extract status information from civic documents
project_status = {}

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10:
            continue
            
        # Skip headers/footers
        lower_line = line.lower()
        if any(skip in lower_line for skip in ['capital improvement', 'disaster recovery', 'status report', 'project schedule', 'updates:', 'recommended action', 'discussion:', 'agenda', 'commission', 'public works', 'page', 'item #']):
            continue
        if line.startswith('Page') or line.startswith('Item'):
            continue
            
        # Check if line mentions FEMA projects
        if 'FEMA' in line or 'emergency' in lower_line:
            # Look for project names in this and nearby lines
            potential_names = []
            
            # Current line
            if 10 <= len(line) <= 150 and not line.startswith('('):
                clean_name = re.sub(r'\s+', ' ', line).strip()
                clean_name = re.sub(r'^[•\-\*\d\.\)]+\s*', '', clean_name)
                potential_names.append(clean_name)
            
            # Previous line (often project name comes before details)
            if i > 0:
                prev_line = lines[i-1].strip()
                if 10 <= len(prev_line) <= 150:
                    clean_name = re.sub(r'\s+', ' ', prev_line).strip()
                    clean_name = re.sub(r'^[•\-\*\d\.\)]+\s*', '', clean_name)
                    potential_names.append(clean_name)
            
            # Find status information
            status = 'unknown'
            for j in range(i+1, min(i+12, len(lines))):
                next_line = lines[j].strip().lower()
                
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
            
            # Map status to projects
            for pot_name in potential_names:
                # Direct match with funding projects
                for fund_proj in fema_funding_projects:
                    if pot_name in fund_proj['Project_Name'] or fund_proj['Project_Name'] in pot_name:
                        project_status[fund_proj['Project_Name']] = status
                
                # Try to match with any funding record
                for fund_name in funding_lookup.keys():
                    if fund_name in pot_name or pot_name in fund_name:
                        project_status[fund_name] = status

# Step 3: Combine funding data with status
final_results = []
for proj in fema_funding_projects:
    project_name = proj['Project_Name']
    status = project_status.get(project_name, 'unknown')
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status,
        'Topic': proj['Topic']
    })

# Sort by amount (highest first)
final_results.sort(key=lambda x: x['Amount'], reverse=True)

# Display results
print('Found', len(final_results), 'FEMA/emergency related projects:')
print()

for i, proj in enumerate(final_results, 1):
    print(f"{i}. {proj['Project_Name']}")
    print(f"   Funding Source: {proj['Funding_Source']}")
    print(f"   Amount: ${proj['Amount']:,}")
    print(f"   Status: {proj['Status']}")
    print(f"   Topic: {proj['Topic']}")
    print()

# Prepare JSON output
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

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:34': {'count': 20, 'sample': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)

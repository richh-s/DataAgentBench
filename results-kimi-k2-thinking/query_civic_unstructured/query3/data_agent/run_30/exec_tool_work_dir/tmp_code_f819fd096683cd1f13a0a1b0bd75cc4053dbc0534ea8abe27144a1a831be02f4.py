code = """import json
import re

funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Step 1: Get all FEMA/emergency projects from funding table
fema_projects = []
for item in funding_data:
    proj_name = item['Project_Name']
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        fema_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

# Step 2: Extract project status from civic documents
project_status = {}

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    current_section = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Detect section headers
        lower_line = line.lower()
        if 'capital improvement projects (design)' in lower_line:
            current_section = 'design'
            continue
        elif 'capital improvement projects (construction)' in lower_line:
            current_section = 'construction'
            continue
        elif 'capital improvement projects (not started)' in lower_line:
            current_section = 'not_started'
            continue
        elif 'disaster recovery projects' in lower_line:
            current_section = 'disaster'
            continue
        
        # Skip headers and footers
        if any(keyword in lower_line for keyword in ['agenda', 'commission', 'page ', 'item #', 'public works', 'status report', 'recommended action', 'discussion:']):
            continue
        if line.startswith('Page') or line.startswith('Item'):
            continue
        
        # Look for project names (reasonable length, not obvious headers)
        if len(line) > 10 and len(line) < 150 and not line.startswith('(') and not line.endswith(':'):
            # Check if it's a project name by seeing if next lines have updates/status
            has_updates = False
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].strip().lower()
                if ('updates:' in next_line or 'status' in next_line or 'schedule' in next_line or 
                    'construction' in next_line or 'design' in next_line or 'completed' in next_line):
                    has_updates = True
                    break
            
            if has_updates:
                current_project = line
                
                # Default status based on section
                if current_section == 'design':
                    project_status[current_project] = 'design'
                elif current_section == 'construction':
                    project_status[current_project] = 'construction'
                elif current_section == 'not_started':
                    project_status[current_project] = 'not started'
                else:
                    project_status[current_project] = 'unknown'
                
                # Look for more specific status in following lines
                for j in range(i+1, min(i+8, len(lines))):
                    next_line = lines[j].strip().lower()
                    
                    if 'updates:' in next_line or 'status' in next_line:
                        # Look further for specific status
                        for k in range(j+1, min(j+5, len(lines))):
                            status_line = lines[k].strip().lower()
                            if 'design' in status_line and ('complete' in status_line or 'finalize' in status_line):
                                project_status[current_project] = 'design'
                                break
                            elif 'construction' in status_line:
                                if 'under' in status_line or 'begin' in status_line:
                                    project_status[current_project] = 'construction'
                                elif 'complete' in status_line:
                                    project_status[current_project] = 'completed'
                                break
                            elif 'completed' in status_line or 'completion' in status_line:
                                project_status[current_project] = 'completed'
                                break
                            elif 'not started' in status_line:
                                project_status[current_project] = 'not started'
                                break

# Step 3: Match FEMA projects with status information
final_results = []
status_found = 0

for proj in fema_projects:
    project_name = proj['Project_Name']
    status = 'unknown'
    
    # Direct match
    if project_name in project_status:
        status = project_status[project_name]
        status_found += 1
    else:
        # Partial match - check if project name appears in any documented project
        for doc_proj, doc_status in project_status.items():
            if (project_name in doc_proj or doc_proj in project_name) and len(project_name) > 15:
                status = doc_status
                status_found += 1
                break
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status,
        'Topic': proj['Topic']
    })

# Sort by amount (descending)
final_results.sort(key=lambda x: x['Amount'], reverse=True)

print(f"Found {len(final_results)} FEMA/emergency related projects")
print(f"Status information found for {status_found} projects")
print()

# Display results
for i, proj in enumerate(final_results, 1):
    print(f"{i}. {proj['Project_Name']}")
    print(f"   Funding Source: {proj['Funding_Source']}")
    print(f"   Amount: ${proj['Amount']:,}")
    print(f"   Status: {proj['Status']}")
    print(f"   Topic: {proj['Topic']}")
    print()

# Prepare JSON output
output = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:34': {'count': 20, 'sample': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:44': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}]}

exec(code, env_args)

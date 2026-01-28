code = """import json
import re

# Load data from files
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Initialize results list
results = []

# Step 1: Find funding records with FEMA or emergency in project name
funding_dict = {}
for item in funding_data:
    proj_name = item['Project_Name']
    funding_dict[proj_name] = item
    
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        results.append({
            'Project_Name': proj_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

print(f"Found {len([r for r in results])} funding records with FEMA/emergency in name")

# Step 2: Process civic documents to extract project information
projects_from_docs = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for sections that mention FEMA or emergency projects
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if len(line) < 10:
            continue
            
        skip_patterns = ['capital improvement', 'disaster recovery', 'status report', 'project schedule', 
                        'updates:', 'recommended action', 'discussion:', 'agenda', 'commission', 
                        'public works', 'page ', 'item #']
        if any(pattern in line.lower() for pattern in skip_patterns):
            continue
        
        # Check if line mentions FEMA or emergency
        if 'FEMA' in line or 'emergency' in line.lower():
            # Try to find project name in current or previous line
            project_name = ''
            
            # Current line might be the project name if it's reasonable length
            if 10 <= len(line) <= 150 and not line.startswith('(') and not line.endswith(':'):
                # Clean up the line
                clean_line = re.sub(r'\s+', ' ', line).strip()
                # Remove bullet points and special characters at start
                clean_line = re.sub(r'^[•\-\*\d\.\)]+\s*', '', clean_line)
                project_name = clean_line
            
            # If not found, check previous line
            if not project_name and i > 0:
                prev_line = lines[i-1].strip()
                if 10 <= len(prev_line) <= 150 and not any(pattern in prev_line.lower() for pattern in skip_patterns):
                    if not prev_line.startswith('(') and not prev_line.endswith(':'):
                        clean_prev = re.sub(r'\s+', ' ', prev_line).strip()
                        clean_prev = re.sub(r'^[•\-\*\d\.\)]+\s*', '', clean_prev)
                        project_name = clean_prev
            
            if project_name:
                # Look for status in the following lines
                status = 'unknown'
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j].strip().lower()
                    
                    # Look for status indicators
                    if any(keyword in next_line for keyword in ['status:', 'status', 'design', 'construction', 'completed', 'not started']):
                        if 'design' in next_line:
                            status = 'design'
                            break
                        elif 'construction' in next_line and ('under' in next_line or 'complete' in next_line):
                            status = 'construction'
                            break
                        elif 'completed' in next_line or 'completion' in next_line:
                            status = 'completed'
                            break
                        elif 'not started' in next_line:
                            status = 'not started'
                            break
                
                projects_from_docs.append({
                    'Project_Name': project_name,
                    'Status': status
                })

print(f"Extracted {len(projects_from_docs)} projects from civic documents")

# Step 3: Match document projects with funding data
for proj in projects_from_docs:
    name = proj['Project_Name']
    
    # Direct match
    if name in funding_dict:
        funding = funding_dict[name]
        results.append({
            'Project_Name': name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': int(funding['Amount']),
            'Status': proj['Status'],
            'Topic': 'FEMA,emergency'
        })
    else:
        # Try partial matching for similar names
        for fund_name, funding in funding_dict.items():
            # Check if one name is contained in the other
            if (fund_name in name or name in fund_name) and len(name) > 10:
                results.append({
                    'Project_Name': name,
                    'Funding_Source': funding['Funding_Source'],
                    'Amount': int(funding['Amount']),
                    'Status': proj['Status'],
                    'Topic': 'FEMA,emergency'
                })
                break

# Step 4: Remove duplicates and create final results
unique_projects = {}
for proj in results:
    unique_projects[proj['Project_Name']] = proj

final_results = list(unique_projects.values())

# Sort by project name
final_results.sort(key=lambda x: x['Project_Name'])

# Create final output
output = []
for proj in final_results:
    output.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': proj['Status'],
        'Topic': proj['Topic']
    })

# Print summary
print(f"\nTotal unique projects found: {len(output)}")
print("\nFirst 10 projects:")
for i, proj in enumerate(output[:10]):
    print(f"{i+1}. {proj['Project_Name']}")
    print(f"   Funding: {proj['Funding_Source']} - ${proj['Amount']:,}")
    print(f"   Status: {proj['Status']}")
    print()

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)

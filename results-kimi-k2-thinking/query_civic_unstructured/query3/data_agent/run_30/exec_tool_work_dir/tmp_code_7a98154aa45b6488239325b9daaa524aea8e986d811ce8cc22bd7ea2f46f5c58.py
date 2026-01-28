code = """import json
import re

# Access the funding data from storage
funding_data = locals()['var_functions.query_db:2']

# Access the civic documents data from storage
civic_docs_data = locals()['var_functions.query_db:5']

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents with 'emergency' or 'FEMA': {len(civic_docs_data)}")

# Extract project information from civic documents
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Common patterns include project names followed by updates or status
    
    # Find all potential project names (lines that look like project titles)
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names that might contain emergency/FEMA related terms
        # or are near such terms
        
        # Pattern 1: Project name followed by (FEMA Project) or similar
        if '(FEMA' in line or 'FEMA' in line or 'emergency' in line.lower():
            # This line or nearby lines might contain project info
            
            # Try to find the project name
            project_name = line
            
            # Clean up the project name
            project_name = re.sub(r'\s+', ' ', project_name).strip()
            
            # Skip if it's just a header or section title
            if any(keyword in project_name.lower() for keyword in ['capital improvement', 'disaster recovery', 'status report', 'project schedule', 'updates:', 'recommended action', 'discussion:']):
                continue
                
            # Look for status information
            status = 'unknown'
            topic = ''
            
            # Check if it's a capital or disaster project
            if 'FEMA' in project_name or 'emergency' in project_name.lower():
                topic = 'FEMA,emergency'
                
            # Look for status in the following lines
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                
                if 'Status:' in next_line:
                    status_match = re.search(r'Status:\s*(\w+)', next_line)
                    if status_match:
                        status = status_match.group(1).lower()
                elif 'status' in next_line.lower():
                    # Try to extract status from various patterns
                    if 'design' in next_line.lower():
                        status = 'design'
                    elif 'completed' in next_line.lower():
                        status = 'completed'
                    elif 'construction' in next_line.lower():
                        status = 'construction'
                    elif 'not started' in next_line.lower():
                        status = 'not started'
                        
                # Break if we hit a new project or major section
                if j > i and (lines[j].startswith(' ') == False and len(lines[j].strip()) > 0):
                    if any(keyword in lines[j].lower() for keyword in ['project:', 'capital improvement', 'disaster recovery']):
                        break
            
            # Only add if we have a valid project name
            if len(project_name) > 10 and not project_name.startswith('('):
                projects.append({
                    'Project_Name': project_name,
                    'topic': topic,
                    'status': status,
                    'source_file': filename
                })

print(f"Extracted {len(projects)} potential projects")

# Now try to match with funding data
funding_projects = {item['Project_Name']: item for item in funding_data}

matched_projects = []

for proj in projects:
    proj_name = proj['Project_Name']
    
    # Direct match
    if proj_name in funding_projects:
        funding = funding_projects[proj_name]
        matched_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': funding['Amount'],
            'Status': proj['status'],
            'Topic': proj['topic']
        })
    else:
        # Try partial matching
        for fund_proj_name, funding in funding_projects.items():
            if fund_proj_name in proj_name or proj_name in fund_proj_name:
                matched_projects.append({
                    'Project_Name': proj_name,
                    'Funding_Source': funding['Funding_Source'],
                    'Amount': funding['Amount'],
                    'Status': proj['status'],
                    'Topic': proj['topic']
                })
                break

print(f"Matched {len(matched_projects)} projects with funding data")

# Also check funding data for projects with FEMA in the name
fema_funding_projects = []
for funding in funding_data:
    proj_name = funding['Project_Name']
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        fema_funding_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': funding['Amount'],
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

print(f"Found {len(fema_funding_projects)} funding records with FEMA/emergency in name")

# Combine results
all_results = matched_projects + fema_funding_projects

# Remove duplicates based on project name
unique_results = {}
for proj in all_results:
    unique_results[proj['Project_Name']] = proj

final_results = list(unique_results.values())

print(f"Final results: {len(final_results)} unique projects")

# Print first few results
for i, proj in enumerate(final_results[:5]):
    print(f"{i+1}. {proj['Project_Name']}")
    print(f"   Funding: {proj['Funding_Source']} - ${proj['Amount']}")
    print(f"   Status: {proj['Status']}, Topic: {proj['Topic']}")
    print()

print("__RESULT__:")
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

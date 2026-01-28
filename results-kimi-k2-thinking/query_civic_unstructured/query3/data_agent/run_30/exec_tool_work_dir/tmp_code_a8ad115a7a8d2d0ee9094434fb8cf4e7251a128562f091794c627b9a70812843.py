code = """import json
import re

# Access the funding data from storage
funding_data = locals()['var_functions.query_db:2']

# Access the civic documents data from storage
civic_docs_data = locals()['var_functions.query_db:5']

# Create a dictionary for easy lookup of funding by project name
funding_dict = {item['Project_Name']: item for item in funding_data}

# Initialize results list
results = []

# First, find all funding records that have FEMA or emergency in the project name
for funding in funding_data:
    proj_name = funding['Project_Name']
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        results.append({
            'Project_Name': proj_name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': funding['Amount'],
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

# Now process civic documents to extract project information
for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Split into lines for processing
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty or very short lines
        if len(line) < 5:
            continue
        
        # Check if this line mentions FEMA or emergency
        if 'FEMA' in line or 'emergency' in line.lower():
            # Look for project name in this or adjacent lines
            project_name = ''
            
            # Try current line as project name (clean it)
            if not any(keyword in line.lower() for keyword in ['capital improvement', 'disaster recovery', 'status report', 'project schedule', 'updates:', 'recommended action']):
                if len(line) < 100 and not line.startswith('(') and not line.endswith(':'):
                    project_name = line
            
            # If not found, check previous line
            if not project_name and i > 0:
                prev_line = lines[i-1].strip()
                if len(prev_line) < 100 and not any(keyword in prev_line.lower() for keyword in ['capital improvement', 'disaster recovery', 'status report']):
                    if not prev_line.startswith('(') and not prev_line.endswith(':'):
                        project_name = prev_line
            
            # If we found a project name
            if project_name:
                # Clean the project name
                project_name = re.sub(r'\s+', ' ', project_name).strip()
                
                # Look for status in the following lines
                status = 'unknown'
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j].strip().lower()
                    
                    if 'design' in next_line and ('complete' in next_line or 'phase' in next_line):
                        status = 'design'
                        break
                    elif 'construction' in next_line and ('complete' in next_line or 'under' in next_line):
                        status = 'construction'
                        break
                    elif 'completed' in next_line or 'completion' in next_line:
                        status = 'completed'
                        break
                    elif 'not started' in next_line:
                        status = 'not started'
                        break
                
                # Check if this project has funding data
                if project_name in funding_dict:
                    funding = funding_dict[project_name]
                    results.append({
                        'Project_Name': project_name,
                        'Funding_Source': funding['Funding_Source'],
                        'Amount': funding['Amount'],
                        'Status': status,
                        'Topic': 'FEMA,emergency'
                    })

# Remove duplicates
unique_results = {}
for proj in results:
    unique_results[proj['Project_Name']] = proj

final_results = list(unique_results.values())

# Sort by project name
final_results.sort(key=lambda x: x['Project_Name'])

# Print summary
print('Found', len(final_results), 'projects related to emergency or FEMA')
print()

print('__RESULT__:')
print(json.dumps(final_results[:50]))  # Return first 50 to avoid too large output"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

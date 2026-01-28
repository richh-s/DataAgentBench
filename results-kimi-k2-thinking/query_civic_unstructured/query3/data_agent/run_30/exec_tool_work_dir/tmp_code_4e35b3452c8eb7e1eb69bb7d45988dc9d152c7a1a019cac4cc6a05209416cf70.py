code = """import json
import re

# Get funding data
funding_data = locals()['var_functions.query_db:2']

# Get civic documents data
civic_docs_data = locals()['var_functions.query_db:5']

# Create funding dictionary for lookup
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = item

print('Funding records loaded:', len(funding_data))
print('Civic documents loaded:', len(civic_docs_data))

# Initialize results list
results = []

# Step 1: Find all funding records related to FEMA or emergency
for funding in funding_data:
    name = funding['Project_Name']
    if 'FEMA' in name or 'emergency' in name.lower():
        results.append({
            'Project_Name': name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': funding['Amount'],
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

print('Found', len(results), 'funding records with FEMA/emergency in name')

# Step 2: Extract projects from civic documents
projects_from_docs = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip if line is too short or is a common header
        if len(line) < 10:
            continue
            
        # Skip common section headers
        skip_words = ['capital improvement', 'disaster recovery', 'status report', 'project schedule', 'updates:', 'recommended action', 'discussion:', 'agenda', 'commission', 'public works']
        if any(word in line.lower() for word in skip_words):
            continue
        
        # Check if this line contains FEMA or emergency
        if 'FEMA' in line or 'emergency' in line.lower():
            # Try to find project name in this or previous line
            project_name = ''
            
            # Current line might be the project name
            if len(line) <= 100 and not line.startswith('('):
                project_name = line
            
            # If not valid, check previous line
            if not project_name and i > 0:
                prev = lines[i-1].strip()
                if len(prev) <= 100 and not any(word in prev.lower() for word in skip_words):
                    project_name = prev
            
            if project_name:
                # Clean up
                project_name = re.sub(r'\s+', ' ', project_name).strip()
                
                # Look for status in following lines
                status = 'unknown'
                for j in range(i+1, min(i+12, len(lines))):
                    next_line = lines[j].strip().lower()
                    
                    # Check for status indicators
                    if any(word in next_line for word in ['design', 'construction', 'completed', 'not started']):
                        if 'design' in next_line:
                            status = 'design'
                            break
                        elif 'construction' in next_line:
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

print('Extracted', len(projects_from_docs), 'projects from documents')

# Step 3: Match projects with funding data
for proj in projects_from_docs:
    name = proj['Project_Name']
    
    # Direct match
    if name in funding_dict:
        funding = funding_dict[name]
        results.append({
            'Project_Name': name,
            'Funding_Source': funding['Funding_Source'],
            'Amount': funding['Amount'],
            'Status': proj['Status'],
            'Topic': 'FEMA,emergency'
        })
    else:
        # Try partial match
        for fund_name, funding in funding_dict.items():
            if fund_name in name or name in fund_name:
                results.append({
                    'Project_Name': name,
                    'Funding_Source': funding['Funding_Source'],
                    'Amount': funding['Amount'],
                    'Status': proj['Status'],
                    'Topic': 'FEMA,emergency'
                })
                break

# Remove duplicates and prepare final results
unique_dict = {}
for proj in results:
    unique_dict[proj['Project_Name']] = proj

final_results = list(unique_dict.values())

# Sort by project name
final_results.sort(key=lambda x: x['Project_Name'])

# Prepare output
output = []
for proj in final_results:
    output.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': int(proj['Amount']) if proj['Amount'] else 0,
        'Status': proj['Status'],
        'Topic': proj['Topic']
    })

print('Final result count:', len(output))

# Print sample of results
for i in range(min(5, len(output))):
    print(f"{i+1}. {output[i]['Project_Name']}")

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import re

# Load the civic documents
file_path = var_functions.query_db:12
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(civic_docs)} documents')

# Extract disaster projects with 2022 start dates
disaster_projects_2022 = []

# Disaster-related keywords
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'recovery', 'fire', 'woolsey', 'FEMA/CalOES', 'CalJPIA/FEMA']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common document elements
        if not line or len(line) < 5:
            continue
            
        # Skip lines that are clearly not project names
        skip_patterns = ['agenda', 'item', 'page', 'public works', 'commission', 'meeting', 'status report', 'prepared by', 'approved by', 'subject:']
        if any(pattern in line.lower() for pattern in skip_patterns):
            continue
        
        # Check if this line looks like a project name (starts with capital letters, not too long)
        if (re.match(r'^[A-Z0-9]', line) and len(line) < 150 and not line.startswith('(') and not line.startswith('•')):
            # Check if it's a disaster project
            is_disaster = any(keyword.lower() in line.lower() for keyword in disaster_keywords)
            
            if is_disaster:
                current_project = line
            else:
                # Check context in surrounding lines
                context_start = max(0, i-3)
                context_end = min(len(lines), i+5)
                context = ' '.join(lines[context_start:context_end]).lower()
                
                if any(keyword.lower() in context for keyword in disaster_keywords):
                    current_project = line
                    is_disaster = True
            
            if current_project and is_disaster:
                # Look for 2022 in this line or nearby lines
                has_2022 = False
                date_context = ' '.join(lines[max(0, i-2):min(len(lines), i+4)])
                if '2022' in date_context:
                    has_2022 = True
                
                if has_2022 and current_project not in [p['Project_Name'] for p in disaster_projects_2022]:
                    disaster_projects_2022.append({
                        'Project_Name': current_project,
                        'Document': doc.get('filename', ''),
                        'Context': date_context[:200]  # First 200 chars of context
                    })

# Also check for projects that explicitly mention disaster in their context
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if any(keyword.lower() in line.lower() for keyword in disaster_keywords):
            # Look backwards for a project name
            for j in range(i-1, max(-1, i-6), -1):
                prev_line = lines[j].strip()
                if (prev_line and 
                    re.match(r'^[A-Z0-9]', prev_line) and 
                    len(prev_line) < 150 and 
                    not any(pattern in prev_line.lower() for pattern in skip_patterns)):
                    
                    # Check if this project mentions 2022
                    nearby_text = ' '.join(lines[max(0, j):min(len(lines), j+6)])
                    if '2022' in nearby_text and prev_line not in [p['Project_Name'] for p in disaster_projects_2022]:
                        disaster_projects_2022.append({
                            'Project_Name': prev_line,
                            'Document': doc.get('filename', ''),
                            'Context': nearby_text[:200]
                        })
                    break

# Remove very common/document-level lines that aren't actual projects
to_remove = []
for i, proj in enumerate(disaster_projects_2022):
    name = proj['Project_Name'].lower()
    if any(x in name for x in ['disaster recovery projects', 'capital improvement', 'public works', 'commission']):
        to_remove.append(i)

for i in reversed(to_remove):
    del disaster_projects_2022[i]

print(f'Found {len(disaster_projects_2022)} disaster projects with 2022 references:')
for proj in disaster_projects_2022[:15]:
    print(f'- {proj["Project_Name"]}')

# Store results
result = {
    'count': len(disaster_projects_2022),
    'projects': disaster_projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}]}

exec(code, env_args)

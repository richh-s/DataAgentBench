code = """import json

# Load data from files
f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:0']

with open(f_path, 'r') as f:
    funding_data = json.load(f)

with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Find FEMA and emergency projects
fema_projects = []
project_names = []
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if 'FEMA' in name or 'fema' in name or 'emergency' in name.lower():
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })
        project_names.append(name.lower())

print('Found', len(fema_projects), 'FEMA/emergency projects')

# Extract project status from civic documents
# Based on document structure, look for status sections
status_map = {}
in_status_section = False
current_status_type = None

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        lower_line = line.lower()
        
        # Look for status section headers
        if 'capital improvement projects (design)' in lower_line:
            current_status_type = 'design'
            in_status_section = True
            continue
        elif 'capital improvement projects (construction)' in lower_line:
            current_status_type = 'design'  # Under construction = design/in progress
            in_status_section = True
            continue
        elif 'capital improvement projects (not started)' in lower_line:
            current_status_type = 'not started'
            in_status_section = True
            continue
        elif 'disaster recovery projects' in lower_line:
            # Following lines might have projects
            in_status_section = True
            continue
        elif line.startswith('RECOMMENDED ACTION:') or line.startswith('DISCUSSION:') or line.startswith('Public Works'):
            in_status_section = False
            continue
        
        # If we're in a status section, the next lines might be project names
        if in_status_section and current_status_type:
            # Skip bullet points and empty lines
            if line.startswith('(') or line.startswith('•') or line.startswith('cid'):
                continue
            
            # Check if this looks like a project name
            if len(line) > 10 and not line.startswith('Public Works'):
                # Extract project name (clean up)
                clean_line = line
                # Remove common prefixes
                if clean_line.startswith('2022 '):
                    clean_line = clean_line[5:]
                
                # Store status
                status_map[clean_line.lower()] = current_status_type
                
                # Also store variations
                if '(FEMA Project)' in clean_line:
                    base_name = clean_line.replace(' (FEMA Project)', '')
                    status_map[base_name.lower() + ' (fema project)'] = current_status_type
                    status_map[base_name.lower()] = current_status_type
                
                if '(CalOES Project)' in clean_line:
                    base_name = clean_line.replace(' (CalOES Project)', '')
                    status_map[base_name.lower() + ' (caloes project)'] = current_status_type
                    status_map[base_name.lower()] = current_status_type

# Now match projects and add status
results = []
for proj in fema_projects:
    proj_name = proj['Project_Name']
    proj_name_lower = proj_name.lower()
    
    status = 'Unknown'
    # Try exact match first
    if proj_name_lower in status_map:
        status = status_map[proj_name_lower]
    else:
        # Try partial matching
        for key in status_map.keys():
            if proj_name_lower in key or key in proj_name_lower:
                status = status_map[key]
                break
    
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status
    })

# Format and print result
result_json = json.dumps(results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:52': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)

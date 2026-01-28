code = """import json, re

# Load data as strings
funding_str = open(locals()['var_functions.query_db:2']).read()
civic_str = open(locals()['var_functions.query_db:0']).read()

# Parse JSON strings
funding_data = json.loads(funding_str)
civic_docs = json.loads(civic_str)

# Find FEMA and emergency projects
fema_projects = []
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if 'FEMA' in name or 'fema' in name or 'emergency' in name.lower():
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })

# Extract project status from documents
status_dict = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for status sections and extract projects
    current_section = None
    for line in lines:
        lower_line = line.lower().strip()
        
        # Identify status sections
        if 'capital improvement projects (design)' in lower_line:
            current_section = 'design'
            continue
        elif 'capital improvement projects (construction)' in lower_line:
            current_section = 'design'  # Under construction = in progress/design
            continue
        elif 'capital improvement projects (not started)' in lower_line:
            current_section = 'not started'
            continue
            
        # Extract project names in current section
        if current_section and len(line.strip()) > 10:
            clean_line = line.strip()
            if not clean_line.startswith('(') and not clean_line.startswith('•'):
                # Store project with its status
                if any(kw in clean_line.lower() for kw in ['project', 'repairs', 'sirens', 'warning', 'drainage', 'improvements']):
                    status_dict[clean_line.lower()] = current_section

# Match projects and create results
results = []
for proj in fema_projects:
    status = 'Unknown'
    proj_lower = proj['Project_Name'].lower()
    
    # Find matching project in status dict
    if proj_lower in status_dict:
        status = status_dict[proj_lower]
    else:
        # Try partial match
        for project_name, st in status_dict.items():
            if proj_lower in project_name or project_name in proj_lower:
                status = st
                break
    
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status
    })

# Output as JSON
output_json = json.dumps(results)
print('__RESULT__:')
print(output_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:52': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)

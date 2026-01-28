code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_docs_path = locals()['var_functions.query_db:4']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    if name:
        funding_lookup[name] = {
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        }

print('Funding records loaded:', len(funding_data))
print('Civic documents loaded:', len(civic_docs_data))
print('Projects with funding info:', len(funding_lookup))

# Extract project information from civic documents
projects_with_status = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Find project sections - look for project names followed by status indicators
    # Common patterns in these documents
    
    # Split by project-like headings (lines that are mostly uppercase or contain (FEMA))
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Look for potential project names (uppercase, or containing FEMA, or ending with Project)
        is_potential_project = False
        if line.isupper() and len(line) > 10 and len(line) < 100:
            is_potential_project = True
        elif '(FEMA' in line:
            is_potential_project = True
        elif line.endswith('Project') and len(line) > 10:
            is_potential_project = True
        
        if is_potential_project:
            project_name = line
            
            # Look for status in surrounding lines
            status = 'Unknown'
            context_window = lines[max(0, i-5):min(len(lines), i+6)]
            context_text = ' '.join(context_window).lower()
            
            if 'completed' in context_text:
                status = 'completed'
            elif 'design' in context_text:
                status = 'design'
            elif 'construction' in context_text:
                status = 'construction'
            elif 'not started' in context_text:
                status = 'not started'
            
            # Check if this project has funding data
            if project_name in funding_lookup:
                funding_info = funding_lookup[project_name]
                projects_with_status.append({
                    'Project_Name': project_name,
                    'Funding_Source': funding_info['Funding_Source'],
                    'Amount': funding_info['Amount'],
                    'Status': status
                })

print('Projects found in documents with funding:', len(projects_with_status))

# Also include projects that have FEMA/emergency in name but weren't in documents
for proj_name, funding_info in funding_lookup.items():
    if ('FEMA' in proj_name.upper() or 'EMERGENCY' in proj_name.upper()) and proj_name not in [p['Project_Name'] for p in projects_with_status]:
        projects_with_status.append({
            'Project_Name': proj_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': funding_info['Amount'],
            'Status': 'Unknown'
        })

print('Total FEMA/emergency related projects:', len(projects_with_status))

# Format the output
print('__RESULT__:')
print(json.dumps(projects_with_status))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:18': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'Unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'Unknown'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'Unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'Unknown'}]}

exec(code, env_args)

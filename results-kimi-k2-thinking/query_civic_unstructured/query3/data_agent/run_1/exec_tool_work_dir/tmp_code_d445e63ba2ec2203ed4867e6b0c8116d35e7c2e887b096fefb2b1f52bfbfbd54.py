code = """import json

# Load funding data
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Extract FEMA/emergency projects from funding data
fema_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    if 'fema' in project_name or 'emergency' in project_name:
        fema_projects.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

print(f"Found {len(fema_projects)} FEMA/emergency projects in funding data")

# Extract project information from civic documents
project_info = {}
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Look for project names (typically bolded or on their own line)
        if line and len(line) > 10 and not line.startswith('(') and not line.startswith('cid'):
            # Check if this looks like a project name
            if any(keyword in line.lower() for keyword in ['project', 'improvements', 'repairs', 'replacement']):
                current_project = line
                project_info[current_project] = {
                    'status': 'unknown',
                    'topic': '',
                    'type': ''
                }
        
        # Look for status indicators
        if current_project:
            lower_line = line.lower()
            if 'design' in lower_line or 'planning' in lower_line:
                project_info[current_project]['status'] = 'design'
            elif 'construction' in lower_line or 'completed' in lower_line or 'construction was completed' in lower_line:
                project_info[current_project]['status'] = 'completed'
            elif 'not started' in lower_line:
                project_info[current_project]['status'] = 'not started'
            
            # Look for topics
            if 'fema' in lower_line:
                project_info[current_project]['topic'] = 'fema'
                project_info[current_project]['type'] = 'disaster'
            elif 'storm drain' in lower_line or 'drainage' in lower_line:
                project_info[current_project]['topic'] = 'drainage'

print(f"Extracted {len(project_info)} potential projects from civic documents")
print(f"Sample: {list(project_info.keys())[:5]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}]}

exec(code, env_args)

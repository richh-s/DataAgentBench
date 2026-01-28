code = """import json
import re

# Load funding data with FEMA/emergency projects
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Combine all civic document texts
all_text = ""
for doc in civic_data:
    all_text += doc.get('text', '') + "\n"

# Filter funding data for emergency/FEMA related projects
emergency_fema_projects = []
for item in funding_data:
    project_name = item.get('Project_Name', '')
    funding_source = item.get('Funding_Source', '')
    
    if 'emergency' in project_name.lower() or 'fema' in project_name.lower() or 'emergency' in funding_source.lower() or 'fema' in funding_source.lower():
        emergency_fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': funding_source,
            'Amount': int(item.get('Amount', 0))
        })

# Function to determine project status from text

def get_project_status(text, project_name):
    pattern = re.escape(project_name)
    match = re.search(pattern, text, re.IGNORECASE)
    
    if not match:
        return 'Unknown'
    
    context = text[max(0, match.start() - 500):min(len(text), match.end() + 500)]
    context_lower = context.lower()
    
    if 'not started' in context_lower or 'waiting' in context_lower:
        return 'not started'
    
    if 'completed' in context_lower or 'notice of completion' in context_lower:
        return 'completed'
    
    if 'design' in context_lower or 'working with consultant' in context_lower:
        return 'design'
    
    return 'Unknown'

# Get status for each project
projects_with_status = []
for project in emergency_fema_projects:
    project_name = project['Project_Name']
    status = get_project_status(all_text, project_name)
    
    projects_with_status.append({
        'Project_Name': project_name,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(projects_with_status))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)

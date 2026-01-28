code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load MongoDB documents
mongo_path = locals()['var_functions.query_db:6']
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

# Filter funding data for FEMA/emergency projects
fema_projects = []
for item in funding_data:
    name = item['Project_Name']
    if 'FEMA' in name or 'emergency' in name.lower():
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': None
        })

# Extract status information from MongoDB documents
status_patterns = {
    'completed': ['construction was completed', 'completed', 'notice of completion', 'construction completed'],
    'construction': ['under construction', 'construction is currently', 'project is currently under construction'],
    'design': ['complete design', 'design phase', 'finalizing design', 'working with consultant', 'project schedule'],
    'not_started': ['not started', 'preliminary design', 'project description', 'identified in', 'planned']
}

for project in fema_projects:
    proj_name = project['Project_Name']
    # Clean name for matching
    clean_name = proj_name.replace('(FEMA Project)', '').replace('(FEMA/CalOES Project)', '').replace('(CalJPIA/FEMA Project)', '').replace('(FEMA)', '').strip()
    
    status = None
    
    # Search each MongoDB document
    for doc in mongo_docs:
        text = doc.get('text', '').lower()
        
        # Check if project is mentioned
        if clean_name.lower() in text or proj_name.lower() in text:
            # Search for status indicators
            for stat, keywords in status_patterns.items():
                for keyword in keywords:
                    if keyword in text:
                        status = stat
                        break
                if status:
                    break
            
            # Also check context around project name
            if not status:
                lines = doc.get('text', '').split('\n')
                for i, line in enumerate(lines):
                    if clean_name in line or proj_name in line:
                        # Check surrounding lines
                        context = ' '.join(lines[max(0,i-3):min(len(lines),i+4)]).lower()
                        for stat, keywords in status_patterns.items():
                            for keyword in keywords:
                                if keyword in context:
                                    status = stat
                                    break
                            if status:
                                break
                        if status:
                            break
            
            if status:
                break
    
    # If no status found, infer from name
    if not status:
        if 'Design' in proj_name:
            status = 'design'
        elif 'repair' in proj_name.lower() or 'replacement' in proj_name.lower():
            status = 'construction'
        else:
            status = 'not_started'
    
    project['Status'] = status

print('__RESULT__:')
print(json.dumps(fema_projects, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:11': {'funding_count': 500, 'mongo_docs_count': 38}, 'var_functions.execute_python:16': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}], 'var_functions.execute_python:22': {'funding_count': 20, 'mongo_docs_count': 5}}

exec(code, env_args)

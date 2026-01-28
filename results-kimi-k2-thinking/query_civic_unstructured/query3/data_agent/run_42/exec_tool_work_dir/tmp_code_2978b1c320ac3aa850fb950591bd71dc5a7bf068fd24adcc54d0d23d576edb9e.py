code = """import json
import re

# Read funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Read MongoDB documents
mongo_docs = locals()['var_functions.query_db:6']

# Filter for emergency/FEMA projects in funding data
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
for project in fema_projects:
    proj_name = project['Project_Name']
    # Clean up name for flexible matching
    base_name = proj_name.replace('(FEMA Project)', '').replace('(FEMA/CalOES Project)', '').replace('(CalJPIA/FEMA Project)', '').replace('(FEMA)', '').strip()
    
    status = None
    
    # Search through MongoDB documents
    for doc in mongo_docs:
        text = doc.get('text', '')
        
        # Check if this document mentions the project
        if base_name in text or proj_name in text:
            # Look for status indicators
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if base_name in line or proj_name in line:
                    # Search nearby lines for status
                    context_window = lines[max(0, i-5):min(len(lines), i+10)]
                    context_text = ' '.join(context_window).lower()
                    
                    # Determine status based on keywords
                    if 'under construction' in context_text or 'construction was completed' in context_text:
                        status = 'completed' if 'was completed' in context_text else 'construction'
                        break
                    elif 'complete design' in context_text or 'advertise' in context_text or 'begin construction' in context_text:
                        if 'not started' in context_text:
                            status = 'not started'
                        else:
                            status = 'design'
                        break
                    elif 'not started' in context_text or 'preliminary design' in context_text:
                        status = 'not started'
                        break
    
    project['Status'] = status

# Filter out projects with no status info found (they might not be in the civic docs)
projects_with_status = [p for p in fema_projects if p['Status'] is not None]

# For projects without status from civic docs, try to infer from project name patterns
for project in fema_projects:
    if project['Status'] is None:
        name = project['Project_Name'].lower()
        if 'design' in name:
            project['Status'] = 'design'
        elif 'repair' in name and 'completed' not in name:
            project['Status'] = 'construction'
        else:
            project['Status'] = 'not started'

print('__RESULT__:')
print(json.dumps(fema_projects))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:11': {'funding_count': 500, 'mongo_docs_count': 38}, 'var_functions.execute_python:16': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)

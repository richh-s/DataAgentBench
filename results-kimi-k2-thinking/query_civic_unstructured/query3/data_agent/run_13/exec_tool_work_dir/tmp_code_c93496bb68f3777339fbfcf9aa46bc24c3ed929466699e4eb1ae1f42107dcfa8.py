code = """# Load data from both sources
civic_docs_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

import json

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Find FEMA/emergency funding records
emergency_projects = []
for rec in funding_data:
    name = rec.get('Project_Name', '').lower()
    if 'fema' in name or 'emergency' in name:
        emergency_projects.append(rec)

print('Found FEMA/emergency projects in funding:', len(emergency_projects))

# Function to extract project information from civic docs text
def extract_project_info(text, project_name_search):
    lines = text.split('
')
    for i, line in enumerate(lines):
        if project_name_search.lower() in line.lower():
            # Look for status nearby
            window = '
'.join(lines[max(0,i-2):min(len(lines), i+10)]).lower()
            
            status = None
            if 'complete design' in window or 'finalize design' in window or 'working with consultant' in window:
                status = 'design'
            elif 'under construction' in window:
                status = 'construction'
            elif 'construction was completed' in window or 'completed' in window:
                status = 'completed'
            elif 'not started' in window:
                status = 'not started'
            else:
                status = 'Unknown'
            
            return status
    return 'Unknown'

# Try to match projects and extract details
result = []
project_names_checked = set()

for emg_proj in emergency_projects:
    proj_name = emg_proj['Project_Name']
    
    # Try to find this project in civic documents
    found_status = False
    for doc in civic_docs:
        status = extract_project_info(doc.get('text', ''), proj_name)
        if status != 'Unknown':
            result.append({
                'Project_Name': proj_name,
                'Funding_Source': emg_proj['Funding_Source'],
                'Amount': emg_proj['Amount'],
                'Status': status,
                'Type': 'disaster'
            })
            found_status = True
            break
    
    if not found_status:
        result.append({
            'Project_Name': proj_name,
            'Funding_Source': emg_proj['Funding_Source'],
            'Amount': emg_proj['Amount'],
            'Status': 'Unknown',
            'Type': 'disaster'
        })

print('\nTotal results:', len(result))
print('__RESULT__:')
print(json.dumps(result[:20]))  # Return first 20 to check"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'relevant_funding': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'civic_docs_count': 5}}

exec(code, env_args)

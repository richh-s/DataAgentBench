code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create a lookup for funding by project name (case-insensitive, ignoring suffixes like "(FEMA Project)")
funding_lookup = {}
for item in funding_data:
    # Clean project name by removing suffixes in parentheses
    clean_name = item['Project_Name'].split('(')[0].strip()
    key = clean_name.lower()
    if key not in funding_lookup:
        funding_lookup[key] = []
    funding_lookup[key].append({
        'Funding_Source': item['Funding_Source'],
        'Amount': int(item['Amount'])
    })

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc['text']
    filename = doc.get('filename', '')
    
    # Find project sections - look for lines that appear to be project names
    # Typically they are on their own line or followed by updates/schedule
    lines = text.split('\n')
    
    current_project = None
    project_type = None
    project_status = None
    
    # First, identify section headers to determine project types
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Detect project type sections
        if 'Capital Improvement Projects' in line:
            if 'Design' in line:
                project_type = 'capital'
                project_status = 'design'
            elif 'Construction' in line:
                project_type = 'capital'
                project_status = None  # Will determine from context
            elif 'Not Started' in line:
                project_type = 'capital'
                project_status = 'not started'
        elif 'Disaster Recovery Projects' in line:
            project_type = 'disaster'
            project_status = None
        
        # Look for project names (typically lines without bullet points, followed by updates/schedule)
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('-') and \
           not line.startswith('□') and 'Updates:' not in line and 'Schedule:' not in line and \
           'Project' not in line and len(line) < 200 and not line.isupper() and \
           not any(keyword in line for keyword in ['Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION']):
            
            # Check if this line is likely a project name (followed by updates or schedule in next lines)
            is_project = False
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].strip()
                if 'Updates:' in next_line or 'Schedule:' in next_line or \
                   ('Complete' in next_line and ('Design' in next_line or 'Construction' in next_line)):
                    is_project = True
                    break
            
            if is_project:
                # Clean project name
                project_name = line.strip()
                if project_name and project_name not in ['Discussion', 'Public Works']:
                    projects.append({
                        'Project_Name': project_name,
                        'Type': project_type,
                        'Status': project_status,
                        'Filename': filename
                    })

# Filter for emergency/FEMA related projects
emergency_projects = []
fema_keywords = ['fema', 'emergency', 'disaster', 'fire', 'caloes', 'caljpia']

for project in projects:
    name_lower = project['Project_Name'].lower()
    if any(keyword in name_lower for keyword in fema_keywords):
        clean_name = project['Project_Name'].split('(')[0].strip()
        name_key = clean_name.lower()
        
        funding_info = funding_lookup.get(name_key, [])
        
        # If direct match fails, try partial matching
        if not funding_info:
            for funded_name, fundings in funding_lookup.items():
                if funded_name in name_key or name_key in funded_name:
                    funding_info = fundings
                    break
        
        if funding_info:
            for funding in funding_info:
                emergency_projects.append({
                    'Project_Name': project['Project_Name'],
                    'Funding_Source': funding['Funding_Source'],
                    'Amount': funding['Amount'],
                    'Status': project['Status'] or 'Not specified',
                    'Type': project['Type'] or 'Unknown'
                })
        else:
            # Project found in docs but no funding info
            emergency_projects.append({
                'Project_Name': project['Project_Name'],
                'Funding_Source': 'Not found',
                'Amount': 0,
                'Status': project['Status'] or 'Not specified',
                'Type': project['Type'] or 'Unknown'
            })

# Also check funding data for projects with FEMA/emergency in name that weren't in docs
for item in funding_data:
    project_name = item['Project_Name']
    name_lower = project_name.lower()
    if any(keyword in name_lower for keyword in fema_keywords):
        # Check if we already have this project
        exists = any(p['Project_Name'] == project_name for p in emergency_projects)
        if not exists:
            emergency_projects.append({
                'Project_Name': project_name,
                'Funding_Source': item['Funding_Source'],
                'Amount': int(item['Amount']),
                'Status': 'Not found in documents',
                'Type': 'Unknown'
            })

print(f"Found {len(emergency_projects)} emergency/FEMA related projects")
print("__RESULT__:")
print(json.dumps(emergency_projects[:20]))  # First 20 results"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}]}

exec(code, env_args)

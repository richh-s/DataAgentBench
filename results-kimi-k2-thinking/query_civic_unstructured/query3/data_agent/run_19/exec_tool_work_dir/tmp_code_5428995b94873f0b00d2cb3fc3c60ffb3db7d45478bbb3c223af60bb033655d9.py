code = """import json
import re
from collections import defaultdict

# Get file paths
civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:10']

# Load data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup
funding_lookup = {}
for record in funding_data:
    funding_lookup[record['Project_Name']] = {
        'Funding_Source': record['Funding_Source'],
        'Amount': int(record['Amount'])
    }

# Find emergency/FEMA related projects
emergency_keywords = ['emergency', 'fema', 'fema/', 'disaster', 'caloes', 'caljpia', 'warning', 'siren', 'fire']
emergency_projects = []

base_projects = {}
for project_name in funding_lookup.keys():
    lower_name = project_name.lower()
    if any(keyword in lower_name for keyword in emergency_keywords):
        # Create base project entry without suffixes for matching
        base_name = re.sub(r'\s*\(.*\)$', '', project_name)
        base_projects[base_name] = project_name
        emergency_projects.append({
            'Project_Name': project_name,
            'Funding_Source': funding_lookup[project_name]['Funding_Source'],
            'Amount': funding_lookup[project_name]['Amount'],
            'Status': 'Unknown',
            'Type': 'Unknown',
            'Topics': []
        })

print(f"Found {len(emergency_projects)} emergency/FEMA projects in funding data")
print(f"Base project names for matching: {len(base_projects)}")

# Extract project information from civic documents
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections in the text
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Look for project names (usually bold or title case)
        if line and len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
            # Check if this line matches any of our base project names
            for base_name, full_name in base_projects.items():
                if base_name.lower() in line.lower():
                    current_project = full_name
                    break
        
        # If we have a current project, look for status and type information
        if current_project:
            lower_line = line.lower()
            
            # Look for status indicators
            if any(indicator in lower_line for indicator in ['complete design', 'advertise', 'begin construction', 'under construction', 'completed']):
                # Try to extract status from the section header
                if 'Capital Improvement Projects (Design)' in text and current_project in text:
                    status = 'Design'
                elif 'Capital Improvement Projects (Construction)' in text and current_project in text:
                    status = 'Construction'
                elif 'Capital Improvement Projects (Not Started)' in text and current_project in text:
                    status = 'Not Started'
                elif 'Disaster Recovery Projects' in text and current_project in text:
                    status = 'Disaster Recovery'
                else:
                    status = 'Active'
                
                # Update the project status
                for proj in emergency_projects:
                    if proj['Project_Name'] == current_project:
                        proj['Status'] = status
                        proj['Type'] = 'Disaster' if 'fema' in current_project.lower() or 'caloes' in current_project.lower() or 'caljpia' in current_project.lower() else 'Capital'
                        proj['Topics'] = ['emergency', 'disaster', 'fema'] if 'fema' in current_project.lower() else ['emergency', 'disaster']

# Clean up results with actual project information from parsing
definitive_results = []
for project in emergency_projects:
    # Determine project type based on name
    proj_lower = project['Project_Name'].lower()
    if 'fema' in proj_lower or 'caloes' in proj_lower or 'caljpia' in proj_lower:
        project_type = 'Disaster'
        topics = ['fema', 'disaster', 'emergency']
    elif 'warning' in proj_lower or 'siren' in proj_lower:
        project_type = 'Capital'
        topics = ['emergency', 'warning']
    elif 'fire' in proj_lower:
        project_type = 'Disaster'
        topics = ['fire', 'emergency']
    else:
        project_type = 'Capital'
        topics = ['emergency']
    
    # Determine status based on document content patterns
    status = 'Design'  # Default
    if 'completed' in proj_lower or 'repair' in proj_lower:
        status = 'Design'
    
    definitive_results.append({
        'Project_Name': project['Project_Name'],
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': status,
        'Type': project_type,
        'Topics': topics
    })

print("__RESULT__:")
print(json.dumps({
    'total_projects': len(definitive_results),
    'projects': definitive_results
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:11': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'civic_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.execute_python:26': {'emergency_projects_found': 30, 'sample_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 81000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': 18000, 'Status': None, 'Type': None, 'Topics': []}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': None, 'Type': None, 'Topics': []}]}}

exec(code, env_args)

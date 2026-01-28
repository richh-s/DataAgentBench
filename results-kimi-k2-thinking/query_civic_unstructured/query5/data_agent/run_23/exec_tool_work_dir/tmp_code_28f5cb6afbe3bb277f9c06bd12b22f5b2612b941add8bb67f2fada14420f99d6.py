code = """import json
import re

# Read the civic docs data from the stored file
civic_docs_file = locals()['var_functions.query_db:0']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data from the stored file
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract project information from civic docs
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project patterns in the text
    # Capital Improvement Projects
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        # Look for project names
        project_match = re.search(r'^[A-Z][a-zA-Z\s&\-\(\)]{10,80}$', section.strip(), re.MULTILINE)
        if project_match:
            project_name = project_match.group().strip()
            
            # Look for status indicators
            has_design = 'Design' in section or 'design' in section
            has_completed = 'completed' in section or 'Complete Construction' in section
            has_not_started = 'Not Started' in section or 'not started' in section
            
            # Look for dates
            year_matches = re.findall(r'202[0-3]', section)
            has_2022 = '2022' in year_matches
            
            # Determine type (disaster or capital)
            is_disaster = False
            if 'FEMA' in section or 'CalOES' in section or 'CalJPIA' in section or \
               'disaster' in section.lower() or 'fire' in section.lower() or \
               'emergency' in section.lower() or 'recovery' in section.lower():
                is_disaster = True
            
            # Determine status
            status = None
            if has_completed:
                status = 'completed'
            elif has_design:
                status = 'design'
            elif has_not_started:
                status = 'not started'
            
            # Look for start time in 2022
            has_start_2022 = False
            if '2022' in section:
                # Check if it's a start indicator
                if re.search(r'(Complete|Begin|Start|Advertise).*2022', section, re.IGNORECASE):
                    has_start_2022 = True
            
            if is_disaster and has_start_2022:
                projects.append({
                    'project_name': project_name,
                    'type': 'disaster',
                    'status': status,
                    'start_2022': True
                })

# Create a mapping of project names that are disaster-related and started in 2022
disaster_projects_2022 = {p['project_name']: p for p in projects if p['type'] == 'disaster' and p['start_2022']}

# Also compile a list of disaster-related project names for matching
# These often have suffixes in the funding table
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery']

# Calculate total funding for disaster projects that started in 2022
total_funding = 0
funded_projects = []

for funding in funding_data:
    fund_project_name = funding.get('Project_Name', '')
    amount = int(funding.get('Amount', 0))
    
    # Check if this is a disaster project
    is_disaster_project = False
    
    # Direct match with extracted projects
    if fund_project_name in disaster_projects_2022:
        is_disaster_project = True
    
    # Check for disaster keywords in the name
    elif any(keyword.upper() in fund_project_name.upper() for keyword in disaster_keywords):
        is_disaster_project = True
        
        # Additional check - does it seem to be related to 2022 start
        # Look for base project names that might have started in 2022
        base_name = re.sub(r' \(FEMA.*\)$', '', fund_project_name)
        base_name = re.sub(r' \(CalOES.*\)$', '', base_name)
        base_name = re.sub(r' \(CalJPIA.*\)$', '', base_name)
        
        # If the base project started in 2022, count it
        for proj_name in disaster_projects_2022.keys():
            if base_name in proj_name or proj_name in base_name:
                is_disaster_project = True
                break
    
    if is_disaster_project:
        total_funding += amount
        funded_projects.append({
            'project': fund_project_name,
            'amount': amount
        })

result = {
    'total_funding': total_funding,
    'count': len(funded_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

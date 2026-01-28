code = """import json
import re

# Get the file paths from the stored variables
civic_docs_file = "/tmp/tmpq4n8w6o8.json"
funding_file = "/tmp/tmp7s5c8t5x.json"

# Read the full datasets
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract project information from civic documents
projects = []

# Patterns to identify disaster projects
disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'Woolsey']

# Date patterns to extract start dates
date_patterns = [
    r'(?:Complete Design|Advertise|Begin Construction|Begin|Complete Construction|Final Design|Start)\s*:\s*(\w+\s*\d{4}|\d{4}-\w+|\d{4})',
    r'(?:Project Schedule|Schedule)\s*.*?(\d{4})',
    r'(\d{4})-(Spring|Summer|Fall|Winter)',
    r'(Spring|Summer|Fall|Winter)\s+(\d{4})',
    r'(\d{4})-(\d{1,2})',
    r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})'
]

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into lines for processing
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for project names (typically on their own line, often with year prefix)
        # Pattern: Optional bullet, then project name with optional year and suffixes
        proj_match = re.match(r'^[\u2022\-\*\u25cf]?\s*([A-Z][A-Za-z0-9\s\&\-\/]+(?:\s*\d{4})?\s*(?:\((?:FEMA|CalOES|CalJPIA)(?:\s+Project)?\)|(?:FEMA|CalOES|CalJPIA)\s+Project)?)\s*$', line)
        
        if proj_match:
            # Save previous project if exists
            if current_project:
                projects.append(current_project)
            
            project_name = proj_match.group(1).strip()
            
            # Determine if disaster project
            project_lower = project_name.lower()
            is_disaster = any(indicator.lower() in project_lower for indicator in disaster_indicators) or \
                         '(FEMA' in project_name or '(CalOES' in project_name or '(CalJPIA' in project_name
            
            current_project = {
                'Project_Name': project_name,
                'type': 'disaster' if is_disaster else 'capital',
                'st': '',
                'et': '',
                'source_file': filename,
                'context': ''
            }
            
            # Extract topics for disaster projects
            if is_disaster:
                topics = []
                if '(FEMA' in project_name or 'FEMA' in project_name:
                    topics.append('FEMA')
                if '(CalOES' in project_name or 'CalOES' in project_name:
                    topics.append('CalOES')
                if '(CalJPIA' in project_name or 'CalJPIA' in project_name:
                    topics.append('CalJPIA')
                current_project['topics'] = ', '.join(topics)
            
            continue
        
        # If we have a current project, look for schedule info in current and next few lines
        if current_project:
            # Search in current line for dates
            for pattern in date_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    for match in matches:
                        if isinstance(match, tuple):
                            # Handle tuple returns from regex
                            for item in match:
                                if isinstance(item, str) and len(item) == 4 and item.isdigit():
                                    year = item
                                    if not current_project['st']:
                                        current_project['st'] = year
                                    elif not current_project['et']:
                                        current_project['et'] = year
                                elif isinstance(item, str) and '202' in item:  # Catch 2020-2029
                                    if not current_project['st'] and '2022' in item:
                                        current_project['st'] = item
                                    elif not current_project['et']:
                                        current_project['et'] = item
                        elif isinstance(match, str):
                            if '202' in match:
                                if not current_project['st'] and '2022' in match:
                                    current_project['st'] = match
                                elif not current_project['et']:
                                    current_project['et'] = match
    
    # Add the last project
    if current_project:
        projects.append(current_project)

# Filter for disaster projects that started in 2022
disaster_projects_2022 = []
for project in projects:
    if project['type'] == 'disaster':
        started_in_2022 = False
        
        # Check if start date contains 2022
        if project['st'] and '2022' in str(project['st']):
            started_in_2022 = True
        
        # Check if project name starts with 2022 (common pattern like "2022 Morning View...")
        if project['Project_Name'].startswith('2022'):
            started_in_2022 = True
            # Set start date if not already set
            if not project['st']:
                project['st'] = '2022'
        
        # Check if "2022" appears anywhere in project info and likely indicates start
        project_str = str(project['Project_Name']) + ' ' + str(project['st'])
        if '2022' in project_str and project['st']:
            started_in_2022 = True
        
        if started_in_2022:
            disaster_projects_2022.append(project)

# Remove duplicates by project name (common issue with parsing)
unique_projects = {}
for project in disaster_projects_2022:
    key = project['Project_Name']
    if key not in unique_projects:
        unique_projects[key] = project

unique_disaster_projects = list(unique_projects.values())

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022': unique_disaster_projects,
    'total_found': len(unique_disaster_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}]}

exec(code, env_args)

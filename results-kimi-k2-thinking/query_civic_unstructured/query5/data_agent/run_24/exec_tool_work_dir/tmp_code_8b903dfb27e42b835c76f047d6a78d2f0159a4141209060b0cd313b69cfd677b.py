code = """import json
import re

# Read the full MongoDB results from the file
with open('/tmp/tmpq4n8w6o8.json', 'r') as f:
    civic_docs = json.load(f)

# Initialize list to store extracted project info
projects = []

# Patterns to identify disaster projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency']

# Patterns to extract dates and schedules
date_patterns = [
    r'(Complete Design|Advertise|Begin Construction|Begin|Complete Construction|Final Design):\s*(\w+\s*\d{4}|\d{4}-\w+|\d{4})',
    r'(\d{4})-(Spring|Summer|Fall|Winter)',
    r'(Spring|Summer|Fall|Winter)\s+(\d{4})',
    r'(\d{4})-(\d{2})',
    r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})'
]

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into sections to find project blocks
    # Look for common patterns that indicate project sections
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Look for project names (typically capitalized, sometimes with year prefix)
        # Pattern: project names often appear as standalone lines or with bullet points
        project_name_match = re.match(r'^[\u2022\-\*]?\s*([A-Z][A-Za-z\s\&\-]+(?:\s*\d{4})?\s*(?:Project|Improvements|Repairs|Program)?(?:\s*\(FEMA\s+Project\)|\s*\(CalOES\s+Project\)|\s*\(CalJPIA\s+Project\))?)$', line)
        
        if project_name_match:
            # Save previous project if exists
            if current_project and project_info:
                projects.append(project_info.copy())
            
            # Start new project
            current_project = project_name_match.group(1).strip()
            project_info = {
                'Project_Name': current_project,
                'type': '',
                'status': '',
                'st': '',
                'et': '',
                'topics': '',
                'source_file': filename
            }
            
            # Determine if it's a disaster project
            project_lower = current_project.lower()
            if any(keyword.lower() in project_lower for keyword in disaster_keywords) or \
               '(FEMA' in current_project or '(CalOES' in current_project or '(CalJPIA' in current_project:
                project_info['type'] = 'disaster'
                # Extract topics
                topics = []
                if 'FEMA' in current_project:
                    topics.append('FEMA')
                if 'CalOES' in current_project:
                    topics.append('CalOES')
                if 'CalJPIA' in current_project:
                    topics.append('CalJPIA')
                if any(word in project_lower for word in ['drain', 'storm']):
                    topics.extend(['drainage', 'storm drain'])
                if 'fire' in project_lower:
                    topics.append('fire')
                project_info['topics'] = ', '.join(topics)
            else:
                # Default to capital for now, will refine
                project_info['type'] = 'capital'
            
            continue
        
        # Extract schedule information
        if current_project:
            # Look for date patterns
            for pattern in date_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    for match in matches:
                        if isinstance(match, tuple):
                            # Check if it's a year pattern
                            for item in match:
                                if isinstance(item, str) and '2022' in item:
                                    project_info['st'] = item
                                    break
                                elif isinstance(item, str) and '2023' in item:
                                    project_info['et'] = item
                                    break
                        elif '2022' in match:
                            project_info['st'] = match
                        elif '2023' in match:
                            project_info['et'] = match
    
    # Add the last project
    if current_project and project_info:
        projects.append(project_info)

# Filter for disaster projects that started in 2022
disaster_projects_2022 = []
for project in projects:
    if project['type'] == 'disaster':
        # Check if start date contains 2022
        if project['st'] and '2022' in project['st']:
            disaster_projects_2022.append(project)
        # Also check if project name starts with 2022
        elif project['Project_Name'].startswith('2022'):
            disaster_projects_2022.append(project)
        # Check for 2022 in any date field
        elif any('2022' in str(value) for value in project.values() if isinstance(value, str)):
            # Additional check to ensure it's actually a start date
            if 'st' in project and project['st']:
                disaster_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022': disaster_projects_2022,
    'all_projects': projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import re
from collections import defaultdict

# Load the data
funding_path = locals()['var_functions.query_db:10']
docs_path = locals()['var_functions.query_db:2']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Convert funding amounts to integers
for record in funding_records:
    record['Amount'] = int(record['Amount'])

# Function to extract projects from a civic document text
def extract_projects_from_text(text, filename):
    projects = []
    
    # Split text into sections that might contain projects
    # Look for project names that might have disaster indicators
    lines = text.split('\n')
    
    # Patterns that indicate project sections
    project_indicators = [
        r'(^[A-Z][a-zA-Z\s&-]+?(?:Project|Improvements|Repairs|Replacement|Upgrades|Construction|System|Facility|Structure|Plan|Study)$)',
        r'(\(FEMA Project\))',
        r'(\(CalOES Project\))', 
        r'(\(CalJPIA Project\))'
    ]
    
    # Common project name patterns from the data
    disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster', 'warning', 'siren']
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line looks like a project name
        project_match = re.match(r'^([A-Z][a-zA-Z\s&\-\(\)/]+?(?:Project|Improvements|Repairs|Replacement|Upgrades|Construction|System|Facility|Structure|Plan|Study))$', line)
        
        if project_match:
            # If we were building a project, save it
            if current_project and current_project.get('name'):
                projects.append(current_project)
            
            # Start new project
            name = project_match.group(1).strip()
            current_project = {
                'name': name,
                'filename': filename,
                'type': None,
                'topic': '',
                'status': None,
                'st': None,
                'et': None
            }
            
            # Check if it's a disaster project based on name
            if any(keyword in name for keyword in disaster_keywords) or \
               '(FEMA Project)' in name or '(CalOES Project)' in name or '(CalJPIA Project)' in name:
                current_project['type'] = 'disaster'
        
        # Extract schedule information
        if current_project:
            # Look for start/completion dates
            if 'Project Schedule:' in line or 'Schedule:' in line:
                # Look ahead for date patterns
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    
                    # Look for 2022 dates in various formats
                    if '2022' in next_line:
                        # Check if it's a start date
                        if any(word in next_line.lower() for word in ['begin', 'start', 'advertise', 'complete design']):
                            current_project['st'] = next_line
                        # Check if it's an end date  
                        elif any(word in next_line.lower() for word in ['complete', 'end', 'finish']):
                            current_project['et'] = next_line
                    
                    # Look for seasonal dates with 2022
                    season_pattern = r'(Spring|Summer|Fall|Winter)\s+(2022)'
                    season_match = re.search(season_pattern, next_line, re.IGNORECASE)
                    if season_match:
                        if any(word in next_line.lower() for word in ['begin', 'start', 'advertise']):
                            current_project['st'] = next_line
                        elif any(word in next_line.lower() for word in ['complete', 'end']):
                            current_project['et'] = next_line
    
    # Add the last project
    if current_project and current_project.get('name'):
        projects.append(current_project)
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'], doc['filename'])
    all_projects.extend(projects)

print(f"Extracted {len(all_projects)} potential projects")

# Show sample projects
sample = all_projects[:10] if all_projects else []
print('__RESULT__:')
print(json.dumps({
    'total_projects': len(all_projects),
    'sample_projects': sample
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_doc_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)

code = """import json
import re

# Load the data
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = locals()['var_functions.query_db:22']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Function to extract project information from text
def extract_projects_from_text(text, doc_id, filename):
    """Extract project information from civic document text"""
    projects = []
    
    # Look for capital and disaster project sections
    # Pattern to match project names (typically title case lines)
    lines = text.split('\n')
    
    current_project = None
    schedule_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or line.startswith('Page') or line.startswith('Agenda Item'):
            continue
            
        # Look for project-like lines (title case, not too short, not common phrases)
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('To:') and
            not line.startswith('Prepared by:') and
            not line.startswith('Approved by:') and
            not line.startswith('Date prepared:') and
            not line.startswith('Meeting date:') and
            not line.startswith('Subject:') and
            not line.startswith('RECOMMENDED ACTION:') and
            not line.startswith('DISCUSSION:') and
            not 'Capital Improvement Projects' in line and
            not 'Disaster Recovery Projects' in line):
            
            # Check if this looks like a project name (contains keywords or has proper structure)
            project_keywords = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Installation', 
                              'Construction', 'Drainage', 'Road', 'Bridge', 'Park', 'Facility']
            
            if any(keyword in line for keyword in project_keywords):
                # Save previous project if exists
                if current_project and current_project.get('name'):
                    projects.append(current_project)
                
                # Start new project
                current_project = {
                    'name': line,
                    'doc_id': doc_id,
                    'filename': filename,
                    'topics': [],
                    'type': None,  # Will determine based on keywords
                    'status': None,
                    'st': None,
                    'et': None
                }
                
                # Determine type based on keywords
                if any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency']):
                    current_project['type'] = 'disaster'
                elif any(k in line for k in ['capital', 'infrastructure']):
                    current_project['type'] = 'capital'
                
                # Determine topics based on keywords
                topics = []
                if 'FEMA' in line:
                    topics.append('FEMA')
                if 'CalOES' in line:
                    topics.append('CalOES')
                if 'CalJPIA' in line:
                    topics.append('CalJPIA')
                if 'fire' in line.lower():
                    topics.append('fire')
                if 'road' in line.lower():
                    topics.append('road')
                if 'park' in line.lower():
                    topics.append('park')
                if 'drain' in line.lower() or 'drainage' in line.lower():
                    topics.append('drainage')
                if 'bridge' in line.lower():
                    topics.append('bridge')
                if 'emergency' in line.lower():
                    topics.append('emergency')
                
                current_project['topics'] = topics
                
        # Look for schedule information
        if current_project:
            if 'Project Schedule:' in line or 'Project Updates:' in line or 'Updates:' in line:
                schedule_section = True
                
            # Extract dates from schedule section
            if schedule_section:
                # Look for dates in various formats
                date_patterns = [
                    r'(\d{4}-(?:Spring|Fall|Summer|Winter))',  # 2022-Spring
                    r'(\d{4}-\d{1,2})',  # 2022-02
                    r'(\d{4}-(?:January|February|March|April|May|June|July|August|September|October|November|December))',  # 2022-March
                ]
                
                for pattern in date_patterns:
                    matches = re.findall(pattern, line, re.IGNORECASE)
                    for match in matches:
                        if '2022' in match:
                            if not current_project['st']:
                                current_project['st'] = match
                            else:
                                current_project['et'] = match
                
                # Check for "Complete Design: Summer 2023" format
                year_match = re.search(r'\b(202\d)\b', line)
                if year_match and '2022' in year_match.group(1):
                    if not current_project['st']:
                        current_project['st'] = year_match.group(1)
    
    # Add last project if exists
    if current_project and current_project.get('name'):
        projects.append(current_project)
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    doc_projects = extract_projects_from_text(doc['text'], doc['_id'], doc['filename'])
    all_projects.extend(doc_projects)

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(all_projects),
    'sample_projects': all_projects[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json'], 'var_functions.execute_python:16': {'funding_type': "<class 'list'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'funding_count': 10, 'civic_is_file_path': 'yes'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_count': 10}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_documents': 5}}

exec(code, env_args)

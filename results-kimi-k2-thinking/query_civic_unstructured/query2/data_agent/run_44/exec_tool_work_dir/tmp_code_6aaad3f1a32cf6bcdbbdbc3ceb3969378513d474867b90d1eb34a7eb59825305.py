code = """import json
import re
from collections import defaultdict

# Load the civic docs data
civic_docs_key = 'var_functions.query_db:0'
civic_docs_path = locals()[civic_docs_key]
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_key = 'var_functions.query_db:1'
funding_path = locals()[funding_key]
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integer for summing
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Create a lookup for funding by project name
funding_lookup = {}
for fund in funding_data:
    proj_name = fund['Project_Name'].strip().lower()
    funding_lookup[proj_name] = fund

# Function to extract projects from civic doc text
def extract_projects_from_text(text, filename):
    projects = []
    
    # Pattern 1: Projects with "Construction was completed" (explicit completion)
    completion_pattern = r'([A-Z][^.]*?)\n\(cid:190\) Updates:\s*\n\s*\(cid:131\) Construction was completed[^\n]*?(2022)[^\n]*'
    
    # Pattern 2: Project names as headers followed by updates
    project_header_pattern = r'([A-Z][A-Za-z0-9 &\-\(\)]+)\n\(cid:190\) Updates:\s*\n([^\n]*(?:\n[^\n]*?)*)'
    
    # Pattern 3: Explicit status mentions
    status_patterns = [
        (r'Construction was completed[^\n]*?(2022)', 'completed', '2022'),
        (r'Completed Construction[^\n]*?(2022)', 'completed', '2022'),
        (r'Notice of completion filed[^\n]*?(2022)', 'completed', '2022'),
        (r'Construction was completed, (\w+\s+2022)', 'completed', '2022'),
    ]
    
    lines = text.split('\n')
    i = 0
    current_project = None
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for project names (typically title case, no special chars at start)
        if (line and 
            not line.startswith('(') and 
            not line.startswith('Page') and 
            not line.startswith('Agenda') and
            not line.startswith('To:') and
            not line.startswith('Prepared') and
            not line.startswith('Approved') and
            not line.startswith('Date') and
            not line.startswith('Meeting') and
            not line.startswith('Subject:') and
            not line.startswith('RECOMMENDED') and
            not line.startswith('DISCUSSION:') and
            not line.startswith('Capital Improvement Projects') and
            not line.startswith('Disaster Recovery Projects') and
            not line.startswith('Fiscal') and
            len(line) > 10 and
            len(line) < 150 and
            (line[0].isupper() or line[0].isdigit()) and
            ('Project' not in line or len(line.split()) > 2)):
            
            # Check if this is likely a project name
            words = line.split()
            if len(words) >= 2 and not any(phrase in line for phrase in ['Status Report', 'City Council', 'Public Works']):
                # Store previous project if exists
                if current_project:
                    projects.append(current_project)
                
                current_project = {
                    'name': line,
                    'filename': filename,
                    'status': None,
                    'completion_year': None,
                    'topics': [],
                    'text_snippet': ''
                }
                
                # Look ahead for status information
                look_ahead = 10
                for j in range(i+1, min(i+look_ahead, len(lines))):
                    next_line = lines[j].strip()
                    
                    # Check for completion in 2022
                    if 'completed' in next_line.lower() and '2022' in next_line:
                        current_project['status'] = 'completed'
                        current_project['completion_year'] = '2022'
                    elif 'Construction was completed' in next_line and '2022' in next_line:
                        current_project['status'] = 'completed'
                        current_project['completion_year'] = '2022'
                    elif 'Notice of completion filed' in next_line and '2022' in next_line:
                        current_project['status'] = 'completed'
                        current_project['completion_year'] = '2022'
                    elif 'Complete Construction' in next_line and '2022' in next_line:
                        current_project['status'] = 'completed'
                        current_project['completion_year'] = '2022'
                    
                    # Check for topics
                    if 'park' in next_line.lower():
                        if 'park' not in current_project['topics']:
                            current_project['topics'].append('park')
                    if any(word in next_line.lower() for word in ['road', 'street']):
                        if 'road' not in current_project['topics']:
                            current_project['topics'].append('road')
                    if 'drain' in next_line.lower():
                        if 'drainage' not in current_project['topics']:
                            current_project['topics'].append('drainage')
                
                # Default topics based on project name
                proj_name_lower = line.lower()
                if 'park' in proj_name_lower:
                    current_project['topics'].append('park')
                if any(word in proj_name_lower for word in ['road', 'street', 'highway']):
                    current_project['topics'].append('road')
                if any(word in proj_name_lower for word in ['drain', 'storm', 'sewer']):
                    current_project['topics'].append('drainage')
        
        i += 1
    
    # Add last project
    if current_project:
        projects.append(current_project)
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'], doc['filename'])
    all_projects.extend(projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for proj in all_projects:
    if (proj['status'] == 'completed' and 
        proj['completion_year'] == '2022' and 
        'park' in proj['topics']):
        park_projects_2022.append(proj)

# Debug: print the projects found
print('__RESULT__:')
print(json.dumps({
    'total_projects_extracted': len(all_projects),
    'park_projects_2022_count': len(park_projects_2022),
    'park_projects_2022': park_projects_2022
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)

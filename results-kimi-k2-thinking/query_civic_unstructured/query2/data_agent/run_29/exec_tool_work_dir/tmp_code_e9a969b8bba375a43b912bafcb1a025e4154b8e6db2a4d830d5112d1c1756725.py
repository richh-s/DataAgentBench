code = """import json
import re

# Load civic documents from the file
civic_docs_file = '/tmp/tmpz5hptp8z.json'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data from the file
funding_file = '/tmp/tmphs_qx5r1.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Split by project sections looking for project names
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this is a project name (typically followed by updates)
        if len(line) > 5 and not line.startswith('(') and not line.startswith('---'):
            # Look ahead to see if this is followed by project content
            is_project = False
            for next_line in lines[i+1:i+4]:
                next_line_lower = next_line.lower()
                if any(marker in next_line_lower for marker in ['updates:', 'project schedule:', 'complete construction:', 'status:', '(cid:']):
                    is_project = True
                    break
            
            if is_project:
                # Save previous project
                if current_project and project_info.get('status') == 'completed' and '2022' in project_info.get('et', ''):
                    park_projects_2022.append(project_info)
                
                current_project = line
                project_info = {
                    'Project_Name': line,
                    'status': '',
                    'et': '',
                    'topic': ''
                }
                
                # Determine topic from project name
                project_lower = line.lower()
                topics = []
                if 'park' in project_lower:
                    topics.append('park')
                if 'playground' in project_lower:
                    topics.append('playground')
                if 'road' in project_lower:
                    topics.append('road')
                if 'drain' in project_lower or 'storm' in project_lower:
                    topics.append('drainage')
                if 'fema' in project_lower:
                    topics.append('FEMA')
                
                project_info['topic'] = ', '.join(topics)
        
        # Check for completion status and dates
        if current_project:
            line_lower = line.lower()
            if any(phrase in line_lower for phrase in ['completed', 'complete construction', 'construction was completed', 'notice of completion']):
                project_info['status'] = 'completed'
                
                # Extract date looking for 2022 patterns
                date_patterns = [
                    r'(\w+\s+2022)\b',  # November 2022
                    r'(2022-\w+)\b',    # 2022-November
                    r'(\b2022\b)',       # 2022
                    r'(Fall\s+2022)',
                    r'(Summer\s+2022)',
                    r'(Spring\s+2022)',
                    r'(Winter\s+2022)',
                    r'(January\s+2022)',
                    r'(February\s+2022)',
                    r'(March\s+2022)',
                    r'(April\s+2022)',
                    r'(May\s+2022)',
                    r'(June\s+2022)',
                    r'(July\s+2022)',
                    r'(August\s+2022)',
                    r'(September\s+2022)',
                    r'(October\s+2022)',
                    r'(November\s+2022)',
                    r'(December\s+2022)'
                ]
                
                for pattern in date_patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        project_info['et'] = match.group(1)
                        break
    
    # Save the last project
    if current_project and project_info.get('status') == 'completed' and '2022' in project_info.get('et', ''):
        park_projects_2022.append(project_info)

# Now filter for only park-related projects
park_related_projects = []
for project in park_projects_2022:
    topics = project.get('topic', '').lower()
    if 'park' in topics or 'playground' in topics:
        park_related_projects.append(project)

# Create a mapping of project names to look up funding
project_names = [proj['Project_Name'] for proj in park_related_projects]

# Find matching funding with flexible matching
funding_matches = []
for funding in funding_data:
    funding_name = funding['Project_Name'].lower()
    for project in park_related_projects:
        project_name = project['Project_Name'].lower()
        # Check for direct match or partial match
        if (funding['Project_Name'] == project['Project_Name'] or 
            funding_name in project_name or 
            project_name in funding_name):
            funding_matches.append({
                'Project_Name': project['Project_Name'],
                'Funding_Name': funding['Project_Name'],
                'Amount': int(funding['Amount'])
            })

# Sum the funding
if funding_matches:
    import pandas as pd
    df = pd.DataFrame(funding_matches)
    total_funding = df['Amount'].sum()
else:
    total_funding = 0

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': park_related_projects,
    'project_count': len(park_related_projects),
    'funding_matches': funding_matches,
    'funding_count': len(funding_matches),
    'total_funding': total_funding
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

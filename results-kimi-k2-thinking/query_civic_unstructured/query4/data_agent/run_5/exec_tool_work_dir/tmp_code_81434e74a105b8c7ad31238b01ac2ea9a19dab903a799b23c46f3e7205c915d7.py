code = """import json
import re
from datetime import datetime

# Load data from files
civic_docs = json.load(open('/tmp/tmp1.json'))
funding_data = json.load(open('/tmp/tmp2.json'))

print("Step 1: Data loaded successfully")
print(f"Civic docs: {len(civic_docs)} documents")
print(f"Funding records: {len(funding_data)} records")

# Convert funding amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])
    record['Funding_ID'] = int(record['Funding_ID'])

# Create a mapping of project names to funding
funding_map = {}
for record in funding_data:
    proj_name = record['Project_Name']
    if proj_name not in funding_map:
        funding_map[proj_name] = []
    funding_map[proj_name].append(record)

print(f"Funding map created with {len(funding_map)} unique project names")

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Common patterns:
    # - Project name followed by "(cid:190) Updates:" or similar
    # - Project name at the start of a line
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and obvious section headers
        if not line or line.startswith('Public Works') or line.startswith('Commission') or \
           line.startswith('To:') or line.startswith('Prepared by:') or \
           line.startswith('Approved by:') or line.startswith('Date prepared:') or \
           line.startswith('Meeting date:') or line.startswith('Subject:') or \
           line.startswith('RECOMMENDED ACTION:') or line.startswith('DISCUSSION:'):
            continue
            
        # Look for project names (usually before "Updates:" or "Project Schedule:")
        if 'Updates:' in line or 'Project Schedule:' in line or 'Estimated Schedule:' in line:
            # The project name is likely the previous non-empty line
            if i > 0:
                prev_line = lines[i-1].strip()
                if prev_line and not any(prev_line.startswith(x) for x in ['(', 'cid:', '•', '-', '■']):
                    if len(prev_line) > 10 and not prev_line.isupper():  # Likely a project name
                        current_project = prev_line
                        
                        # Extract project info from following lines
                        start_date = None
                        status = None
                        
                        # Look ahead for schedule info
                        for j in range(i+1, min(i+10, len(lines))):
                            next_line = lines[j].strip()
                            
                            # Look for dates
                            if 'Complete Design:' in next_line or 'Begin Construction:' in next_line or \
                               'Advertise:' in next_line or 'Complete Construction:' in next_line:
                                # Extract date
                                date_match = re.search(r'(Spring|Summer|Fall|Winter)\s+(\d{4})', next_line)
                                if date_match:
                                    season = date_match.group(1)
                                    year = date_match.group(2)
                                    if not start_date:
                                        start_date = f"{year}-{season}"
                            
                            # Look for status indicators
                            if 'design' in next_line.lower():
                                status = 'design'
                            elif 'construction' in next_line.lower() and ('under' in next_line.lower() or 'completed' in next_line.lower()):
                                if 'under' in next_line.lower():
                                    status = 'construction'
                                elif 'completed' in next_line.lower():
                                    status = 'completed'
                            elif 'not started' in next_line.lower():
                                status = 'not started'
                        
                        if current_project and start_date:
                            # Determine type based on name and keywords
                            project_type = 'capital'  # default
                            if any(x in current_project.lower() for x in ['fema', 'fire', 'disaster', 'recovery']):
                                project_type = 'disaster'
                            elif any(x in current_project.lower() for x in ['storm', 'drain', 'culvert', 'bridge', 'road', 'street', 'park', 'facility', 'signal', 'crosswalk', 'guardrail']):
                                project_type = 'capital'
                            
                            # Determine topic
                            topics = []
                            if 'park' in current_project.lower():
                                topics.append('park')
                            if 'road' in current_project.lower() or 'street' in current_project.lower():
                                topics.append('road')
                            if 'storm' in current_project.lower() or 'drain' in current_project.lower():
                                topics.append('drainage')
                            if 'fema' in current_project.lower():
                                topics.append('FEMA')
                            if 'fire' in current_project.lower():
                                topics.append('fire')
                            if 'bridge' in current_project.lower():
                                topics.append('bridge')
                            if 'signal' in current_project.lower():
                                topics.append('signal')
                            if 'crosswalk' in current_project.lower():
                                topics.append('crosswalk')
                            if 'guardrail' in current_project.lower():
                                topics.append('guardrail')
                            
                            topic_str = ', '.join(topics) if topics else 'general infrastructure'
                            
                            projects.append({
                                'Project_Name': current_project,
                                'topic': topic_str,
                                'type': project_type,
                                'status': status or 'unknown',
                                'st': start_date,
                                'et': None,
                                'source_file': filename
                            })

# Filter for Spring 2022 projects
spring_2022_projects = []
for proj in projects:
    if proj['st'] and '2022' in proj['st'] and 'Spring' in proj['st']:
        spring_2022_projects.append(proj)

print(f"\nFound {len(spring_2022_projects)} projects starting in Spring 2022")

# For each Spring 2022 project, find matching funding
results = []
total_funding = 0

for proj in spring_2022_projects:
    project_name = proj['Project_Name']
    
    # Look for exact match and partial matches
    matching_funding = []
    
    # Exact match
    if project_name in funding_map:
        matching_funding.extend(funding_map[project_name])
    else:
        # Try to find similar names (without suffixes like "Project", "Improvements", etc.)
        base_name = re.sub(r'\s+(Project|Improvements|Repairs|Infrastructure|Renovation)$', '', project_name)
        
        for funded_proj, funds in funding_map.items():
            if funded_proj.startswith(base_name) or base_name in funded_proj:
                matching_funding.extend(funds)
    
    proj_funding = sum(f['Amount'] for f in matching_funding)
    total_funding += proj_funding
    
    results.append({
        'project': project_name,
        'funding_records': len(matching_funding),
        'funding_amount': proj_funding,
        'details': proj
    })

print(f"Total funding for Spring 2022 projects: ${total_funding:,}")

# Prepare result
result = {
    'count': len(spring_2022_projects),
    'total_funding': total_funding,
    'projects': results
}

print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

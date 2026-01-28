code = """import json
import re

# Read the full civic_docs results
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")

# Extract project information from text
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split by lines to find project headings and details
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and lines that are clearly not project names
        if not line or line.startswith('(') or line.startswith('●') or line.startswith('■'):
            continue
            
        # Skip common agenda headings
        if any(heading in line.lower() for heading in ['capital improvement', 'disaster recovery', 'public works', 'commission meeting', 'agenda report', 'page ', 'item #']):
            continue
            
        # Check if this might be a project name (followed by project-related content)
        next_chunks = []
        for j in range(i+1, min(i+5, len(lines))):
            next_line = lines[j].strip()
            if next_line and not next_line.startswith('('):
                next_chunks.append(next_line)
        
        next_text = ' '.join(next_chunks).lower()
        
        # If next lines contain project indicators, this is likely a project
        if any(indicator in next_text for indicator in ['updates:', 'schedule:', 'complete', 'design', 'construction', 'project']):
            # Found a project
            if current_project:
                projects.append(current_project)
            
            current_project = {
                'Project_Name': line,
                'topic': '',
                'status': '',
                'st': '',
                'et': '',
                'source_doc': filename
            }
            
            # Extract potential topics from name
            name_lower = line.lower()
            topics = []
            if 'park' in name_lower:
                topics.append('park')
            if 'road' in name_lower or 'street' in name_lower:
                topics.append('road')
            if 'drain' in name_lower or 'storm' in name_lower:
                topics.append('drainage')
            if 'warning' in name_lower:
                topics.append('emergency warning')
            if 'playground' in name_lower:
                topics.append('playground')
            if 'bridge' in name_lower:
                topics.append('bridge')
            if 'water' in name_lower:
                topics.append('water treatment')
            if 'guardrail' in name_lower:
                topics.append('guardrail')
            if 'fire' in name_lower:
                topics.append('fire')
            if 'fema' in name_lower:
                topics.append('FEMA')
                
            current_project['topic'] = ', '.join(topics)
        
        # Extract status and dates from updates and schedule
        if current_project:
            # Look for completion patterns in this line
            line_lower = line.lower()
            
            # Check for completed status
            if any(word in line_lower for word in ['completed', 'notice of completion', 'construction was completed']):
                current_project['status'] = 'completed'
                # Try to extract year
                year_match = re.search(r'(202\d)', line)
                if year_match:
                    current_project['et'] = year_match.group(1)
            
            # Check for specific completion dates
            if 'complete construction' in line_lower or 'complete:' in line_lower:
                year_match = re.search(r'(202\d)', line)
                if year_match:
                    current_project['et'] = year_match.group(1)
                    current_project['status'] = 'completed'
            
            # Check for design status
            if 'design' in line_lower and current_project['status'] == '':
                current_project['status'] = 'design'
                
            # Check for not started
            if any(word in line_lower for word in ['not started', 'identified', 'proposed']) and current_project['status'] == '':
                current_project['status'] = 'not started'
    
    # Don't forget the last project
    if current_project:
        projects.append(current_project)

print(f"Extracted {len(projects)} potential projects")

# Show first 10 projects to verify
for i, p in enumerate(projects[:10]):
    print(f"{i+1}. {p['Project_Name']} | Topic: {p['topic']} | Status: {p['status']} | End: {p['et']}")

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for p in projects:
    # Check if park-related
    topics = p.get('topic', '').lower()
    if 'park' not in topics:
        # Also check project name itself
        if 'park' not in p['Project_Name'].lower():
            continue
    
    # Check if completed and has 2022 date
    et = p.get('et', '')
    status = p.get('status', '')
    
    if '2022' in et and status == 'completed':
        park_projects_2022.append(p)
    elif status == 'completed' and '2022' in str(p):
        # Additional check in the whole project dict
        park_projects_2022.append(p)

print(f"\nFound {len(park_projects_2022)} park projects completed in 2022:")
for p in park_projects_2022:
    print(f"- {p['Project_Name']} (End: {p['et']}, Status: {p['status']}, Doc: {p['source_doc']})")

# Save the filtered projects for next step
with open('/tmp/park_projects_2022.json', 'w') as f:
    json.dump(park_projects_2022, f, indent=2)

print("\nPark projects saved to /tmp/park_projects_2022.json")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

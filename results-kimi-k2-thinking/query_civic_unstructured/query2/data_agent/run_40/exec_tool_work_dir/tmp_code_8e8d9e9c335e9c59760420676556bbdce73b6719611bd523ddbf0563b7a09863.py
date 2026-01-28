code = """import json
import re

# Read the full civic_docs results
civic_docs_path = var_functions.query_db:2
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
    in_project_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Detect project headings (typically standalone project names)
        # These are often followed by updates or schedule info
        if len(line) > 0 and not line.startswith('(') and not line.startswith('●') and not line.startswith('■') and not line.startswith('■'):
            # Check if next lines contain project indicators
            next_lines = '\n'.join(lines[i:i+5])
            if 'Updates:' in next_lines or 'Schedule:' in next_lines or 'Complete' in next_lines:
                # Likely a project name
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
            # Look for completion patterns
            completion_patterns = [
                r'completed[^\n,]*[,\s]+(\w+\s+202\d)',
                r'completed:\s*(\w+\s+202\d)',
                r'Complete Construction:\s*(\w+\s+202\d)',
                r'Complete:\s*(\w+\s+202\d)',
                r'Complete Design:\s*(\w+\s+202\d)',
                r'Complete[^\n]*(\d{4})'
            ]
            
            for pattern in completion_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    current_project['et'] = matches[0] if isinstance(matches[0], str) else matches[0]
                    current_project['status'] = 'completed'
                    break
            
            # Look for status patterns
            status_patterns = {
                'completed': [r'completed', r'notice of completion', r'construction was completed'],
                'design': [r'design', r'in design', r'planning', r'preliminary design'],
                'not started': [r'not started', r'identified', r'proposed']
            }
            
            for status, patterns in status_patterns.items():
                for pattern in patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        current_project['status'] = status
                        break
    
    # Don't forget the last project
    if current_project:
        projects.append(current_project)

print(f"Extracted {len(projects)} potential projects")

# Show first few projects to verify extraction
for i, p in enumerate(projects[:10]):
    print(f"{i+1}. {p['Project_Name']} | Topic: {p['topic']} | Status: {p['status']} | End: {p['et']}")

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for p in projects:
    # Check if park-related
    topics = p.get('topic', '').lower()
    if 'park' not in topics:
        continue
        
    # Check if completed in 2022
    et = p.get('et', '')
    status = p.get('status', '')
    
    if ('2022' in et) or ('2022' in str(p)):
        if status == 'completed' or 'completed' in et.lower():
            park_projects_2022.append(p)

print(f"\nFound {len(park_projects_2022)} park projects completed in 2022")
for p in park_projects_2022:
    print(f"- {p['Project_Name']} (End: {p['et']}, Status: {p['status']})")

# Save projects for next step
with open('park_projects_2022.json', 'w') as f:
    json.dump(park_projects_2022, f, indent=2)

print("\nPark projects saved to park_projects_2022.json")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

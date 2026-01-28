code = """import json
import re

# Load the civic documents data
civic_docs_path = var_functions.query_db:5
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Total documents: {len(civic_docs)}")

# Extract project information from text
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Disaster projects often have (FEMA Project), (CalJPIA Project), or (CalOES Project) suffix
    
    # Find lines that might contain project names
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Check if line contains disaster project indicators
        if any(indicator in line for indicator in ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)']):
            # This is likely a disaster project
            project_name = line.strip()
            
            # Look for date patterns in nearby lines
            # Search for "2022" in the text around this project
            context_window = 1000  # characters before and after
            start_pos = text.find(project_name)
            if start_pos >= 0:
                context_start = max(0, start_pos - context_window)
                context_end = min(len(text), start_pos + len(project_name) + context_window)
                context = text[context_start:context_end]
                
                # Look for start date patterns
                start_patterns = [
                    r'(\d{4}-\w+)',
                    r'(\d{4}-\d{1,2})',
                    r'Start\s*:\s*(\S+)',
                    r'Begin\s*:?\s*(\S+)',
                ]
                
                st = None
                for pattern in start_patterns:
                    matches = re.findall(pattern, context)
                    for match in matches:
                        if '2022' in str(match):
                            st = str(match)
                            break
                    if st:
                        break
                
                # Determine topic based on content
                topic = []
                if 'FEMA' in project_name or 'FEMA' in context:
                    topic.append('FEMA')
                if 'fire' in text.lower():
                    topic.append('fire')
                if 'emergency' in context.lower():
                    topic.append('emergency')
                if 'storm' in context.lower():
                    topic.append('storm')
                if 'drainage' in context.lower():
                    topic.append('drainage')
                
                projects.append({
                    'project_name': project_name,
                    'type': 'disaster',
                    'topic': ','.join(topic) if topic else 'disaster',
                    'status': 'unknown',
                    'st': st,
                    'et': None,
                    'source_doc': filename
                })

# Print disaster projects with 2022 start dates
disaster_projects_2022 = [p for p in projects if p['st'] and '2022' in p['st']]

print(f"\nFound {len(disaster_projects_2022)} disaster projects that started in 2022:")
for p in disaster_projects_2022:
    print(f"- {p['project_name']}: {p['st']}")

# Also look for projects with 2022 in their name (like "2022 Morning View...")
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for patterns like "2022 ... Project" or "2022 ... Improvements"
    # that might be disaster-related
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('2022') and ('Project' in line or 'Improvements' in line):
            # Check if this is likely disaster-related
            if any(keyword in text.lower() for keyword in ['fema', 'fire', 'disaster', 'emergency', 'caloes', 'caljpia']):
                project_name = line
                
                # Look for start date
                st = None
                if '2022' in project_name:
                    # Extract the first part that contains 2022
                    parts = project_name.split()
                    for i, part in enumerate(parts):
                        if '2022' in part:
                            # Could be "2022-Spring" or just "2022"
                            if i+1 < len(parts) and '-' in part:
                                st = part
                            else:
                                st = '2022'
                            break
                
                topic = []
                if 'FEMA' in text:
                    topic.append('FEMA')
                if 'fire' in text.lower():
                    topic.append('fire')
                if 'storm' in text.lower():
                    topic.append('storm')
                if 'drainage' in text.lower():
                    topic.append('drainage')
                
                # Check if this project is already in our list
                exists = any(p['project_name'] == project_name for p in projects)
                if not exists:
                    projects.append({
                        'project_name': project_name,
                        'type': 'disaster',
                        'topic': ','.join(topic) if topic else 'disaster',
                        'status': 'unknown',
                        'st': st or '2022',
                        'et': None,
                        'source_doc': filename
                    })

# Re-filter after second pass
all_disaster_projects = [p for p in projects if p['type'] == 'disaster']
disaster_projects_2022 = [p for p in all_disaster_projects if p['st'] and '2022' in p['st']]

print(f"\nAfter second pass, found {len(disaster_projects_2022)} disaster projects that started in 2022:")
for p in disaster_projects_2022:
    print(f"- {p['project_name']}: {p['st']}")

# Output the projects for the next step
result = {
    'disaster_projects_2022': disaster_projects_2022,
    'all_disaster_projects': all_disaster_projects,
    'total_documents': len(civic_docs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

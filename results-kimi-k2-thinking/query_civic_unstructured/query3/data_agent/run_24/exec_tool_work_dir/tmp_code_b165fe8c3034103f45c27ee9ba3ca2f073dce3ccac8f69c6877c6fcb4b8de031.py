code = """import json
import os

# Read the MongoDB results
file_path = None
for key, value in locals().items():
    if 'functions.query_db:5' in key:
        file_path = value
        break

print("File path from storage:", file_path)

with open(file_path, 'r') as f:
    mongo_docs = json.load(f)

print(f"Found {len(mongo_docs)} documents")
print(f"First doc keys: {list(mongo_docs[0].keys()) if mongo_docs else 'No docs'}")

projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    section_type = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check for section headers
        if "Capital Improvement Projects (Design)" in line or "Disaster Recovery Projects (Design)" in line:
            section_type = "design"
            continue
        elif "Capital Improvement Projects (Construction)" in line or "Disaster Recovery Projects (Construction)" in line:
            section_type = "construction"
            continue
        elif "Capital Improvement Projects (Not Started)" in line or "Disaster Recovery Projects (Not Started)" in line:
            section_type = "not_started"
            continue
        
        # Look for project names
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('•') and not line.startswith('■') and not line.startswith('●'):
            if 'Updates:' not in line and 'Schedule:' not in line and 'Project Description:' not in line and 'Page' not in line:
                
                next_segment = '\n'.join(lines[i:i+4]) if i+4 < len(lines) else ''
                if 'Updates:' in next_segment or 'Schedule:' in next_segment or 'Project Description:' in next_segment:
                    
                    project_name = line.strip()
                    
                    topics = []
                    name_lower = project_name.lower()
                    text_lower = text.lower()
                    
                    if 'fema' in name_lower or 'fema' in text_lower:
                        topics.append('FEMA')
                    if 'emergency' in name_lower or 'emergency' in text_lower:
                        topics.append('emergency')
                    if 'fire' in name_lower:
                        topics.append('fire')
                    if 'storm' in name_lower or 'drainage' in name_lower or 'storm drain' in name_lower:
                        topics.append('drainage')
                    if 'warning' in name_lower or 'siren' in name_lower:
                        topics.append('emergency warning')
                    if 'road' in name_lower:
                        topics.append('road')
                    if 'park' in name_lower:
                        topics.append('park')
                    
                    project_type = 'disaster' if any(marker in project_name for marker in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']) else 'capital'
                    status = section_type if section_type else 'unknown'
                    if status == 'construction':
                        status = 'completed'
                    
                    projects.append({
                        'Project_Name': project_name,
                        'status': status,
                        'type': project_type,
                        'topics': topics,
                        'filename': filename
                    })

print(f"\nExtracted {len(projects)} projects")
print("\nAll extracted projects:")
for p in projects:
    print(f"- {p['Project_Name'][:80]} | status: {p['status']} | type: {p['type']} | topics: {p['topics']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import re

# Access the file path from the query result
file_info = locals()['var_functions.query_db:5']
print(f"Type: {type(file_info)}")
print(f"Value: {file_info[:200] if isinstance(file_info, str) else str(file_info)[:200]}")

# Read the MongoDB results
if isinstance(file_info, str):
    with open(file_info, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = file_info

print(f"\nFound {len(mongo_docs)} documents")
if mongo_docs:
    print(f"First doc keys: {list(mongo_docs[0].keys())}")
    print(f"Sample text preview: {mongo_docs[0].get('text', '')[:200]}")

# Extract projects from documents
projects = []

for doc_idx, doc in enumerate(mongo_docs):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    section_type = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        if any(phrase in line for phrase in [
            "Capital Improvement Projects (Design)",
            "Disaster Recovery Projects (Design)"
        ]):
            section_type = "design"
            continue
        elif any(phrase in line for phrase in [
            "Capital Improvement Projects (Construction)",
            "Disaster Recovery Projects (Construction)"
        ]):
            section_type = "construction"
            continue
        elif any(phrase in line for phrase in [
            "Capital Improvement Projects (Not Started)",
            "Disaster Recovery Projects (Not Started)"
        ]):
            section_type = "not_started"
            continue
        
        # Look for project names
        if (len(line) > 5 and not line.startswith('(') and not line.startswith('•') and 
            not line.startswith('■') and not line.startswith('●') and 'Updates:' not in line and 
            'Schedule:' not in line and 'Project Description:' not in line and 
            'Page' not in line):
            
            # Check if next lines contain project information
            next_segment = '\n'.join(lines[i:i+4])
            if 'Updates:' in next_segment or 'Schedule:' in next_segment or 'Project Description:' in next_segment:
                
                # This appears to be a project name
                project_name = line.strip()
                
                # Determine topics
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
                
                # Determine type based on name and context
                project_type = 'disaster' if any(marker in project_name for marker in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']) else 'capital'
                
                # Determine status from section
                status = section_type if section_type else 'unknown'
                if status == 'construction':
                    status = 'completed'  # Construction projects are often completed or in progress
                
                projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'type': project_type,
                    'topics': topics,
                    'filename': filename
                })

print(f"\nExtracted {len(projects)} potential projects")

# Show sample
for p in projects[:10]:
    print(f"- {p['Project_Name'][:60]} | status: {p['status']} | type: {p['type']} | topics: {p['topics']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

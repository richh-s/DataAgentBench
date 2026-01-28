code = """import json
import re

# Read the full MongoDB query result
mongo_file_path = var_functions.query_db:2
with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

print(f"Found {len(mongo_docs)} documents related to 'emergency' or 'FEMA'")

# Extract project information from the documents
projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into lines for easier parsing
    lines = text.split('\n')
    
    current_project = None
    
    # Look for project patterns
    # Common patterns:
    # - Project names are often on their own line
    # - Status indicators like "(Design)", "(Construction)", "(Not Started)"
    # - FEMA/CalOES/CalJPIA indicators
    
    project_patterns = [
        r'^([A-Z0-9][^\n]*?(?:FEMA|CalOES|CalJPIA|Tiger Team)[^\n]*)$',
        r'^([A-Z0-9][^\n]*?(?:Emergency|Disaster|Recovery)[^\n]*)$',
        r'^([A-Z0-9][^\n]*?(?:Storm Drain|Drainage|Culvert|Bridge|Road|Fire)[^\n]*)$'
    ]
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line looks like a project name
        if (line.isupper() or 
            line.startswith('202') or 
            '(' in line or
            any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Replacement'])):
            
            # Check if it mentions emergency/FEMA/disaster keywords
            if any(keyword.lower() in line.lower() for keyword in ['fema', 'emergency', 'disaster', 'recovery', 'caloes', 'caljpia', 'warning sirens', 'outdoor warning']):
                current_project = line
                print(f"Found potential project: {line[:100]}...")
                
                # Determine project type based on keywords
                project_type = None
                if any(k in line.lower() for k in ['fema', 'caloes', 'caljpia', 'disaster', 'recovery']):
                    project_type = 'disaster'
                elif any(k in line.lower() for k in ['capital', 'improvement', 'infrastructure']):
                    project_type = 'capital'
                else:
                    project_type = 'disaster'  # Default for emergency-related projects
                
                # Determine status (this is a simplification - in reality we'd look for context)
                status = 'design'  # Default assumption
                
                # Determine topics
                topics = []
                if 'fema' in line.lower():
                    topics.append('FEMA')
                if 'emergency' in line.lower():
                    topics.append('emergency')
                if 'disaster' in line.lower():
                    topics.append('disaster')
                if 'warning' in line.lower() or 'siren' in line.lower():
                    topics.append('emergency warning')
                if 'drain' in line.lower():
                    topics.append('storm drain')
                if 'fire' in line.lower():
                    topics.append('fire')
                
                projects.append({
                    'Project_Name': current_project,
                    'topics': ','.join(topics),
                    'status': status,
                    'type': project_type,
                    'filename': filename
                })

print(f"\nExtracted {len(projects)} projects with emergency/FEMA keywords")
for proj in projects[:5]:
    print(f"  - {proj['Project_Name'][:60]}...")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

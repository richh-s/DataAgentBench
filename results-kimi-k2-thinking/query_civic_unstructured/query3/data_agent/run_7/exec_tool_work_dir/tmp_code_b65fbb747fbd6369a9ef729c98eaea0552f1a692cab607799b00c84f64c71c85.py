code = """import json
import re

# Read the full MongoDB query result
mongo_file_path = var_functions.query_db:2
with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

print("Found documents count:", len(mongo_docs))

# Extract project information from the documents
projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into lines for easier parsing
    lines = text.split('\n')
    
    # Keywords to look for
    keywords = ['fema', 'emergency', 'disaster', 'recovery', 'caloes', 'caljpia', 'warning sirens', 'outdoor warning']
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line contains emergency/FEMA keywords
        if any(keyword in line.lower() for keyword in keywords):
            # Check if it looks like a project name
            if (line.isupper() or '(' in line or 'Project' in line or 'Improvements' in line or 
                'Repairs' in line or 'Replacement' in line or line.startswith('202')):
                
                current_project = line
                
                # Determine project type
                project_type = 'disaster'
                if 'capital' in line.lower() and 'improvement' in line.lower():
                    project_type = 'capital'
                
                # Determine status
                status = 'design'
                
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
                
                if topics:
                    projects.append({
                        'Project_Name': current_project,
                        'topics': ','.join(topics),
                        'status': status,
                        'type': project_type,
                        'filename': filename
                    })

print("Extracted projects count:", len(projects))
print("First few projects:")
for proj in projects[:3]:
    print("  Project:", proj['Project_Name'][:60])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

code = """import json
import re

# Load the MongoDB query result
mongo_result = locals()['var_functions.query_db:0']

# If it's a file path, read from file
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        documents = json.load(f)
else:
    documents = mongo_result

print(f"Number of documents found: {len(documents)}")
print(f"First document filename: {documents[0].get('filename')}")

# Let's inspect the first document's text to understand the structure
sample_text = documents[0].get('text', '')[:2000]
print("\nSample text (first 2000 chars):")
print(sample_text)

# Let's look for patterns that might indicate project names and statuses
# Based on the sample, we see patterns like:
# "Latigo Canyon Road Retaining Wall Repair Project" with status "Awaiting final FEMA/CalOES approval"
# Disaster projects often have (FEMA Project) suffix

# Let's extract potential project information
projects = []

for doc in documents:
    text = doc.get('text', '')
    
    # Look for disaster projects first (those with FEMA/FEMA-related patterns)
    # Pattern 1: Project names with (FEMA Project) or similar suffixes
    fema_pattern = r'([A-Za-z\s&\-]+?\s*\(FEMA\s+[^\)]+\))'
    caljpia_pattern = r'([A-Za-z\s&\-]+?\s*\(CalJPIA\s+[^\)]+\))'
    caloes_pattern = r'([A-Za-z\s&\-]+?\s*\(CalOES\s+[^\)]+\))'
    
    # Also look for projects with "emergency" or "FEMA" in the name
    emergency_patterns = [
        fema_pattern,
        caljpia_pattern,
        caloes_pattern,
        r'([A-Za-z\s\-]*Emergency[A-Za-z\s\-]*Project)',
        r'([A-Za-z\s\-]*FEMA[A-Za-z\s\-]*Project)',
    ]
    
    for pattern in emergency_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            project_name = match.strip()
            # Try to find status near this project name
            # Look for status keywords after the project name
            after_text = text[text.find(project_name):text.find(project_name)+500]
            
            status = None
            if 'completed' in after_text.lower():
                status = 'completed'
            elif 'design' in after_text.lower() or 'planning' in after_text.lower():
                status = 'design'
            elif 'not started' in after_text.lower():
                status = 'not started'
            elif 'construction' in after_text.lower() or 'under construction' in after_text.lower():
                # Check if it's completed or in progress
                if 'complete construction' in after_text.lower() or 'completed' in after_text.lower():
                    status = 'completed'
                else:
                    status = 'design'  # or some other status
            
            # Determine type
            proj_type = 'disaster'  # Since they're FEMA/emergency related
            
            # Determine topic
            topic = 'emergency, FEMA'
            if 'fire' in project_name.lower():
                topic += ', fire'
            elif 'drainage' in project_name.lower() or 'storm' in project_name.lower():
                topic += ', drainage'
            elif 'road' in project_name.lower():
                topic += ', road'
            
            projects.append({
                'Project_Name': project_name,
                'topic': topic,
                'type': proj_type,
                'status': status,
                'source_file': doc.get('filename')
            })
    
    # Also look for "Outdoor Warning Signs" which is mentioned as emergency-related
    if 'warning signs' in text.lower() or 'warning siren' in text.lower():
        # Find the context around this
        warning_matches = re.finditer(r'Outdoor Warning Signs[^
]*', text)
        for match in warning_matches:
            project_name = match.group().strip()
            if project_name:
                # Find status
                start = match.start()
                after_text = text[start:start+500]
                
                status = None
                if 'completed' in after_text.lower():
                    status = 'completed'
                elif 'design' in after_text.lower():
                    status = 'design'
                else:
                    status = 'not started'
                
                projects.append({
                    'Project_Name': project_name,
                    'topic': 'emergency warning',
                    'type': 'disaster',
                    'status': status,
                    'source_file': doc.get('filename')
                })

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in projects:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

print(f"\nExtracted {len(unique_projects)} unique emergency/FEMA projects:")
for proj in unique_projects:
    print(f"- {proj['Project_Name']}: status={proj['status']}, type={proj['type']}")

# Save for next step
result = json.dumps(unique_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

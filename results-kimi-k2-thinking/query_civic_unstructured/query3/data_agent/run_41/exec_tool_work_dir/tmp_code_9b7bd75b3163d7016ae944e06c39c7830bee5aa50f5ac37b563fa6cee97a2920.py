code = """import json
import re

# Load the MongoDB query result
mongo_result = locals()['var_functions.query_db:0']

# Parse the result
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        documents = json.load(f)
else:
    documents = mongo_result

print(f"Number of documents found: {len(documents)}")

# Initialize projects list
projects = []

# Define patterns for disaster/emergency projects
disaster_patterns = [
    r'([A-Za-z][A-Za-z0-9\s\-&\(\)]+)\(FEMA[^\)]*\)',  # Projects ending with (FEMA ...)
    r'([A-Za-z][A-Za-z0-9\s\-&\(\)]+)\(CalJPIA[^\)]*\)',  # Projects ending with (CalJPIA ...)
    r'([A-Za-z][A-Za-z0-9\s\-&\(\)]+)\(CalOES[^\)]*\)',  # Projects ending with (CalOES ...)
]

status_keywords = {
    'completed': ['completed', 'complete construction', 'notice of completion', 'construction was completed'],
    'design': ['design', 'planning', 'working with consultant', 'plans are being finalized', 'rfq/p', 'rfp'],
    'not started': ['not started', 'identified', 'waiting for', 'pending'],
    'construction': ['construction', 'under construction', 'construction bids']
}

def find_project_status(text):
    """Determine project status from text"""
    text_lower = text.lower()
    
    # Check for completed first (highest priority)
    for keyword in status_keywords['completed']:
        if keyword in text_lower:
            return 'completed'
    
    # Check for not started
    for keyword in status_keywords['not started']:
        if keyword in text_lower:
            return 'not started'
    
    # Check for design/planning
    for keyword in status_keywords['design']:
        if keyword in text_lower:
            return 'design'
    
    # Check for construction (but not yet completed)
    for keyword in status_keywords['construction']:
        if keyword in text_lower and 'completed' not in text_lower:
            return 'design'  # Treat as design phase if not completed
    
    return 'unknown'

def extract_topic_from_name(project_name):
    """Extract topic keywords from project name"""
    topic_parts = ['emergency', 'fema']
    name_lower = project_name.lower()
    
    if 'fire' in name_lower:
        topic_parts.append('fire')
    if 'drainage' in name_lower or 'storm drain' in name_lower:
        topic_parts.append('drainage')
    if 'road' in name_lower or 'street' in name_lower:
        topic_parts.append('road')
    if 'bridge' in name_lower:
        topic_parts.append('bridge')
    if 'warning' in name_lower or 'siren' in name_lower:
        topic_parts.append('emergency warning')
    if 'culvert' in name_lower:
        topic_parts.append('drainage')
    
    return ', '.join(set(topic_parts))

# Process each document
for doc in documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Find all disaster project patterns
    for pattern in disaster_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            project_name = match.group(0).strip()
            if len(project_name) > 10:  # Filter out very short matches
                # Find status
                status = find_project_status(text)
                
                # Extract topic
                topic = extract_topic_from_name(project_name)
                
                projects.append({
                    'Project_Name': project_name,
                    'topic': topic,
                    'type': 'disaster',
                    'status': status,
                    'source_file': filename
                })
    
    # Also look for Outdoor Warning Signs/Sirens projects
    warning_patterns = [
        r'Outdoor Warning Signs[^\n]*',
        r'Outdoor Warning Sirens[^\n]*'
    ]
    
    for pattern in warning_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            project_name = match.group(0).strip()
            if len(project_name) > 5 and 'outdoor' in project_name.lower():
                status = find_project_status(text)
                
                projects.append({
                    'Project_Name': project_name,
                    'topic': 'emergency warning',
                    'type': 'disaster',
                    'status': status,
                    'source_file': filename
                })

# Remove duplicates and normalize
unique_projects = {}
for proj in projects:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

result_projects = list(unique_projects.values())

print(f"Found {len(result_projects)} unique emergency/FEMA projects")
print(f"Sample projects:")
for p in result_projects[:5]:
    print(f"  - {p['Project_Name'][:80]}... status: {p['status']}")

result_json = json.dumps(result_projects)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

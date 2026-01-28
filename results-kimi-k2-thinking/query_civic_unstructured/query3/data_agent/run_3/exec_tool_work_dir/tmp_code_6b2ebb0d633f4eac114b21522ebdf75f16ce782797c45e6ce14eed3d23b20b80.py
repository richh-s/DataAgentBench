code = """import json
import re

# Read the file path from the storage variable
file_path = str(var_functions.query_db:2).strip()
print(f"File path: {file_path}")

# Read the JSON file
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Initialize list to store extracted projects
extracted_projects = []

# Debug info
print(f"Number of documents: {len(civic_docs_data)}")

# Function to extract project information from text
def extract_projects_from_text(text, filename):
    projects = []
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Look for potential project names
        project_indicators = ['Project', 'Road', 'Park', 'Drainage', 'Bridge', 'Highway', 'Walkway', 'Facility', 'Study']
        project_keywords = ['emergency', 'FEMA', 'fire', 'warning', 'drainage', 'storm', 'road', 'park', 'bridge', 'highway']
        
        # Check if line contains relevant keywords for emergency/FEMA projects
        line_lower = line.lower()
        has_emergency_or_fema = 'emergency' in line_lower or 'fema' in line_lower or 'fire' in line_lower
        has_general_indicators = any(indicator in line for indicator in project_indicators)
        
        if has_emergency_or_fema or has_general_indicators:
            # Look for updates/schedule patterns in nearby lines
            chunk_start = max(0, i-2)
            chunk_end = min(len(lines), i+20)
            chunk = '\n'.join(lines[chunk_start:chunk_end])
            
            # Check for project-like structure with updates/schedule
            if ('Updates:' in chunk or 'Project Schedule:' in chunk or 
                'Construction' in chunk or 'Design' in chunk):
                
                # Determine project type
                project_type = 'unknown'
                if 'FEMA' in chunk:
                    project_type = 'disaster'
                elif any(keyword in line_lower for keyword in ['road', 'park', 'bridge', 'highway', 'walkway']):
                    project_type = 'capital'
                
                # Determine status
                status = 'unknown'
                if 'under construction' in chunk:
                    status = 'construction'
                elif 'Construction was completed' in chunk:
                    status = 'completed'
                elif 'Complete Design:' in chunk or 'Design' in chunk:
                    status = 'design'
                elif 'Advertise:' in chunk or 'Project Schedule:' in chunk:
                    status = 'design'
                
                # Extract topics
                topics = []
                if 'emergency' in line_lower or 'emergency' in chunk.lower():
                    topics.append('emergency')
                if 'FEMA' in chunk:
                    topics.append('FEMA')
                if 'fire' in line_lower or 'fire' in chunk.lower():
                    topics.append('fire')
                if 'warning' in line_lower:
                    topics.append('emergency warning')
                if 'drainage' in line_lower or 'storm' in line_lower or 'drainage' in chunk.lower():
                    topics.append('drainage')
                    topics.append('storm drain')
                
                # Only add projects with emergency/FEMA topics
                if topics:
                    projects.append({
                        'Project_Name': line.strip(),
                        'topic': ', '.join(topics),
                        'type': project_type,
                        'status': status,
                        'source_file': filename
                    })
        
        i += 1
    
    return projects

# Extract projects from all documents
for doc in civic_docs_data:
    if isinstance(doc, dict) and 'text' in doc:
        filename = doc.get('filename', '')
        # Only process documents that mention emergency or FEMA
        text_lower = doc['text'].lower()
        if 'emergency' in text_lower or 'fema' in text_lower or 'fire' in text_lower:
            projects = extract_projects_from_text(doc['text'], filename)
            extracted_projects.extend(projects)

print(f"Extracted {len(extracted_projects)} projects")

# Create result
result = {
    'projects': extracted_projects,
    'count': len(extracted_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)

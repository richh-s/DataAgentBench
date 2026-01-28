code = """import json
import re

# Access the file path from storage
file_path_key = 'var_functions.query_db:2'
file_path = locals()[file_path_key]

# Read the JSON file
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Initialize list to store extracted projects
extracted_projects = []

# Debug info
print(f'Number of documents: {len(civic_docs_data)}')

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
            
        # Check for emergency/FEMA related keywords
        line_lower = line.lower()
        has_relevant_keywords = ('emergency' in line_lower or 'fema' in line_lower or 
                                'fire' in line_lower)
        
        # Also check for common project types that might have emergency/FEMA context
        has_project_indicators = any(indicator in line for indicator in 
                                    ['Project', 'Road', 'Park', 'Drainage', 'Bridge', 
                                     'Highway', 'Walkway', 'Facility', 'Study'])
        
        if has_relevant_keywords or has_project_indicators:
            # Look ahead to see if this is a project with updates/schedule
            chunk_start = max(0, i-2)
            chunk_end = min(len(lines), i+25)
            chunk = ' | '.join(lines[chunk_start:chunk_end])
            
            # Check for project structure
            if ('Updates:' in chunk or 'Project Schedule:' in chunk or 
                'under construction' in chunk or 'Construction was completed' in chunk):
                
                # Determine status
                status = 'unknown'
                if 'under construction' in chunk:
                    status = 'construction'
                elif 'Construction was completed' in chunk:
                    status = 'completed'
                elif 'Complete Design:' in chunk:
                    status = 'design'
                elif 'Project Schedule:' in chunk:
                    status = 'design'
                
                # Determine type
                project_type = 'unknown'
                if 'FEMA' in chunk:
                    project_type = 'disaster'
                elif any(keyword in line_lower for keyword in ['road', 'park', 'bridge', 'highway', 'walkway']):
                    project_type = 'capital'
                
                # Determine topics
                topics = []
                if 'emergency' in chunk.lower():
                    topics.append('emergency')
                if 'FEMA' in chunk:
                    topics.append('FEMA')
                if 'fire' in chunk.lower():
                    topics.append('fire')
                if 'warning' in chunk.lower():
                    topics.append('emergency warning')
                
                # Only include projects with emergency/FEMA/fire topics
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
        text = doc['text']
        filename = doc.get('filename', '')
        
        # Only process documents mentioning emergency, FEMA, or fire
        text_lower = text.lower()
        if 'emergency' in text_lower or 'fema' in text_lower or 'fire' in text_lower:
            projects = extract_projects_from_text(text, filename)
            extracted_projects.extend(projects)

print(f'Extracted {len(extracted_projects)} projects')

# Create result
result = {
    'projects': extracted_projects,
    'count': len(extracted_projects)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)

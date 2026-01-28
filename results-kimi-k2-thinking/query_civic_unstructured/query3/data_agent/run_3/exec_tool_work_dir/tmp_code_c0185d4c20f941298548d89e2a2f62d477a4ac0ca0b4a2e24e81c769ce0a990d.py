code = """import json, re

# The file path should be in storage under key var_functions.query_db:2
storage_key = 'var_functions.query_db:2'
file_path = globals().get(storage_key) or locals().get(storage_key)

# Read the JSON file
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Initialize list to store extracted projects
extracted_projects = []

print(f'Number of documents: {len(civic_docs_data)}')

# Function to extract project information
def extract_projects(text, filename):
    projects = []
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        line_lower = line.lower()
        text_chunk = ' '.join(lines[max(0,i-2):min(len(lines),i+20)])
        
        # Check for emergency/FEMA/fire content
        if ('emergency' in line_lower or 'fema' in line_lower or 'fire' in line_lower):
            if ('Updates:' in text_chunk or 'Project Schedule:' in text_chunk or 
                'under construction' in text_chunk):
                
                # Determine status and type
                status = 'unknown'
                if 'under construction' in text_chunk:
                    status = 'construction'
                elif 'Construction was completed' in text_chunk:
                    status = 'completed'
                elif 'Complete Design:' in text_chunk:
                    status = 'design'
                elif 'Project Schedule:' in text_chunk:
                    status = 'design'
                
                project_type = 'disaster' if 'FEMA' in text_chunk else 'capital'
                
                # Extract topics
                topics = []
                if 'emergency' in text_chunk.lower():
                    topics.append('emergency')
                if 'FEMA' in text_chunk:
                    topics.append('FEMA')
                if 'fire' in text_chunk.lower():
                    topics.append('fire')
                if 'warning' in text_chunk.lower():
                    topics.append('emergency warning')
                
                if topics:
                    projects.append({
                        'Project_Name': line,
                        'topic': ', '.join(topics),
                        'type': project_type,
                        'status': status,
                        'source_file': filename
                    })
    return projects

# Process all documents
for doc in civic_docs_data:
    if isinstance(doc, dict) and 'text' in doc:
        text = doc['text']
        filename = doc.get('filename', '')
        if any(kw in text.lower() for kw in ['emergency', 'fema', 'fire']):
            extracted_projects.extend(extract_projects(text, filename))

print(f'Extracted {len(extracted_projects)} projects')

# Output results
result = {'projects': extracted_projects, 'count': len(extracted_projects)}
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)

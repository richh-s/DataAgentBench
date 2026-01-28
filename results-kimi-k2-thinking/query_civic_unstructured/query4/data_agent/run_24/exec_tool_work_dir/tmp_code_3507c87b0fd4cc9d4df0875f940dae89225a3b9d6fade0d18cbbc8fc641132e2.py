code = """import json
import re

# Load the civic documents from the file
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    documents = json.load(f)

print(f"Loaded {len(documents)} documents")

# Examine the first document to understand structure
first_doc = documents[0]
print(f"First doc filename: {first_doc.get('filename')}")

# Function to extract project information from text
projects = []

for doc in documents:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names - capitalized lines with project indicators
        if line and len(line) > 10:
            project_indicators = ['Project', 'Improvements', 'Repairs', 'Facility', 'Park', 'Road', 'Drainage', 'Bridge', 'Playground', 'Treatment', 'Wall', 'Study', 'System', 'Lane', 'Structure']
            has_indicator = any(indicator.lower() in line.lower() for indicator in project_indicators)
            is_capitalized = line[0].isupper()
            
            if has_indicator and is_capitalized and not line.startswith('(') and not line.startswith('*'):
                project_name = line
                
                # Look for Spring 2022 date information in following lines
                start_date = None
                
                for j in range(i+1, min(i+8, len(lines))):
                    next_line = lines[j].strip()
                    
                    # Look for date patterns with Spring 2022
                    if '2022' in next_line and ('Spring' in next_line or 'March' in next_line or 'April' in next_line or 'May' in next_line):
                        if any(keyword in next_line for keyword in ['Advertise', 'Begin', 'Start', 'Complete', 'Design']):
                            # Try to extract a clean date reference
                            date_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', 'Spring 2022']
                            for pattern in date_patterns:
                                if pattern in next_line:
                                    start_date = pattern
                                    break
                
                if start_date:
                    projects.append(project_name)
                    print(f"Found project with Spring 2022: {project_name} - {start_date}")

print(f"\nTotal projects with Spring 2022 start: {len(projects)}")
print("Projects found:", projects[:10])  # Show first 10

result_json = json.dumps({"count": len(projects), "projects": projects})
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

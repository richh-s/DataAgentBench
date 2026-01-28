code = """import json
import re

# Read the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Debug: print the number of documents and first document structure
print(f"Number of documents: {len(civic_docs_data)}")
if civic_docs_data:
    print(f"First document keys: {list(civic_docs_data[0].keys())}")
    print(f"First document filename: {civic_docs_data[0].get('filename')}")

# Initialize list to store extracted projects
extracted_projects = []

# Function to extract project information from text
def extract_projects_from_text(text, filename):
    projects = []
    
    # Look for project patterns in the text
    # Pattern 1: Project names followed by updates/schedule
    # Look for lines that seem like project names (title case, often include location)
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Look for potential project names (capitalized, often include words like Project, Road, Park, etc.)
        # and check if they have associated updates or schedules
        project_indicators = ['Project', 'Road', 'Park', 'Drainage', 'Bridge', 'Highway', 'Walkway', 'Facility', 'Study']
        project_keywords = ['emergency', 'FEMA', 'fire', 'warning', 'drainage', 'storm', 'road', 'park', 'bridge', 'highway']
        
        # Check if line looks like a project name
        if (any(indicator in line for indicator in project_indicators) or 
            any(keyword.lower() in line.lower() for keyword in project_keywords)):
            
            # Check if next lines contain updates or schedules
            next_lines = []
            j = i + 1
            while j < len(lines) and j < i + 10:  # Look ahead up to 10 lines
                next_line = lines[j].strip()
                if next_line:
                    next_lines.append(next_line)
                if 'Project Schedule:' in next_line or 'Updates:' in next_line:
                    break
                j += 1
            
            # If we found updates or schedule, this is likely a project
            if any('Updates:' in nl for nl in next_lines) or any('Project Schedule:' in nl for nl in next_lines):
                # Extract project name (clean up)
                project_name = line.strip()
                
                # Extract status from the content
                status = "unknown"
                if 'Updates: Project is currently under construction' in text[i:min(i+20, len(lines))]:
                    status = "construction"
                elif 'Construction was completed' in text[i:min(i+20, len(lines))]:
                    status = "completed"
                elif 'Complete Design:' in text or 'Project Schedule:' in text[i:min(i+20, len(lines))]:
                    status = "design"
                elif 'Not Started' in text or 'identified' in text:
                    status = "not started"
                
                # Determine type based on keywords
                project_type = "unknown"
                if 'FEMA' in line or 'FEMA' in text[i:min(i+30, len(lines))]:
                    project_type = "disaster"
                    status = "design"  # Most FEMA projects are in design
                elif any(capital in line.lower() for capital in ['road', 'park', 'bridge', 'drainage', 'highway', 'walkway']):
                    project_type = "capital"
                
                # Extract topics
                topics = []
                if 'emergency' in line.lower() or 'emergency' in text[i:min(i+30, len(lines))].lower():
                    topics.append('emergency')
                if 'FEMA' in line or 'FEMA' in text[i:min(i+30, len(lines))]:
                    topics.append('FEMA')
                if 'fire' in line.lower() or 'fire' in text[i:min(i+30, len(lines))].lower():
                    topics.append('fire')
                if 'warning' in line.lower():
                    topics.append('emergency warning')
                if 'drainage' in line.lower() or 'storm' in line.lower():
                    topics.append('drainage')
                    topics.append('storm drain')
                if 'road' in line.lower():
                    topics.append('road')
                if 'park' in line.lower():
                    topics.append('park')
                if 'highway' in line.lower():
                    topics.append('highway')
                if 'bridge' in line.lower():
                    topics.append('bridge')
                
                # Only add if it has relevant topics
                if topics:
                    projects.append({
                        'Project_Name': project_name,
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
        projects = extract_projects_from_text(doc['text'], doc.get('filename', ''))
        extracted_projects.extend(projects)

# Debug: print extracted projects
print(f"\nExtracted {len(extracted_projects)} projects:")
for proj in extracted_projects[:10]:
    print(f"  - {proj['Project_Name']}: {proj['topic']}, {proj['type']}, {proj['status']}")

# Store results in a way we can access later
result = {
    'extracted_projects': extracted_projects,
    'total_docs': len(civic_docs_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)

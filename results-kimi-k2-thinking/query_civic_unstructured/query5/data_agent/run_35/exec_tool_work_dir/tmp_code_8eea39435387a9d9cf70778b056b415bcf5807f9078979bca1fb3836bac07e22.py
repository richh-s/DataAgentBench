code = """import json
import re
from datetime import datetime

# Read the civic documents from the file
file_path = '/tmp/tmp8d3h4c3e.json'
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")

# Let's examine the structure of the first document
if civic_docs:
    print("\nFirst document structure:")
    print(f"_id: {civic_docs[0].get('_id')}")
    print(f"filename: {civic_docs[0].get('filename')}")
    print(f"Text preview (first 500 chars): {civic_docs[0].get('text', '')[:500]}")

# Now let's try to extract project information from the text
# We'll look for patterns that indicate project information

def extract_projects_from_text(text):
    """Extract project information from document text"""
    projects = []
    
    # Look for project sections - they often appear with bullet points or specific markers
    # Disaster projects often have (FEMA Project), (CalJPIA Project), or (CalOES Project) suffixes
    
    # Split text into lines for easier processing
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names with disaster-related suffixes
        # Common patterns: "Project Name (FEMA Project)" or similar
        disaster_suffixes = ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)']
        
        for suffix in disaster_suffixes:
            if suffix in line and len(line.strip()) < 200:  # Likely a project name/title
                # This is likely a disaster project
                project_name = line.strip()
                
                # Initialize project info
                project_info = {
                    'Project_Name': project_name,
                    'type': 'disaster',
                    'topic': 'disaster,FEMA',
                    'status': 'unknown',
                    'st': None,
                    'et': None,
                    'source_line': line
                }
                
                # Look for status information nearby
                # Common status indicators
                status_indicators = {
                    'design': ['design', 'planning', 'plan', 'development'],
                    'completed': ['completed', 'construction was completed', 'notice of completion'],
                    'not started': ['not started', 'identified', 'future', 'pending']
                }
                
                # Look ahead and behind for status
                for j in range(max(0, i-3), min(len(lines), i+4)):
                    check_line = lines[j].lower()
                    
                    for status, keywords in status_indicators.items():
                        if any(keyword in check_line for keyword in keywords):
                            project_info['status'] = status
                            break
                
                # Look for date information (st/et)
                # Look for patterns like "2022-Spring", "2022-Fall", "2022-02", "2022-March"
                # Also "Complete Design: Summer 2023", "Begin Construction: Fall 2023", etc.
                
                # Search nearby lines for date patterns
                date_patterns = [
                    r'\b(202[0-9])[-\s]?(Spring|Summer|Fall|Winter|[A-Za-z]+)\b',
                    r'\b(202[0-9])[-\s]?([0-1]?[0-9])\b',  # 2022-02 format
                    r'\b(202[0-9])\b'  # Just the year
                ]
                
                for j in range(max(0, i-5), min(len(lines), i+6)):
                    check_line = lines[j]
                    
                    # Look for start/completion dates
                    if any(keyword in check_line.lower() for keyword in ['begin', 'start', 'complete', 'construction', 'design']):
                        for pattern in date_patterns:
                            matches = re.findall(pattern, check_line, re.IGNORECASE)
                            if matches:
                                for match in matches:
                                    year = match[0]
                                    # If we find a 2022 date and it's associated with start/begin, mark it
                                    if '2022' in year:
                                        if any(kw in check_line.lower() for kw in ['begin', 'start', 'advertise', 'design']):
                                            if not project_info['st']:
                                                project_info['st'] = f"{year}-{match[1] if len(match) > 1 else ''}".rstrip('-')
                                        elif any(kw in check_line.lower() for kw in ['complete', 'finish', 'end']):
                                            if not project_info['et']:
                                                project_info['et'] = f"{year}-{match[1] if len(match) > 1 else ''}".rstrip('-')
                
                # If we found date info in the line itself
                for pattern in date_patterns:
                    matches = re.findall(pattern, line, re.IGNORECASE)
                    if matches:
                        for match in matches:
                            year = match[0]
                            if '2022' in year and not project_info['st']:
                                project_info['st'] = f"{year}-{match[1] if len(match) > 1 else ''}".rstrip('-')
                
                projects.append(project_info)
                break  # Found a disaster project, move to next line
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    all_projects.extend(projects)

print(f"\nTotal projects extracted: {len(all_projects)}")

# Filter for disaster projects that started in 2022
disaster_projects_2022 = []
for proj in all_projects:
    if proj['type'] == 'disaster' and proj['st'] and '2022' in proj['st']:
        disaster_projects_2022.append(proj)

print(f"\nDisaster projects starting in 2022: {len(disaster_projects_2022)}")

# Display the projects found
for proj in disaster_projects_2022:
    print(f"- {proj['Project_Name']}")
    print(f"  Status: {proj['status']}, Start: {proj['st']}")
    print()

# Pass the results to the next step
result = {
    'all_projects': all_projects,
    'disaster_projects_2022': disaster_projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

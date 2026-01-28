code = """import json
import re

# Load the MongoDB documents file
mongo_file = locals()['var_functions.query_db:0']
with open(mongo_file, 'r') as f:
    documents = json.load(f)

# Extract project information from documents
projects = []

# Regular expressions to extract project information
for doc in documents:
    text = doc.get('text', '')
    
    # Look for project patterns
    # Capital projects
    capital_patterns = [
        r'Capital Improvement Projects\s*\((\w+)\)\s*\n\n([^\n]+)',
        r'Capital Improvement Projects[^\n]*\n([^\n]+)\s*\n\s*\\(cid:\w+\\)\s*(\w+)\s*:\s*([\w\s-]+)',
        r'([^\n]+)\s*\n\s*\\(cid:\w+\\)\s*Updates\s*:\s*\n((?:\s*\\\(cid:\w+\\\)\s*[^\n]+\n)+)',
    ]
    
    # Extract project names and details
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Find project names and related information
        if (line and not line.startswith('Public Works') and 
            not line.startswith('Commission') and 
            not line.startswith('To:') and 
            not line.startswith('Prepared') and 
            not line.startswith('Approved') and 
            not line.startswith('Date') and 
            not line.startswith('Meeting') and 
            not line.startswith('Subject:') and 
            not line.startswith('RECOMMENDED') and
            not line.startswith('DISCUSSION:') and
            not line.startswith('Page') and
            not line.startswith('Agenda') and
            not line.startswith('Capital Improvement Projects') and
            not line.startswith('Capital Improvement') and
            not line.startswith('To') and
            not line.startswith('From') and
            not any(word in line for word in ['Updates:', 'Project Schedule:', 'Project Description:', 'Project Updates:', 'Estimated Schedule:']) and
            len(line) > 5):
            
            # Check if this looks like a project name
            if i < len(lines) - 1:
                next_line = lines[i+1].strip() if i+1 < len(lines) else ''
                
                # Look for keywords that suggest this is a project
                project_indicators = [
                    'Project', 'Resurfacing', 'Improvements', 'Repairs', 'Drainage', 
                    'Structure', 'Replacement', 'Study', 'Phase', 'System', 'Screens'
                ]
                
                # Check current line or next line for project indicators
                has_indicator = any(indicator.lower() in line.lower() for indicator in project_indicators)
                
                if has_indicator:
                    # Extract schedule from surrounding lines
                    schedule_text = '\n'.join(lines[max(0, i-5):min(len(lines), i+10)])
                    
                    # Look for dates in schedule text
                    # Patterns to match: 2022-Spring, 2022-02, 2022-March, Spring 2022, etc.
                    date_matches = []
                    
                    # Look for Spring 2022 patterns
                    spring_patterns = [
                        r'2022-?Spring',
                        r'Spring\s*2022',
                        r'2022-[Mm]ar|2022-[Aa]pr|2022-[Mm]ay',
                        r'Complete\s+Design\s*:\s*Spring\s+2022',
                        r'Advertise\s*:\s*Spring\s+2022',
                        r'Begin\s+Construction\s*:\s*Spring\s+2022',
                    ]
                    
                    for pattern in spring_patterns:
                        if re.search(pattern, schedule_text, re.I):
                            project_info = {
                                'project_name': line,
                                'start_date': '2022-Spring',
                                'status': 'design',
                                'type': 'capital',
                                'topic': '',
                            }
                            
                            # Determine type from name
                            if any(word in line.lower() for word in ['fema', 'caloes', 'caljpia', 'fire', 'disaster']):
                                project_info['type'] = 'disaster'
                            
                            # Determine status by looking at context
                            if 'Complete Construction' in schedule_text:
                                project_info['status'] = 'completed'
                            elif 'Not Started' in text:
                                project_info['status'] = 'not started'
                            elif 'Design' in extract_section:
                                project_info['status'] = 'design'
                            
                            # Determine topic from keywords
                            if any(word in line.lower() for word in ['storm', 'drain']):
                                project_info['topic'] = 'storm drain'
                            elif any(word in line.lower() for word in ['park', 'playground']):
                                project_info['topic'] = 'park'
                            elif any(word in line.lower() for word in ['road', 'highway']):
                                project_info['topic'] = 'road'
                            elif 'emergency' in line.lower() or 'warning' in line.lower():
                                project_info['topic'] = 'emergency warning'
                            
                            projects.append(project_info)
                            break

print(f"Found {len(projects)} potential projects")

# Show what we found
for p in projects[:10]:
    print(f"Project: {p['project_name']}, Date: {p['start_date']}, Type: {p['type']}, Status: {p['status']}")

# Store the projects for now
projects_json = json.dumps(projects)
print('__RESULT__:')
print(projects_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

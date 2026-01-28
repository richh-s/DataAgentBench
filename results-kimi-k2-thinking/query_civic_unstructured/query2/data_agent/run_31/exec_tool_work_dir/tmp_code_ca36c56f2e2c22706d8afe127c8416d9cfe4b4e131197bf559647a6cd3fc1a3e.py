code = """import json
import re

# Read the full civic docs results
civic_docs_path = var_functions.query_db:2
civic_docs_full = []

with open(civic_docs_path, 'r') as f:
    civic_docs_full = json.load(f)

print(f"Total civic docs found: {len(civic_docs_full)}")

# Function to extract project information from text
def extract_projects_from_text(text, filename):
    projects = []
    
    # Look for project sections
    # Projects are typically listed with bullet points or specific formatting
    # Look for patterns like project names followed by status updates
    
    # Split text into lines for easier parsing
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names - often at the start of a section or after bullet points
        # Common patterns: project names that end with "Project" or contain location names
        
        # Check if this looks like a project name (title case, contains keywords, not a common phrase)
        if (len(line) > 10 and 
            (line.startswith('"') or 
             line.istitle() or 
             any(keyword in line.lower() for keyword in ['park', 'road', 'drain', 'bridge', 'project', 'improvements', 'repairs'])) and
            not any(phrase in line.lower() for phrase in ['city council', 'public works', 'commission meeting', 'agenda', 'prepared by', 'approved by'])):
            
            # If we were building a previous project, save it
            if current_project and project_info:
                project_info['project_name'] = current_project
                project_info['filename'] = filename
                projects.append(project_info)
            
            # Start new project
            current_project = line.strip('"').strip()
            project_info = {}
            
        # Look for status indicators
        if current_project:
            lower_line = line.lower()
            
            # Check for status
            if 'status:' in lower_line:
                if 'completed' in lower_line:
                    project_info['status'] = 'completed'
                elif 'design' in lower_line:
                    project_info['status'] = 'design'
                elif 'construction' in lower_line:
                    project_info['status'] = 'construction'
            elif 'updates:' in lower_line:
                # Look ahead for status in updates
                for j in range(i+1, min(i+5, len(lines))):
                    next_line = lines[j].lower()
                    if 'completed' in next_line:
                        project_info['status'] = 'completed'
                        # Look for completion date
                        if '2022' in next_line:
                            project_info['et'] = '2022'
                        elif '2023' in next_line:
                            project_info['et'] = '2023'
                        break
                    elif 'design' in next_line or 'planning' in next_line:
                        project_info['status'] = 'design'
                        break
                    elif 'construction' in next_line:
                        project_info['status'] = 'construction'
                        break
            
            # Look for completion dates
            if 'completed' in lower_line:
                project_info['status'] = 'completed'
                if '2022' in lower_line:
                    project_info['et'] = '2022'
                elif '2023' in lower_line:
                    project_info['et'] = '2023'
                elif '2021' in lower_line:
                    project_info['et'] = '2021'
            
            # Look for topic keywords
            if any(keyword in lower_line for keyword in ['park', 'drain', 'road', 'bridge', 'playground', 'walkway', 'slope', 'crosswalk']):
                if 'topic' not in project_info:
                    project_info['topic'] = []
                
                if 'park' in lower_line and 'park' not in project_info['topic']:
                    project_info['topic'].append('park')
                if 'drain' in lower_line and 'drain' not in project_info['topic']:
                    project_info['topic'].append('drain')
                if 'road' in lower_line and 'road' not in project_info['topic']:
                    project_info['topic'].append('road')
                if 'bridge' in lower_line and 'bridge' not in project_info['topic']:
                    project_info['topic'].append('bridge')
                if 'playground' in lower_line and 'playground' not in project_info['topic']:
                    project_info['topic'].append('playground')
                if 'walkway' in lower_line and 'walkway' not in project_info['topic']:
                    project_info['topic'].append('walkway')
                if 'slope' in lower_line and 'slope' not in project_info['topic']:
                    project_info['topic'].append('slope')
                if 'crosswalk' in lower_line and 'crosswalk' not in project_info['topic']:
                    project_info['topic'].append('crosswalk')
    
    # Add the last project
    if current_project and project_info:
        project_info['project_name'] = current_project
        project_info['filename'] = filename
        projects.append(project_info)
    
    return projects

# Extract projects from all documents
all_projects = []

for doc in civic_docs_full:
    projects = extract_projects_from_text(doc.get('text', ''), doc.get('filename', ''))
    all_projects.extend(projects)

print(f"Total projects extracted: {len(all_projects)}")

# Filter for park-related projects completed in 2022
park_completed_2022 = []

for proj in all_projects:
    # Check if it's park-related
    topics = proj.get('topic', [])
    is_park = 'park' in topics
    
    # Check status and completion year
    status = proj.get('status', '')
    end_time = proj.get('et', '')
    
    if is_park and status == 'completed' and '2022' in str(end_time):
        park_completed_2022.append(proj)

print(f"Park projects completed in 2022 found: {len(park_completed_2022)}")

for proj in park_completed_2022:
    print(f"- {proj['project_name']}")

# Save the filtered projects
filtered_projects_path = '/tmp/park_completed_2022.json'
with open(filtered_projects_path, 'w') as f:
    json.dump(park_completed_2022, f, indent=2)

print("__RESULT__:")
print(json.dumps({"filtered_projects_path": filtered_projects_path, "count": len(park_completed_2022)}))"""

env_args = {'var_functions.execute_python:0': {'collection': 'civic_docs', 'filter': {'text': {'$regex': 'park', '$options': 'i'}}, 'projection': {'filename': 1, 'text': 1}}, 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

code = """import json
import re

# Read the full civic docs results from the stored variable
civic_docs_full = locals().get('var_functions.query_db:2')

# If it's a string (file path), load it from the file
if isinstance(civic_docs_full, str):
    with open(civic_docs_full, 'r') as f:
        civic_docs_full = json.load(f)

print(f"Total civic docs found: {len(civic_docs_full)}")

# Function to extract project information from text
def extract_projects_from_text(text, filename):
    projects = []
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this looks like a project name
        if (len(line) > 10 and 
            (line.startswith('"') or line.istitle() or 
             any(keyword in line.lower() for keyword in ['park', 'road', 'drain', 'bridge', 'project', 'improvements', 'repairs'])) and
            not any(phrase in line.lower() for phrase in ['city council', 'public works', 'commission meeting', 'agenda', 'prepared by', 'approved by'])):
            
            # Save previous project if exists
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
                # Look ahead for status
                for j in range(i+1, min(i+5, len(lines))):
                    next_line = lines[j].lower()
                    if 'completed' in next_line:
                        project_info['status'] = 'completed'
                        if '2022' in next_line:
                            project_info['et'] = '2022'
                        elif '2023' in next_line:
                            project_info['et'] = '2023'
                        break
                    elif 'design' in next_line or 'planning' in next_line:
                        project_info['status'] = 'design'
                        break
                    elif 'construction' in next_line or 'under construction' in next_line:
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
                
                keywords_map = {
                    'park': 'park',
                    'drain': 'drain',
                    'road': 'road',
                    'bridge': 'bridge',
                    'playground': 'playground',
                    'walkway': 'walkway',
                    'slope': 'slope',
                    'crosswalk': 'crosswalk'
                }
                
                for key, value in keywords_map.items():
                    if key in lower_line and value not in project_info['topic']:
                        project_info['topic'].append(value)
    
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
    topics = proj.get('topic', [])
    is_park = 'park' in topics
    status = proj.get('status', '')
    end_time = proj.get('et', '')
    
    if is_park and status == 'completed' and '2022' in str(end_time):
        park_completed_2022.append(proj)

print(f"Park projects completed in 2022 found: {len(park_completed_2022)}")

for proj in park_completed_2022:
    print(f"- {proj['project_name']}")

# Store the results
result_data = {
    "park_completed_2022": park_completed_2022,
    "count": len(park_completed_2022),
    "project_names": [proj['project_name'] for proj in park_completed_2022]
}

print("__RESULT__:")
print(json.dumps(result_data))"""

env_args = {'var_functions.execute_python:0': {'collection': 'civic_docs', 'filter': {'text': {'$regex': 'park', '$options': 'i'}}, 'projection': {'filename': 1, 'text': 1}}, 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

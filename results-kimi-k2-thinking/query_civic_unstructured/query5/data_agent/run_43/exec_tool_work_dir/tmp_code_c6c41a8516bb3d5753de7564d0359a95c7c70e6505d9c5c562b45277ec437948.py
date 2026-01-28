code = """import json
import re
from collections import defaultdict

# Read the full result from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    documents = json.load(f)

print(f"Found {len(documents)} documents")

# Extract disaster-related projects with start dates in 2022
disaster_projects_2022 = []

for doc in documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Projects often start with a project name followed by updates/schedule
    project_patterns = [
        r'([A-Z][A-Za-z\s&\-]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study))\s*\(cid:\d+\)\s*Updates:',
        r'([A-Z][A-Za-z\s&\-]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study))\s*\(cid:\d+\)\s*Project Description:',
        r'([A-Z][A-Za-z\s&\-]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study))\s*Updates:',
    ]
    
    for pattern in project_patterns:
        projects = re.findall(pattern, text)
        for project_name in projects:
            project_name = project_name.strip()
            
            # Check if it's a disaster-related project
            is_disaster = False
            disaster_keywords = ['FEMA', 'fire', 'emergency', 'disaster', 'recovery', 'woolsey']
            for keyword in disaster_keywords:
                if keyword.lower() in project_name.lower() or keyword.lower() in text.lower():
                    is_disaster = True
                    break
            
            if is_disaster:
                # Look for start date information
                # Look for schedule patterns
                schedule_pattern = rf'{re.escape(project_name)}.*?Project Schedule:.*?(\d{{4}}[-\s]\w+)'
                schedule_match = re.search(schedule_pattern, text, re.DOTALL | re.IGNORECASE)
                
                if schedule_match:
                    date_str = schedule_match.group(1)
                    if '2022' in date_str:
                        disaster_projects_2022.append({
                            'project_name': project_name,
                            'filename': filename,
                            'start_date': date_str
                        })
                else:
                    # Alternative: look for any date after the project name
                    project_section = text[text.find(project_name):text.find(project_name)+2000]
                    date_patterns = [
                        r'Begin(?:ning)?\s*(?:Construction)?:\s*([A-Za-z\s]*2022)',
                        r'Complete\s*Design:\s*([A-Za-z\s]*2022)',
                        r'Advertise:\s*([A-Za-z\s]*2022)',
                        r'(2022[-\s][A-Za-z]+)',
                    ]
                    
                    for dp in date_patterns:
                        date_match = re.search(dp, project_section, re.IGNORECASE)
                        if date_match:
                            date_str = date_match.group(1)
                            if '2022' in date_str:
                                disaster_projects_2022.append({
                                    'project_name': project_name,
                                    'filename': filename,
                                    'start_date': date_str
                                })
                                break

print(f"Found {len(disaster_projects_2022)} disaster projects starting in 2022")
for proj in disaster_projects_2022[:10]:  # Show first 10
    print(f"- {proj['project_name']}: {proj['start_date']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

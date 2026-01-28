code = """import json
import re
from collections import defaultdict

# Read the full result from the file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    documents = json.load(f)

# Extract disaster-related projects with start dates in 2022
disaster_projects = []

for doc in documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check if document contains disaster-related keywords
    disaster_keywords = ['FEMA', 'fire', 'emergency', 'disaster', 'recovery', 'woolsey']
    is_disaster_doc = any(keyword.lower() in text.lower() for keyword in disaster_keywords)
    
    if is_disaster_doc:
        # Extract project names using multiple patterns
        patterns = [
            r'([A-Z][A-Za-z\s&\-\(\)]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study))\s*\(cid:\d+\)\s*Updates:',
            r'^\s*([A-Z][A-Za-z\s&\-\(\)]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study))\s*$'
        ]
        
        all_projects = []
        for pattern in patterns:
            matches = re.findall(pattern, text, re.MULTILINE)
            all_projects.extend(matches)
        
        all_projects = list(set(all_projects))  # Remove duplicates
        
        for project_name in all_projects:
            project_name = project_name.strip()
            if len(project_name) > 10:
                
                # Find project section in text
                proj_start = text.find(project_name)
                if proj_start == -1:
                    continue
                
                proj_section = text[proj_start:proj_start+2000]
                
                # Look for 2022 dates
                date_patterns = [
                    r'Begin(?:ning)?\s*(?:Construction)?:\s*([A-Za-z\s]*2022)',
                    r'Complete\s*Design:\s*([A-Za-z\s]*2022)',
                    r'Advertise:\s*([A-Za-z\s]*2022)',
                    r'(2022[-\s][A-Za-z]+)',
                    r'(Spring\s*2022)',
                    r'(Summer\s*2022)',
                    r'(Fall\s*2022)',
                    r'(Winter\s*2022)',
                ]
                
                project_start_date = None
                for dp in date_patterns:
                    date_match = re.search(dp, proj_section, re.IGNORECASE)
                    if date_match:
                        project_start_date = date_match.group(1).strip()
                        break
                
                if project_start_date:
                    disaster_projects.append({
                        'project_name': project_name,
                        'filename': filename,
                        'start_date': project_start_date
                    })

# Remove duplicates by project name
unique_projects = []
seen_names = set()
for proj in disaster_projects:
    if proj['project_name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['project_name'])

# Prepare result for JSON output
result = {
    'total_found': len(unique_projects),
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

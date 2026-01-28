code = """import json
import re
from collections import defaultdict

# Read the full result from the file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    documents = json.load(f)

print(f"Found {len(documents)} documents")

# Extract disaster-related projects with start dates in 2022
disaster_projects = []

for doc in documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for disaster-related keywords first
    disaster_keywords = ['FEMA', 'fire', 'emergency', 'disaster', 'recovery', 'woolsey']
    is_disaster_doc = any(keyword.lower() in text.lower() for keyword in disaster_keywords)
    
    if is_disaster_doc:
        # Extract project names - look for common patterns
        # Pattern 1: Project name followed by updates section
        pattern1 = r'([A-Z][A-Za-z\s&\-\(\)]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study))\s*\(cid:\d+\)\s*Updates:'
        
        # Pattern 2: Just the project name on its own line (common format)
        pattern2 = r'^\s*([A-Z][A-Za-z\s&\-\(\)]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study))\s*$'
        
        projects1 = re.findall(pattern1, text, re.MULTILINE)
        projects2 = re.findall(pattern2, text, re.MULTILINE)
        
        all_projects = list(set(projects1 + projects2))
        
        for project_name in all_projects:
            project_name = project_name.strip()
            if len(project_name) > 10:  # Filter out short/partial matches
                
                # Find the section of text related to this project
                proj_start = text.find(project_name)
                if proj_start == -1:
                    continue
                
                # Look ahead for project details (up to 2000 chars)
                proj_section = text[proj_start:proj_start+2000]
                
                # Check if it has a 2022 date
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
                        project_start_date = date_match.group(1)
                        break
                
                if project_start_date:
                    disaster_projects.append({
                        'project_name': project_name,
                        'filename': filename,
                        'start_date': project_start_date.strip()
                    })

# Remove duplicates and clean up
cleaned_projects = []
seen_names = set()
for proj in disaster_projects:
    name = proj['project_name']
    if name not in seen_names:
        cleaned_projects.append(proj)
        seen_names.add(name)

print(f"Found {len(cleaned_projects)} unique disaster projects with 2022 start dates")
for proj in cleaned_projects[:10]:
    print(f"- {proj['project_name']}: {proj['start_date']}")

# Save cleaned projects for next step
cleaned_projects_json = json.dumps(cleaned_projects, indent=2)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

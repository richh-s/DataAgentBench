code = """import re
import json

docs_filepath = locals()['var_function-call-10727724106832810456']
with open(docs_filepath, 'r') as f:
    docs_content = json.load(f)

projects_data = []

for doc in docs_content:
    text = doc['text']
    
    # Split the document by lines to process each line individually
    lines = text.splitlines()
    
    current_project_name = None
    current_project_status = None
    current_project_et = None

    for i, line in enumerate(lines):
        # Look for project names. They are often capitalized and followed by a specific pattern.
        # This regex tries to capture lines that look like a project title.
        project_name_match = re.search(r'^([A-Z][a-zA-Z0-9\s&\-]+(?:Project|Improvements|Repair|Plan|Study|Facility|System|Screens|Shade Structure|Green Streets|Quality)?[^\n]*?)\s*$', line)
        if project_name_match and not any(keyword in project_name_match.group(1) for keyword in ['RECOMMENDED ACTION', 'Subject:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'DISCUSSION:']):
            current_project_name = project_name_match.group(1).strip()
            current_project_status = None # Reset for a new project
            current_project_et = None # Reset for a new project

        # Look for status (completed) and end time (2022)
        if current_project_name:
            if re.search(r'Construction was completed.*2022', line, re.IGNORECASE):
                current_project_status = 'completed'
                et_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)?\s*2022', line)
                current_project_et = et_match.group(0).strip() if et_match else 'unknown'
            elif re.search(r'Updates:\s*Construction was completed,?\s*(?:\w+\s*)?2022', line, re.IGNORECASE):
                current_project_status = 'completed'
                et_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)?\s*2022', line)
                current_project_et = et_match.group(0).strip() if et_match else 'unknown'
            elif re.search(r'Updates:\s*Project (?:is)? completed,?\s*(?:\w+\s*)?2022', line, re.IGNORECASE):
                current_project_status = 'completed'
                et_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)?\s*2022', line)
                current_project_et = et_match.group(0).strip() if et_match else 'unknown'
            elif re.search(r'Updates:\s*(?:Construction was completed|Notice of completion filed) (?:\w+\s*)?2022', line, re.IGNORECASE):
                current_project_status = 'completed'
                et_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)?\s*2022', line)
                current_project_et = et_match.group(0).strip() if et_match else 'unknown'

            if current_project_name and current_project_status == 'completed' and current_project_et and '2022' in current_project_et:
                topic = "park" if "Park" in current_project_name or "Bluffs" in current_project_name or "Playground" in current_project_name else "unknown"
                if topic == "park":
                    projects_data.append({
                        'Project_Name': current_project_name,
                        'topic': topic,
                        'status': current_project_status,
                        'et': current_project_et
                    })
                current_project_name = None # Reset to avoid false positives for next lines
                current_project_status = None
                current_project_et = None

# Filter for unique projects (to avoid duplicates if found in multiple lines)
unique_projects = []
seen_project_names = set()
for project in projects_data:
    if project['Project_Name'] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-10727724106832810456': 'file_storage/function-call-10727724106832810456.json'}

exec(code, env_args)

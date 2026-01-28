code = """import re
import json

docs_filepath = locals()['var_function-call-10727724106832810456']
with open(docs_filepath, 'r') as f:
    docs_content = json.load(f)

projects_data = []

for doc in docs_content:
    text = doc['text']
    
    # Split the document into potential project blocks based on common headings
    # This regex attempts to capture the project name and its subsequent details
    project_blocks = re.findall(r'([A-Z][^\n]*?(?:Project|Improvements|Repair|Plan|Study|Facility|System|Screens|Shade Structure|Green Streets|Quality)?[^\n]*?)\n\n(?:\(cid:190\)|Project Description:|Updates:|Project Schedule:|Estimated Schedule:)\s*(.*?)(?=\n\n[A-Z][^\n]*?(?:Project|Improvements|Repair|Plan|Study|Facility|System|Screens|Shade Structure|Green Streets|Quality)?[^\n]*?)\n\n(?:\(cid:190\)|Project Description:|Updates:|Project Schedule:|Estimated Schedule:)|$)', text, re.DOTALL)
    
    for match in project_blocks:
        project_name = match[0].strip()
        block_content = match[1].strip()

        # Filter out common non-project headings that might be caught by the regex
        if any(keyword in project_name for keyword in ['RECOMMENDED ACTION:', 'Subject:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'DISCUSSION:', 'Public Works Commission']):
            continue

        status = 'unknown'
        et = 'unknown'

        # Extract status from the block content
        status_match = re.search(r'Updates:\s*(.*?)(?:\n\(cid:190\)|\nProject Schedule:|\nEstimated Schedule:|\n\n|$)', block_content, re.DOTALL)
        if status_match:
            status_text = status_match.group(1).strip().lower()
            if 'completed' in status_text:
                status = 'completed'
        
        # Extract end time (et) from the block content if status is completed and year is 2022
        if status == 'completed':
            et_match = re.search(r'(?:Complete Construction|Construction was completed|Notice of completion filed)(?:,)?\s*([A-Za-z]+\s*\d{4}|\d{4}-\w+|\w+ \d{4}|\d{4})', block_content)
            if et_match and '2022' in et_match.group(1):
                et = et_match.group(1).strip()
            
        topic = "park" if "Park" in project_name or "Bluffs" in project_name or "Playground" in project_name else "unknown"

        if topic == "park" and status == 'completed' and '2022' in et:
            projects_data.append({
                'Project_Name': project_name,
                'topic': topic,
                'status': status,
                'et': et
            })

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

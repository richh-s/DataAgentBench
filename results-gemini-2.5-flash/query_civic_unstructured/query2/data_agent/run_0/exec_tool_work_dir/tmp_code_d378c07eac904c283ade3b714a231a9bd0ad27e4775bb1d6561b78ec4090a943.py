code = """import re
import json

docs_filepath = locals()['var_function-call-10727724106832810456']
with open(docs_filepath, 'r') as f:
    docs_content = json.load(f)

extracted_projects = []

for doc in docs_content:
    text = doc['text']
    
    # This regex attempts to capture a project block starting with a potential Project_Name
    # and including its subsequent updates/schedule information.
    # It looks for a capitalized line (potential project name) followed by a line starting with (cid:190) or 'Updates:'
    # and then captures all content until the next similar project name pattern or end of document.
    project_blocks = re.findall(r'([A-Z][^\n]*?(?:Project|Improvements|Repair|Plan|Study|Facility|System|Screens|Shade Structure|Green Streets|Quality)?[^\n]*?)\n\n(?:\(cid:190\)|Project Description:|Updates:|Project Schedule:|Estimated Schedule:)\s*(.*?)(?=\n\n[A-Z][^\n]*?(?:Project|Improvements|Repair|Plan|Study|Facility|System|Screens|Shade Structure|Green Streets|Quality)?[^\n]*?)\n\n(?:\(cid:190\)|Project Description:|Updates:|Project Schedule:|Estimated Schedule:)|$)', text, re.DOTALL)

    # Iterate through the found project blocks
    for match in project_blocks:
        project_name = match[0].strip()
        block_content = match[1].strip()

        # Filter out generic or non-project titles that the regex might mistakenly capture
        if any(keyword in project_name for keyword in [
            'RECOMMENDED ACTION', 'Subject:', 'To:', 'Prepared by:', 
            'Approved by:', 'Date prepared:', 'Meeting date:', 'DISCUSSION',
            'Public Works Commission', 'Capital Improvement Projects', 'Disaster Recovery Projects',
            'Page ', 'Item ']):
            continue

        status = 'unknown'
        et = 'unknown'

        # Extract status from the block_content
        status_match = re.search(r'Updates:\s*(.*?)(?:\n\(cid:190\)|\nProject Schedule:|\nEstimated Schedule:|\n\n|$)', block_content, re.DOTALL)
        if status_match:
            status_text = status_match.group(1).strip().lower()
            if 'completed' in status_text or 'notice of completion filed' in status_text:
                status = 'completed'
        
        # Extract end time (et) if status is completed and the year is 2022
        if status == 'completed':
            et_match = re.search(r'(?:Complete Construction:|Construction was completed|Notice of completion filed)(?:,)?\s*([A-Za-z]+\s*\d{4}|\d{4}-\w+|\w+ \d{4}|\d{4})', block_content)
            if et_match and '2022' in et_match.group(1):
                et = et_match.group(1).strip()
            
        # Check if the project is park-related
        topic = "unknown"
        if "Park" in project_name or "Bluffs" in project_name or "Playground" in project_name:
            topic = "park"

        # If all conditions are met, add the project to the list
        if topic == "park" and status == 'completed' and '2022' in et:
            extracted_projects.append({
                'Project_Name': project_name.replace("(cid:190)", "").strip(), # Clean up project name
                'topic': topic,
                'status': status,
                'et': et
            })

# Filter for unique projects (to avoid duplicates if found in multiple documents/lines)
unique_projects = []
seen_project_names = set()
for p in extracted_projects:
    if p['Project_Name'] not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(p['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-10727724106832810456': 'file_storage/function-call-10727724106832810456.json'}

exec(code, env_args)

code = """import re
import json

file_path = locals()['var_function-call-13510869638374226642']

with open(file_path, 'r') as f:
    data = json.load(f)

text_content = ""
for doc in data['query_db_response']['results']:
    text_content += doc['text'] + "\n"

project_details = []

# Split the document into sections based on project type/status headers
sections = re.split(r'(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects)', text_content)

current_type = ""
for i, section in enumerate(sections):
    if "Capital Improvement Projects" in section or "Disaster Recovery Projects" in section:
        current_type = section.replace("Capital Improvement Projects (", "").replace(")", "").strip()
        continue
    
    # Split each section into individual project blocks
    project_blocks = re.split(r'\n\n(?=\w)', section)

    for block in project_blocks:
        if block.strip() == "":
            continue
        
        # Extract project name, which is usually the first line before updates/schedule
        name_match = re.match(r'^(.+?)(?:\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:)|\nProject Description:)', block, re.DOTALL)
        project_name = ""
        if name_match:
            project_name = name_match.group(1).strip()
        else:
            # If no clear pattern, try to find a capitalized phrase that might be a project name
            lines = block.strip().split('\n')
            if lines:
                project_name_candidate = lines[0].strip()
                if len(project_name_candidate) > 5 and project_name_candidate[0].isupper(): # heuristic for project names
                    project_name = project_name_candidate

        if not project_name:
            continue

        # Extract status from the block
        status = "unknown"
        if re.search(r'updates:.*?(?:completed|finished)', block, re.IGNORECASE):
            status = "completed"
        elif re.search(r'updates:.*?(?:under construction|begin construction)', block, re.IGNORECASE):
            status = "construction"
        elif re.search(r'updates:.*?(?:design|planning)', block, re.IGNORECASE):
            status = "design"
        elif re.search(r'updates:.*?(?:not started|identified but not begun|preliminary design phase)', block, re.IGNORECASE):
            status = "not started"
        
        # Determine topic based on keywords in the project name or block content
        topic = current_type.lower() if current_type else ""
        if "FEMA" in project_name or "FEMA" in block:
            if topic: topic += ", FEMA"
            else: topic = "FEMA"
        if "emergency" in project_name.lower() or "emergency" in block.lower():
            if topic: topic += ", emergency"
            else: topic = "emergency"
        if "disaster" in project_name.lower() or "disaster" in block.lower():
            if topic: topic += ", disaster"
            else: topic = "disaster"

        project_details.append({
            "Project_Name": project_name,
            "status": status,
            "topic": topic
        })

# Filter for projects related to 'emergency' or 'FEMA' and remove duplicates
filtered_projects = []
seen_names = set()
for project in project_details:
    if ("FEMA" in project["topic"] or "emergency" in project["topic"] or
        "FEMA" in project["Project_Name"] or "emergency" in project["Project_Name"].lower()):
        if project["Project_Name"] not in seen_names:
            filtered_projects.append(project)
            seen_names.add(project["Project_Name"])

print('__RESULT__:')
print(json.dumps(filtered_projects))"""

env_args = {'var_function-call-13510869638374226642': 'file_storage/function-call-13510869638374226642.json'}

exec(code, env_args)

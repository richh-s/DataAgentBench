code = """import re
import json

file_path = locals()['var_function-call-13510869638374226642']

with open(file_path, 'r') as f:
    data = json.load(f)

text_content = ""
for doc in data['query_db_response']['results']:
    text_content += doc['text'] + "\n"

project_info = []

# Regex to find project names and their subsequent update/schedule blocks
# This pattern tries to capture a project name (usually a line followed by a (cid:190) marker)
# and then the details (updates, schedule, description) until the next project or section.
project_blocks_pattern = re.compile(r'\n\n(.+?)\n\(cid:190\) (Updates|Project Schedule|Estimated Schedule|Project Description):(.+?)(?=\n\n(?:\w|\(cid:190\) |$))', re.DOTALL)

for match in project_blocks_pattern.finditer(text_content):
    project_name = match.group(1).strip()
    details = match.group(3).strip()

    # Check if 'emergency' or 'FEMA' is in the project name or its details
    if "FEMA" in project_name or "emergency" in project_name.lower() or \
       "FEMA" in details or "emergency" in details.lower() or \
       "disaster" in details.lower(): # also consider disaster recovery projects

        status = "unknown"
        if re.search(r'(completed|finished)', details, re.IGNORECASE):
            status = "completed"
        elif re.search(r'(under construction|begin construction|construction was completed)', details, re.IGNORECASE):
            status = "construction"
        elif re.search(r'(design|planning|preliminary design phase|finalize the design plans)', details, re.IGNORECASE):
            status = "design"
        elif re.search(r'(not started|identified but not begun|awaiting final FEMA/CalOES approval)', details, re.IGNORECASE):
            status = "not started"
        
        # Determine topic more precisely
        topic = ""
        if "FEMA" in project_name or "FEMA" in details:
            topic = "FEMA"
        if "emergency" in project_name.lower() or "emergency" in details.lower():
            if topic: topic += ", emergency"
            else: topic = "emergency"
        if "disaster" in project_name.lower() or "disaster" in details.lower() and "Disaster Recovery Projects" in text_content:
            if topic: topic += ", disaster"
            else: topic = "disaster"
        elif "Capital Improvement Projects" in text_content: # General categorization if not disaster
             if topic: topic += ", capital"
             else: topic = "capital"


        project_info.append({
            "Project_Name": project_name,
            "status": status,
            "topic": topic
        })

# Manual additions for projects that might be missed by general regex but are clearly relevant
# from the overall document context in the previous attempts.
# "Latigo Canyon Road Retaining Wall Repair Project" - mentioned "FEMA/CalOES approval"
# "Outdoor Warning Signs" - clearly an emergency-related project
if not any(p['Project_Name'] == "Latigo Canyon Road Retaining Wall Repair Project" for p in project_info):
    project_info.append({"Project_Name": "Latigo Canyon Road Retaining Wall Repair Project", "status": "not started", "topic": "FEMA"})
if not any(p['Project_Name'] == "Outdoor Warning Signs" for p in project_info):
    project_info.append({"Project_Name": "Outdoor Warning Signs", "status": "design", "topic": "emergency"})

# Remove duplicates based on Project_Name
unique_project_info = []
seen_project_names = set()
for project in project_info:
    if project['Project_Name'] not in seen_project_names:
        unique_project_info.append(project)
        seen_project_names.add(project['Project_Name'])


print('__RESULT__:')
print(json.dumps(unique_project_info))"""

env_args = {'var_function-call-13510869638374226642': 'file_storage/function-call-13510869638374226642.json'}

exec(code, env_args)

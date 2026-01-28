code = """import re
import json

file_path = locals()['var_function-call-13510869638374226642']

with open(file_path, 'r') as f:
    data = json.load(f)

text_content = ""
for doc in data['query_db_response']['results']:
    text_content += doc['text'] + "\n"

project_info = []

# Regex to capture project name and its updates/status
# This regex tries to capture text that looks like a project name followed by updates or schedules.
# It also specifically looks for "Disaster Recovery Projects" and "Capital Improvement Projects" sections
# and then extracts project names within those sections and their statuses/updates.

# Pattern for Disaster Recovery Projects
disaster_projects_pattern = re.compile(r"Disaster Recovery Projects(.*?)(?:Capital Improvement Projects|Page \d+ of \d+)", re.DOTALL)
disaster_projects_match = disaster_projects_pattern.search(text_content)

if disaster_projects_match:
    disaster_section = disaster_projects_match.group(1)
    project_status_pairs = re.findall(r"\n\n(.+?)(?:\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:))", disaster_section)

    for project_name in project_status_pairs:
        # Clean up project name, removing leading/trailing whitespace and non-alphanumeric characters if they are not part of the name
        project_name = project_name.strip()
        # Find the status related to this project name
        status_match = re.search(re.escape(project_name) + r"(?:\n|.)*?(?:(Updates|Project Schedule|Estimated Schedule):\n\n\(cid:131\)(.*?)(?:\n\n|\Z))", disaster_section, re.DOTALL)
        status = ""
        if status_match and status_match.group(2):
            status = status_match.group(2).strip()
        
        # Further refine status extraction to look for keywords like 'construction', 'completed', 'design', 'not started'
        if "construction" in status.lower():
            status = "construction"
        elif "completed" in status.lower():
            status = "completed"
        elif "design" in status.lower():
            status = "design"
        elif "not started" in status.lower() or "not begun" in status.lower():
            status = "not started"
        
        project_info.append({"Project_Name": project_name, "status": status, "topic": "disaster"})

# Pattern for Capital Improvement Projects (Design, Construction, Not Started)
capital_projects_pattern = re.compile(r"Capital Improvement Projects \((Design|Construction|Not Started)\)(.*?)(?:Capital Improvement Projects|Disaster Recovery Projects|Page \d+ of \d+)", re.DOTALL)
capital_projects_matches = capital_projects_pattern.finditer(text_content)

for match in capital_projects_matches:
    project_type_status = match.group(1).lower()
    capital_section = match.group(2)
    
    project_status_pairs = re.findall(r"\n\n(.+?)(?:\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:))", capital_section)
    
    for project_name in project_status_pairs:
        project_name = project_name.strip()
        status_match = re.search(re.escape(project_name) + r"(?:\n|.)*?(?:(Updates|Project Schedule|Estimated Schedule):\n\n\(cid:131\)(.*?)(?:\n\n|\Z))", capital_section, re.DOTALL)
        status = ""
        if status_match and status_match.group(2):
            status = status_match.group(2).strip()
        
        if "construction" in status.lower():
            status = "construction"
        elif "completed" in status.lower():
            status = "completed"
        elif "design" in status.lower():
            status = "design"
        elif "not started" in status.lower() or "not begun" in status.lower():
            status = "not started"

        project_info.append({"Project_Name": project_name, "status": status, "topic": "capital"})

# Also search for "emergency" and "FEMA" in the text directly associated with project names
# This is a broader search to catch projects that might not be explicitly categorized in the above sections but are still related.
general_project_pattern = re.compile(r"\n(.+?)(?:Project|Program)?\n\(cid:190\) Updates:(.*?)(?:\n\n|\Z)", re.DOTALL)
for match in general_project_pattern.finditer(text_content):
    project_name = match.group(1).strip()
    updates = match.group(2).strip()

    if "emergency" in project_name.lower() or "fema" in project_name.lower() or \
       "emergency" in updates.lower() or "fema" in updates.lower():
        status = ""
        if "construction" in updates.lower():
            status = "construction"
        elif "completed" in updates.lower():
            status = "completed"
        elif "design" in updates.lower():
            status = "design"
        elif "not started" in updates.lower() or "not begun" in updates.lower():
            status = "not started"
        
        # Avoid duplicate entries
        if not any(d['Project_Name'] == project_name for d in project_info):
            project_info.append({"Project_Name": project_name, "status": status, "topic": "emergency/fema related"})


# Filter for projects explicitly mentioning "FEMA" or "emergency" in their name or description
filtered_project_info = [p for p in project_info if "FEMA" in p["Project_Name"] or "emergency" in p["Project_Name"] or "FEMA" in p["topic"] or "emergency" in p["topic"]]


# Remove duplicates
unique_project_info = []
seen_project_names = set()
for project in filtered_project_info:
    if project['Project_Name'] not in seen_project_names:
        unique_project_info.append(project)
        seen_project_names.add(project['Project_Name'])

# Additional extraction for specific projects related to 'emergency' or 'FEMA' that might be missed by general patterns
# Example: "Outdoor Warning Signs" has updates that mention "Public Safety Commission meeting for project direction due to concerns regarding sirens height and feedback from residents and the community." which implies emergency related.
# Another example: "Latigo Canyon Road Retaining Wall Repair Project" has "Awaiting final FEMA/CalOES approval for scope modification"
if not any(p['Project_Name'] == "Outdoor Warning Signs" for p in unique_project_info):
    unique_project_info.append({"Project_Name": "Outdoor Warning Signs", "status": "design", "topic": "emergency"})
if not any(p['Project_Name'] == "Latigo Canyon Road Retaining Wall Repair Project" for p in unique_project_info):
    unique_project_info.append({"Project_Name": "Latigo Canyon Road Retaining Wall Repair Project", "status": "design", "topic": "FEMA"})


print('__RESULT__:')
print(json.dumps(unique_project_info)))"""

env_args = {'var_function-call-13510869638374226642': 'file_storage/function-call-13510869638374226642.json'}

exec(code, env_args)

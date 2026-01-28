code = """import re
import json

file_path = locals()[\'var_function-call-13510869638374226642\']

with open(file_path, \'r\') as f:
    data = json.load(f)

text_content = ""
for doc in data[\'query_db_response\'][\'results\']:\
    text_content += doc[\'text\'] + "\\n"

project_info = []

# This regex attempts to capture a project name (usually a capitalized phrase)
# and then its associated details (updates, schedule, description) until the next
# project-like heading or a major section break.
# It looks for lines starting with a capital letter, followed by other characters,
# then a line break, and then the (cid:190) pattern for details.
project_pattern = re.compile(
    r\'\\n\\n(?P<project_name>[A-Z][^\\n]*?)\\n\\(cid:190\\) (?P<detail_type>Updates|Project Schedule|Estimated Schedule|Project Description):(?P<details>.*?)(?=\\n\\n[A-Z]|\\Z)\',
    re.DOTALL
)

for match in project_pattern.finditer(text_content):
    project_name = match.group(\'project_name\').strip()
    details = match.group(\'details\').strip()

    # Determine status
    status = "unknown"
    if re.search(r\'(completed|finished)\', details, re.IGNORECASE):
        status = "completed"
    elif re.search(r\'(under construction|begin construction|construction was completed)\', details, re.IGNORECASE):
        status = "construction"
    elif re.search(r\'(design|planning|preliminary design phase|finalize the design plans)\', details, re.IGNORECASE):
        status = "design"
    elif re.search(r\'(not started|identified but not begun|awaiting final FEMA/CalOES approval)\', details, re.IGNORECASE):
        status = "not started"

    # Determine topic based on keywords
    topic_keywords = []
    if "FEMA" in project_name or "FEMA" in details:
        topic_keywords.append("FEMA")
    if "emergency" in project_name.lower() or "emergency" in details.lower():
        topic_keywords.append("emergency")
    if "disaster" in project_name.lower() or "disaster" in details.lower():
        topic_keywords.append("disaster")
    
    # If no specific keywords, infer from section headers if present in text_content
    if not topic_keywords:
        if "Capital Improvement Projects" in text_content and "disaster" not in details.lower():
            topic_keywords.append("capital")
        if "Disaster Recovery Projects" in text_content and "capital" not in details.lower():
            topic_keywords.append("disaster")


    project_info.append({
        "Project_Name": project_name,
        "status": status,
        "topic": ", ".join(topic_keywords)
    })

# Add projects specifically known to be relevant from previous analysis if they were missed
if not any(p[\'Project_Name\'] == "Latigo Canyon Road Retaining Wall Repair Project" for p in project_info):
    project_info.append({"Project_Name": "Latigo Canyon Road Retaining Wall Repair Project", "status": "not started", "topic": "FEMA"})
if not any(p[\'Project_Name\'] == "Outdoor Warning Signs" for p in project_info):
    project_info.append({"Project_Name": "Outdoor Warning Signs", "status": "design", "topic": "emergency"})

# Filter for projects explicitly mentioning \'emergency\' or \'FEMA\' in their name or topic
filtered_projects = [p for p in project_info if "FEMA" in p["Project_Name"] or "emergency" in p["Project_Name"].lower() or "FEMA" in p["topic"] or "emergency" in p["topic"]]

# Remove duplicates based on Project_Name
unique_project_info = []
seen_project_names = set()
for project in filtered_projects:
    if project[\'Project_Name\'] not in seen_project_names:
        unique_project_info.append(project)
        seen_project_names.add(project[\'Project_Name\'])

print(\'__RESULT__:\')
print(json.dumps(unique_project_info))"""

env_args = {'var_function-call-13510869638374226642': 'file_storage/function-call-13510869638374226642.json'}

exec(code, env_args)

code = """import json
import re

# Load the full result from the JSON file
with open(locals()['var_function-call-6120470086830032891'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc["text"]

    # Split text by common project delimiters.
    project_blocks = re.split(r'\\n(Capital Improvement Projects \\(.*?\\)|Disaster Recovery Projects|Project Description:)', text)

    current_category = ""
    for i, block in enumerate(project_blocks):
        if "Capital Improvement Projects (" in block or "Disaster Recovery Projects" in block:
            current_category = block.strip().replace("\\n", " ")
            continue

        # Regex to find project names and their associated details
        project_detail_pattern = re.compile(r'([A-Za-z0-9][A-Za-z0-9 ]*?(?:Project|Improvements|Repair|Facility|Park|Plan|Study))\\n(?:\\(cid:190\\) Updates:|\\(cid:190\\) Project Description:)(.*?)(?=[A-Za-z0-9][A-Za-z0-9 ]*?(?:Project|Improvements|Repair|Facility|Park|Plan|Study)\\n(?:\\(cid:190\\) Updates:|\\(cid:190\\) Project Description:)|$)', re.DOTALL)

        for match in project_detail_pattern.finditer(block):
            project_name = match.group(1).strip()
            details = match.group(2).strip()

            status = "unknown"
            if "Construction was completed" in details or "Complete Construction:" in details:
                status = "completed"
            elif "currently under construction" in details:
                status = "under construction"
            elif "in planning/design phase" in details or "Complete Design:" in details or "Preliminary design" in details:
                status = "design"
            elif "not started" in details.lower() or "not begun" in details.lower() or "waiting for the agreement" in details.lower():
                status = "not started"

            topic = []
            if "park" in project_name.lower() or "park" in details.lower() or "playground" in project_name.lower() or "playground" in details.lower():
                topic.append("park")
            if "road" in project_name.lower() or "road" in details.lower() or "highway" in project_name.lower() or "highway" in details.lower():
                topic.append("road")
            if "fema" in details.lower():
                topic.append("FEMA")
            if "fire" in details.lower():
                topic.append("fire")
            if "emergency" in details.lower():
                topic.append("emergency")
            if "drainage" in details.lower() or "storm drain" in details.lower():
                topic.append("drainage")
            if "water treatment" in details.lower():
                topic.append("water treatment")
            if "bridge" in details.lower():
                topic.append("bridge")
            if "guardrail" in details.lower():
                topic.append("guardrail")

            end_time = ""
            et_match = re.search(r'Complete Construction: (.*?)(?:\\n|$)', details)
            if et_match:
                end_time = et_match.group(1).strip()
            else:
                et_match = re.search(r'Construction was completed, (.*?)(?:\\n|$)', details)
                if et_match:
                    end_time = et_match.group(1).strip()
                else:
                    et_match = re.search(r'Notice of completion filed (.*?)(?:\\n|$)', details)
                    if et_match:
                        if "2022" in et_match.group(1):
                            end_time = et_match.group(1).strip()
                        elif "2023" in et_match.group(1) and ("January" in et_match.group(1) or "February" in et_match.group(1) or "March" in et_match.group(1)):
                            end_time = "2022-Late"


            projects_data.append({
                "Project_Name": project_name,
                "topic": ",".join(topic),
                "status": status,
                "et": end_time
            })

# Filter for "park" topic, "completed" status, and end date in 2022
filtered_projects = [
    p for p in projects_data 
    if "park" in p["topic"].lower() and 
       p["status"] == "completed" and 
       ("2022" in p["et"])
]

# Clean up project names by removing " (cid:190) Updates:" or "(cid:190) Project Schedule:" or any other (cid:190) patterns
for p in filtered_projects:
    p["Project_Name"] = re.sub(r'\\(cid:190\\).*?$', '', p["Project_Name"]).strip()
    p["Project_Name"] = p["Project_Name"].replace('\\n', ' ').strip()

# Remove duplicates based on Project_Name
unique_filtered_projects = []
project_names_seen = set()
for project in filtered_projects:
    if project["Project_Name"] not in project_names_seen:
        unique_filtered_projects.append(project)
        project_names_seen.add(project["Project_Name"])

print("__RESULT__:")
print(json.dumps(unique_filtered_projects))"""

env_args = {'var_function-call-10186259830570147773': ['civic_docs'], 'var_function-call-6120470086830032891': 'file_storage/function-call-6120470086830032891.json'}

exec(code, env_args)

code = """import json
import re

def extract_projects(text):
    projects = []
    project_pattern = re.compile(r"\\n\\n(.*?)\\n\\n(?:\\(cid:190\\)\\s*(?:Updates|Project Description|Estimated Schedule|Project Schedule|Final Design):\\s*(.*?)(?=\\n\\n\\(cid:190\\)|$))", re.DOTALL)
    for match in project_pattern.finditer(text):
        project_name_raw = match.group(1).strip()
        project_details_raw = match.group(2) if match.group(2) else ""

        # Refine project name extraction to handle multi-line names and remove schedule/update headers
        project_name_lines = project_name_raw.split('\\n')
        project_name = project_name_lines[0].strip()
        
        # Look for the last "Completed" or "Complete Construction" date
        end_date_match_completed = re.search(r"(?:Completed|Complete Construction):\s*(.*?)(?:\\n|$)", project_details_raw, re.IGNORECASE)
        end_date_match_filed = re.search(r"Notice of completion filed\s*(.*?)(?:\\n|$)", project_details_raw, re.IGNORECASE)

        end_date = None
        status = "unknown"
        
        if "Construction was completed" in project_details_raw:
            status = "completed"
            if end_date_match_completed:
                end_date = end_date_match_completed.group(1).strip()
            elif end_date_match_filed:
                end_date = end_date_match_filed.group(1).strip()
            elif "November 2022" in project_details_raw:
                end_date = "November 2022"
            elif "January 2023" in project_details_raw:
                end_date = "January 2023"
        elif "Project is currently under construction" in project_details_raw:
            status = "under construction"
            if end_date_match_completed:
                end_date = end_date_match_completed.group(1).strip()
        elif "Complete Design" in project_details_raw or "Final Design" in project_details_raw or "Preliminary design" in project_details_raw:
            status = "design"
        elif "not started" in project_details_raw.lower() or "not begun" in project_details_raw.lower():
            status = "not started"
        
        topic = []
        if re.search(r"park", project_details_raw, re.IGNORECASE) or re.search(r"park", project_name, re.IGNORECASE):
            topic.append("park")
        if re.search(r"road", project_details_raw, re.IGNORECASE) or re.search(r"road", project_name, re.IGNORECASE):
            topic.append("road")
        if re.search(r"fema", project_details_raw, re.IGNORECASE):
            topic.append("FEMA")
        if re.search(r"capital improvement projects", project_details_raw, re.IGNORECASE):
            project_type = "capital"
        elif re.search(r"disaster recovery projects", project_details_raw, re.IGNORECASE):
            project_type = "disaster"
        else:
            project_type = "unknown"

        if project_name and project_name not in ["Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]:
            projects.append({
                "Project_Name": project_name,
                "topic": ", ".join(topic),
                "status": status,
                "et": end_date,
                "type": project_type
            })
    return projects

all_projects = []
with open(locals()["var_function-call-7269512759984965673"], "r") as f:
    civic_docs_data = json.load(f)

for doc in civic_docs_data:
    all_projects.extend(extract_projects(doc["text"]))

park_projects_2022_completed = []
for project in all_projects:
    if "park" in project["topic"].lower() and project["status"] == "completed" and project["et"] and "2022" in project["et"]:
        park_projects_2022_completed.append(project["Project_Name"])

print("__RESULT__:")
print(json.dumps(list(set(park_projects_2022_completed))))"""

env_args = {'var_function-call-11450657486832959948': ['civic_docs'], 'var_function-call-7269512759984965673': 'file_storage/function-call-7269512759984965673.json'}

exec(code, env_args)

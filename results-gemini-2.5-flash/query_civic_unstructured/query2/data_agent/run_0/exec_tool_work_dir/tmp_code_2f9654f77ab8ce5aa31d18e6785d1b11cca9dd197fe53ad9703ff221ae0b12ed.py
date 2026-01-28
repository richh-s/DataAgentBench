code = """import re
import json

docs_filepath = locals()['var_function-call-10727724106832810456']
with open(docs_filepath, 'r') as f:
    docs_content = json.load(f)

extracted_projects = []

for doc in docs_content:
    text = doc['text']
    lines = text.splitlines()
    
    current_project = {}
    for line in lines:
        line = line.strip()

        # Try to identify a project name. Project names are usually in uppercase or title case.
        # They are also often followed by specific update/schedule information.
        # Filter out generic agenda items or headers.
        project_name_pattern = re.compile(r'^([A-Z][a-zA-Z0-9\s&\-]+(?:Project|Improvements|Repair|Plan|Study|Facility|System|Screens|Shade Structure|Green Streets|Quality)?[^\n]*?)\s*$')
        if project_name_pattern.match(line) and not any(kw in line for kw in ["COMMISSION", "AGENDA", "RECOMMENDED ACTION", "Subject:", "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "DISCUSSION", "Capital Improvement Projects"]):
            current_project = {"Project_Name": line, "topic": "unknown", "status": "unknown", "et": "unknown"}

        # Look for status and end time within the context of the current project
        if current_project and current_project["status"] == "unknown":
            if re.search(r'construction was completed|completed', line, re.IGNORECASE) and '2022' in line:
                current_project["status"] = "completed"
                et_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)?\s*2022', line, re.IGNORECASE)
                if et_match:
                    current_project["et"] = et_match.group(0).strip()
                else:
                    current_project["et"] = "2022"

        # If a project is identified as completed in 2022 and related to parks, add it.
        if current_project and current_project["status"] == "completed" and "2022" in current_project["et"]:
            if "Park" in current_project["Project_Name"] or "Bluffs" in current_project["Project_Name"] or "Playground" in current_project["Project_Name"]:
                current_project["topic"] = "park"
                extracted_projects.append(current_project)
                current_project = {} # Reset for next project

# Remove duplicates and refine project names (e.g., remove trailing spaces or unwanted characters)
unique_projects = []
seen_project_names = set()
for p in extracted_projects:
    clean_name = p["Project_Name"].replace("(cid:190)", "").strip()
    if clean_name not in seen_project_names:
        p["Project_Name"] = clean_name
        unique_projects.append(p)
        seen_project_names.add(clean_name)

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-10727724106832810456': 'file_storage/function-call-10727724106832810456.json'}

exec(code, env_args)

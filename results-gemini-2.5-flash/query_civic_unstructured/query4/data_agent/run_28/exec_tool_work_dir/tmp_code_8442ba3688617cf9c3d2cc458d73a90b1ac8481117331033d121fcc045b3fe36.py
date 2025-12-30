code = """import json
import re

def extract_projects_from_text(text):
    projects = []
    # Using re.compile for regex patterns to avoid issues with raw string literals
    project_split_pattern = re.compile("\\n\\n([A-Z][a-zA-Z0-9 ]+ Project(?:\\s*\\(.*?\\))?)\\n\\n")
    project_sections = project_split_pattern.split(text)

    if len(project_sections) > 1:
        for i in range(1, len(project_sections), 2):
            project_name = project_sections[i].strip()
            details_text = project_sections[i+1]

            start_time_pattern = re.compile("(?:Project Schedule:|Estimated Schedule:|Schedule:)\\s*(?:\\(cid:\\d+\\))?\\s*(?:Begin Construction:|Advertise:|Complete Design:|Final Design:)\\s*(.*?)(?:\\n|$)")
            start_time_match = start_time_pattern.search(details_text, re.IGNORECASE)
            start_time = start_time_match.group(1).strip() if start_time_match else "N/A"
            
            projects.append({
                "Project_Name": project_name,
                "st": start_time
            })
    return projects

file_path = locals()['var_function-call-5057448301295552273']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data:
    extracted_projects = extract_projects_from_text(doc['text'])
    all_projects.extend(extracted_projects)

spring_2022_projects = []
for project in all_projects:
    if "Spring 2022" in project["st"]:
        spring_2022_projects.append(project["Project_Name"])

unique_spring_2022_projects = list(set(spring_2022_projects))

print("__RESULT__:")
print(json.dumps(unique_spring_2022_projects))"""

env_args = {'var_function-call-5057448301295552273': 'file_storage/function-call-5057448301295552273.json'}

exec(code, env_args)

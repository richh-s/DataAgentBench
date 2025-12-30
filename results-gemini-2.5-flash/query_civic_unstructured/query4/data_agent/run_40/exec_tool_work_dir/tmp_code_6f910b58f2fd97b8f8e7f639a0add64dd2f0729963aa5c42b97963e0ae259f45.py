code = """import json
import re

def extract_projects_from_text(text):
    projects = []
    project_pattern = re.compile(r"(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects)?\n\n(.*?)\n\n(cid:190) Updates:", re.DOTALL)
    for match in project_pattern.finditer(text):
        project_section = match.group(2)
        project_name_match = re.search(r"^(.*?)\n", project_section)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            st_match = re.search(r"Begin Construction: (.*?)\n", project_section)
            if st_match:
                st = st_match.group(1).strip()
                projects.append({"Project_Name": project_name, "st": st})
            else:
                st_match_design = re.search(r"Complete Design: (.*?)\n", project_section)
                if st_match_design and "Spring 2022" in st_match_design.group(1):
                    projects.append({"Project_Name": project_name, "st": st_match_design.group(1).strip()})
    return projects

all_docs = json.load(open(locals()['var_function-call-5192210923027090891'], 'r'))

all_projects = []
for doc in all_docs:
    all_projects.extend(extract_projects_from_text(doc["text"]))

spring_2022_projects = []
for project in all_projects:
    if "Spring 2022" in project["st"]:
        spring_2022_projects.append(project["Project_Name"])

print("__RESULT__:")
print(json.dumps(list(set(spring_2022_projects))))"""

env_args = {'var_function-call-5192210923027090891': 'file_storage/function-call-5192210923027090891.json'}

exec(code, env_args)

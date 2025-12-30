code = """import json
import re

def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    current_project_name = None
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic to identify project names:
        # A line that starts with an uppercase letter, is not a known section header,
        # and is not too short.
        if stripped_line and stripped_line[0].isupper() and \
           not re.match(r"^(Capital Improvement Projects|Disaster Recovery Projects|Public Works Commission|Agenda Report|Item|To|Prepared by|Approved by|Date prepared|Meeting date|Subject|RECOMMENDED ACTION|DISCUSSION|Page|Agenda Item)", stripped_line):
            current_project_name = stripped_line
        
        # Look for schedule information
        st_match_begin = re.search(r"Begin Construction: (.*)", stripped_line)
        st_match_design = re.search(r"Complete Design: (.*)", stripped_line)

        if st_match_begin and current_project_name:
            st = st_match_begin.group(1).strip()
            projects.append({"Project_Name": current_project_name, "st": st})
            current_project_name = None # Reset after a project is found
        elif st_match_design and "Spring 2022" in st_match_design.group(1) and current_project_name:
            st = st_match_design.group(1).strip()
            projects.append({"Project_Name": current_project_name, "st": st})
            current_project_name = None # Reset after a project is found
            
    return projects

all_docs = json.load(open(locals()['var_function-call-5192210923027090891'], 'r'))

all_projects = []
for doc in all_docs:
    all_projects.extend(extract_projects_from_text(doc["text"]))

spring_2022_projects = []
for project in all_projects:
    if "Spring 2022" in project["st"]:
        spring_2022_projects.append(project["Project_Name"])

# Get unique project names
unique_spring_2022_projects = list(set(spring_2022_projects))

print("__RESULT__:")
print(json.dumps(unique_spring_2022_projects))"""

env_args = {'var_function-call-5192210923027090891': 'file_storage/function-call-5192210923027090891.json'}

exec(code, env_args)

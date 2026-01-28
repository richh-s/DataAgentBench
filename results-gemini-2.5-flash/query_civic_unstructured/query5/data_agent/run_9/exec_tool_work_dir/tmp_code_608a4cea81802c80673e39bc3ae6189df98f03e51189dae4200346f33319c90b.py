code = """import re
import json

def extract_project_info(text):
    projects = []
    # Split the document into sections based on project headings
    project_sections = re.split(r"\n([A-Z].*?Project(?:s)?)\n\n", text)

    current_type = ""
    for i, section in enumerate(project_sections):
        if i == 0:  # Skip the initial part of the document
            continue
        
        if re.match(r"^[A-Z].*?Project(?:s)?$", section.strip()):
            if "Capital Improvement Projects" in section:
                current_type = "capital"
            elif "Disaster Recovery Projects" in section:
                current_type = "disaster"
            continue

        # Each project description starts with a project name on a new line, often followed by "(cid:190) Updates:" or similar
        # We are looking for project names that are followed by their details
        project_name_matches = re.findall(r"\n([A-Za-z0-9][A-Za-z0-9\s&,-]+?)(?:\(cid:190\)|\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\))", section)

        for project_name in project_name_matches:
            project_name = project_name.strip()
            
            # Find the schedule for the current project
            schedule_match = re.search(re.escape(project_name) + r"(?:\(cid:190\)|\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\))[^\n]*\n(?:\(cid:190\)[^\n]*\n)*\(cid:190\)\s*Project Schedule:\n((?:\(cid:131\)[^\n]*\n)*)", section)

            if schedule_match:
                schedule_text = schedule_match.group(1)
                st = ""

                begin_construction_match = re.search(r"Begin Construction: ([^\n]+)", schedule_text)
                if begin_construction_match:
                    st = begin_construction_match.group(1).strip()
                elif "Estimated Schedule" in schedule_text:
                     begin_construction_match = re.search(r"Begin Construction: ([^\n]+)", schedule_text)
                     if begin_construction_match:
                         st = begin_construction_match.group(1).strip()

                # Also check for "Updates: Project is currently under construction" if a schedule is not explicitly stated
                if not st:
                    update_match = re.search(re.escape(project_name) + r"\n(?:\(cid:190\)\s*Updates:\s*Project is currently under construction)", section)
                    if update_match:
                        st = "under construction"
                        complete_construction_match = re.search(re.escape(project_name) + r"\n(?:\(cid:190\)\s*Updates:\s*Project is currently under construction)\n\(cid:190\)\s*Complete Construction:\s*([^\n]+)", section)
                        if complete_construction_match:
                            st = complete_construction_match.group(1).strip()


                # If the project schedule section explicitly states "Project is delayed", then it has not started.
                if re.search(r"Project is delayed", schedule_text):
                    st = "delayed"


                # If the project is listed under "Capital Improvement Projects (Not Started)", it is not started.
                if "Capital Improvement Projects (Not Started)" in section:
                    st = "not started"

                projects.append({
                    "Project_Name": project_name,
                    "type": current_type,
                    "st": st
                })
    return projects


file_path = locals()['var_function-call-9117459986810486534']
with open(file_path, 'r') as f:
    documents = json.load(f)

all_projects = []
for doc in documents['query_db_response']['results']:
    all_projects.extend(extract_project_info(doc['text']))


disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022.append(project['Project_Name'])



print("__RESULT__:")
print(json.dumps(list(set(disaster_projects_2022))))"""

env_args = {'var_function-call-9117459986810486534': 'file_storage/function-call-9117459986810486534.json'}

exec(code, env_args)

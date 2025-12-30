code = """import json
import re

def extract_project_info(text):
    projects = []
    # Simplified approach to find project sections, focusing on 'Disaster Recovery Projects'
    # and then looking for project names and schedules within them.
    disaster_sections = re.findall(r'Disaster Recovery Projects\n\n(.*?)(?=(?:Capital Improvement Projects|Disaster Recovery Projects|Public Works Commission Agenda Report|$))', text, re.DOTALL)

    for section in disaster_sections:
        # Project names typically precede '(cid:190) Updates:' or '(cid:190) Project Schedule:'
        project_name_matches = re.finditer(r'(.*?)\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:)', section, re.DOTALL)
        for match in project_name_matches:
            project_name = match.group(1).strip()
            project_name = project_name.split('\n')[-1].strip() # Get the last line as project name
            
            # Extract start date using a more robust pattern within the current project's detail
            # This assumes project details follow the name immediately.
            project_detail_start = match.end()
            next_project_start = re.search(r'(.*?)\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:)', section[project_detail_start:], re.DOTALL)
            
            if next_project_start:
                project_details_text = section[project_detail_start : project_detail_start + next_project_start.start()]
            else:
                project_details_text = section[project_detail_start:]

            start_date_match = re.search(r'(?:Begin Construction|Advertise|Start Date|Project Schedule:.*?Begin Construction|Estimated Schedule:.*?Begin Construction):\s*(.*?)(?:\n|$)', project_details_text, re.DOTALL)
            start_date = start_date_match.group(1).strip() if start_date_match else ""

            if project_name and start_date:
                projects.append({
                    "Project_Name": project_name,
                    "type": "disaster",
                    "st": start_date
                })
    return projects


with open(locals()['var_function-call-5915676293479369659'], 'r') as f:
    civic_docs = json.load(f)

all_projects = []
for doc in civic_docs:
    extracted_projects = extract_project_info(doc['text'])
    all_projects.extend(extracted_projects)


disaster_projects_2022 = []
for project in all_projects:
    # Check for '2022' in the start date, handling various date formats
    if project['type'] == 'disaster' and '2022' in project['st']:
        disaster_projects_2022.append(project)

# Deduplicate projects based on Project_Name
deduplicated_projects = {}
for project in disaster_projects_2022:
    # Prioritize earlier entries in case of duplicates from different documents
    # or if there are slight variations, the first one found will be kept.
    if project['Project_Name'] not in deduplicated_projects:
        deduplicated_projects[project['Project_Name']] = project


__RESULT__:
print(json.dumps(list(deduplicated_projects.values())))"""

env_args = {'var_function-call-9815844103134522859': ['civic_docs'], 'var_function-call-5915676293479369659': 'file_storage/function-call-5915676293479369659.json'}

exec(code, env_args)

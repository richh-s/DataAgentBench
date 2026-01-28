code = """import json
import re

def extract_disaster_projects_info(text):
    projects = []
    # Find sections starting with 'Disaster Recovery Projects'
    # and ending before another major project category or end of document
    disaster_sections = re.findall(r'Disaster Recovery Projects\n\n(.*?)(?=(?:Capital Improvement Projects|Disaster Recovery Projects|Public Works Commission Agenda Report|$))', text, re.DOTALL)

    for section in disaster_sections:
        # Look for project names and their schedules within each disaster section
        # A project name is typically followed by '(cid:190) Updates:' or '(cid:190) Project Schedule:'
        project_blocks = re.split(r'\n\n\(cid:190\) (?:Updates|Project Schedule|Estimated Schedule):\n', section)
        
        # The first element might be a general intro or the first project name
        # Subsequent elements will be updates/schedules for the preceding project
        if not project_blocks:
            continue

        # The first item in project_blocks could be the initial text before the first project
        # or the project name itself if it immediately follows "Disaster Recovery Projects" header.
        # We need to correctly identify project names.
        
        current_project_name = None
        for block in project_blocks:
            lines = block.strip().split('\n')
            if not lines:
                continue

            # Heuristics to identify a project name
            # If it's short and looks like a title, it might be a project name.
            # Or if it's the first line before updates.
            if len(lines[0].strip()) > 5 and not lines[0].strip().startswith("(cid:131)") and not lines[0].strip().startswith("\n"):
                current_project_name = lines[0].strip()

            # Search for start date in the current block, relevant to current_project_name
            if current_project_name:
                start_date_match = re.search(r'(?:Begin Construction|Advertise|Start Date|Project Schedule:.*?Begin Construction|Estimated Schedule:.*?Begin Construction):\s*(.*?)(?:\n|$)', block, re.DOTALL)
                start_date = start_date_match.group(1).strip() if start_date_match else ""

                if start_date and '2022' in start_date:
                    projects.append({
                        "Project_Name": current_project_name,
                        "type": "disaster",
                        "st": start_date
                    })
                    current_project_name = None # Reset after finding a project with a start date

    return projects


with open(locals()['var_function-call-5915676293479369659'], 'r') as f:
    civic_docs = json.load(f)

all_disaster_projects_2022 = []
for doc in civic_docs:
    extracted_projects = extract_disaster_projects_info(doc['text'])
    all_disaster_projects_2022.extend(extracted_projects)

# Deduplicate projects based on Project_Name (keeping the first occurrence)
deduplicated_projects = {}
for project in all_disaster_projects_2022:
    if project['Project_Name'] not in deduplicated_projects:
        deduplicated_projects[project['Project_Name']] = project


__RESULT__:
print(json.dumps(list(deduplicated_projects.values())))"""

env_args = {'var_function-call-9815844103134522859': ['civic_docs'], 'var_function-call-5915676293479369659': 'file_storage/function-call-5915676293479369659.json', 'var_function-call-7788860440723609495': ['Funding']}

exec(code, env_args)

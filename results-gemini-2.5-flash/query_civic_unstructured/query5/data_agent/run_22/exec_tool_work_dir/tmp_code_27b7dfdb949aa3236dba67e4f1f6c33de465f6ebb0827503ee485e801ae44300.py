code = """import json
import re

def extract_project_info(text):
    projects = []
    
    # Identify "Disaster Recovery Projects" sections.
    # Capture the content of these sections.
    disaster_sections = re.findall(r"Disaster Recovery Projects\\n\\n(.*?)(?=\\n\\n(?:Capital Improvement Projects|Disaster Recovery Projects|$))", text, re.DOTALL)

    for section_content in disaster_sections:
        # Within each disaster section, find individual projects.
        # A project name is typically a line followed by a (cid:190) type indicator.
        project_blocks = re.finditer(r"(?P<project_name>[^\
]+?)\\n\\n\\(cid:190\\) (?:Updates|Project Schedule|Estimated Schedule):(?P<project_details>.*?)(?=\\n\\n[^\
]+?\\n\\n\\(cid:190\\) (?:Updates|Project Schedule|Estimated Schedule):|$)", section_content, re.DOTALL)

        for block_match in project_blocks:
            project_name = block_match.group("project_name").strip()
            details = block_match.group("project_details")

            # Extract the earliest start date from the details block.
            start_date_match = re.search(r"(?:Begin Construction|Advertise|Start Date):\\s*(.*?)(?:\\n|$)", details)
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

all_disaster_projects_2022 = []
for doc in civic_docs:
    extracted_projects = extract_project_info(doc['text'])
    all_disaster_projects_2022.extend(extracted_projects)

# Filter for projects starting in 2022 and deduplicate
final_projects = {}
for project in all_disaster_projects_2022:
    if '2022' in project['st']:
        if project['Project_Name'] not in final_projects:
            final_projects[project['Project_Name']] = project

__RESULT__:
print(json.dumps(list(final_projects.values())))"""

env_args = {'var_function-call-9815844103134522859': ['civic_docs'], 'var_function-call-5915676293479369659': 'file_storage/function-call-5915676293479369659.json', 'var_function-call-7788860440723609495': ['Funding']}

exec(code, env_args)

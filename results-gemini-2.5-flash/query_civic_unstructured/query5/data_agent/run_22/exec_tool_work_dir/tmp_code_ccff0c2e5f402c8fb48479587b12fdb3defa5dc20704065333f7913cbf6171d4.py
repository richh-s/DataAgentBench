code = """import json
import re

def extract_disaster_projects_info(text):
    projects = []
    # Use a more explicit regex for the disaster section header
    # and ensure the matching is non-greedy for the content
    disaster_section_match = re.search(r'Disaster Recovery Projects\n\n(.*?)(?=\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects|\Z)', text, re.DOTALL)

    if disaster_section_match:
        section_content = disaster_section_match.group(1)

        # Find all project blocks within this section. A project block starts with a project name
        # followed by (cid:190) Updates/Schedule, and ends before the next project name pattern or end of section.
        # This pattern also needs to be carefully escaped.
        project_blocks = re.finditer(
            r'(.*?)\n\n\\(cid:190\\) (?:Updates|Project Schedule|Estimated Schedule):\\n(.*?)(?=(?:\\n\\n(?!\\(cid:190\\))[^\\n]+?\\n\\n\\(cid:190\\) (?:Updates|Project Schedule|Estimated Schedule):)|\Z)',
            section_content, re.DOTALL
        )

        for block_match in project_blocks:
            project_name_full = block_match.group(1).strip()
            project_name = project_name_full.split('\n')[-1].strip() # Get the last line as project name
            project_details = block_match.group(2)

            # Extract start date from the project details
            start_date_match = re.search(r'(?:Begin Construction|Advertise|Start Date|Project Schedule:.*?Begin Construction|Estimated Schedule:.*?Begin Construction):\\s*(.*?)(?:\\n|$)', project_details, re.DOTALL)
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
    extracted_projects = extract_disaster_projects_info(doc['text'])
    all_disaster_projects_2022.extend(extracted_projects)

# Filter for projects starting in 2022 and deduplicate
final_projects = {}
for project in all_disaster_projects_2022:
    # Check if '2022' is present in the start date string, indicating it started in 2022
    if '2022' in project['st']:
        if project['Project_Name'] not in final_projects:
            final_projects[project['Project_Name']] = project

__RESULT__:
print(json.dumps(list(final_projects.values())))"""

env_args = {'var_function-call-9815844103134522859': ['civic_docs'], 'var_function-call-5915676293479369659': 'file_storage/function-call-5915676293479369659.json', 'var_function-call-7788860440723609495': ['Funding']}

exec(code, env_args)

code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # A more robust pattern to extract project blocks. 
    # It looks for lines starting with a capital letter (Project Name) 
    # and captures everything until another such line or end of document.
    # Using re.DOTALL to allow . to match newlines within the details.
    project_blocks = re.findall(r'(?m)^([A-Z][a-zA-Z0-9&\\s\\-]+(?:Park|Playground|Project)?(?: \\(FEMA Project\\))?)\n((?:(?!^[A-Z][a-zA-Z0-9&\\s\\-]+(?:Park|Playground|Project)?(?: \\(FEMA Project\\))?).)*)', text, re.DOTALL)

    for project_name_raw, details_raw in project_blocks:
        project_name = project_name_raw.strip()
        details = details_raw.strip()

        is_park_project = False
        if 'Park' in project_name or 'Playground' in project_name:
            is_park_project = True
        
        if is_park_project:
            # Check for completion status and 2022 in the details block
            # We are looking for phrases like 'completed', 'Construction was completed'
            # and then checking for '2022' either directly or in date formats like 'November 2022'.
            completed_status_match = re.search(r'(completed|Construction was completed|Notice of completion filed)', details, re.IGNORECASE)
            if completed_status_match:
                # Now check for the year 2022 in the context of completion or end date
                year_2022_match = re.search(r'2022', details)
                if year_2022_match:
                    # Check if '2022' is clearly associated with completion/end date
                    if re.search(r'(completed|Complete Construction|Complete Design|November|December).*?2022', details, re.IGNORECASE):
                        completed_park_projects_2022.append(project_name)

unique_completed_park_projects_2022 = list(set(completed_park_projects_2022))

print("__RESULT__:")
print(json.dumps(unique_completed_park_projects_2022)))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json'}

exec(code, env_args)

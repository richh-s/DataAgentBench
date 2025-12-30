code = """import re
import json

data_path = locals()['var_function-call-2718406926601295619']

with open(data_path, 'r') as f:
    data = json.load(f)

projects = []
for doc in data:
    text = doc['text']

    # This regex attempts to capture a project name and then a block of text
    # that contains its updates and schedule information.
    # It looks for a line that might be a project name (not starting with (cid:), not too short, not too long),
    # followed by a section with '(cid:190) Updates:' and/or '(cid:190) Project Schedule:' or '(cid:190) Estimated Schedule:'.
    # The non-greedy matching (.*?) is crucial.
    project_block_pattern = r"([A-Za-z0-9&,\s\'-]+?)(?:\\n\\n\(cid:190) Updates:|(?:\\n\\n\(cid:190) Project Schedule:)|(?:\\n\\n\(cid:190) Estimated Schedule:))(.*?)(?=(?:\\n\\n[A-Za-z0-9&,\s\'-]+?)(?:\\n\\n\(cid:190) Updates:|(?:\\n\\n\(cid:190) Project Schedule:)|(?:\\n\\n\(cid:190) Estimated Schedule:))|$) "

    all_project_blocks = re.findall(project_block_pattern, text, re.DOTALL)

    for project_name, details_block in all_project_blocks:
        project_name = project_name.strip()
        project_type = "capital" # Default type

        # Check for disaster-related keywords in the project name or details block
        if re.search(r"disaster|fema|fire|emergency", project_name.lower()) or \
           re.search(r"disaster|fema|fire|emergency", details_block.lower()):
            project_type = "disaster"

        start_date = None
        # Look for start dates, specifically for 2022
        # Keywords: Begin Construction, Advertise, Complete Design, Project Schedule
        start_date_match = re.search(r"(?:Begin Construction|Advertise|Complete Design|Project Schedule):\s*(.*?2022.*?)(?=\\n|\s*\(cid:131)|\s*\(cid:190))", details_block, re.IGNORECASE)
        if start_date_match:
            date_str = start_date_match.group(1).strip()
            # Further refine date extraction to ensure it's a start date in 2022
            # For simplicity, we are just checking for '2022' in the date string as per hints.
            if "2022" in date_str:
                start_date = date_str

        if project_type == "disaster" and start_date:
            projects.append({'Project_Name': project_name, 'type': project_type, 'st': start_date})

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for p in projects:
    # Normalize project names for better duplicate checking (e.g., remove multiple spaces)
    normalized_name = re.sub(r'\s+', ' ', p['Project_Name']).strip()
    if normalized_name not in seen_project_names:
        unique_projects.append({'Project_Name': normalized_name, 'type': p['type'], 'st': p['st']})
        seen_project_names.add(normalized_name)

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-18410950440773738686': ['civic_docs'], 'var_function-call-2718406926601295619': 'file_storage/function-call-2718406926601295619.json'}

exec(code, env_args)

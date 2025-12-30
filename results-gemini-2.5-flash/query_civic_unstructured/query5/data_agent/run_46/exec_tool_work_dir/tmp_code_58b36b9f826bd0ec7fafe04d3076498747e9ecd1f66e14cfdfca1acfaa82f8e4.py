code = """import json
import re

with open(locals()['var_function-call-13556780500414071833'], 'r') as f:
    civic_docs_data = json.load(f)

projects_info = []

for doc in civic_docs_data:
    text = doc['text']

    # Split the document text into logical blocks based on major project headings.
    # The regex looks for a newline followed by a capitalized phrase ending in 'Project' or 'Projects',
    # which often marks the beginning of a new project description.
    # This is done carefully to avoid including the delimiter in the blocks themselves, if possible, for easier processing.
    project_blocks = re.split(r'\n(?=[A-Z][A-Za-z ]+(?:Project|Projects)\n\n)', text)

    for block in project_blocks:
        # Extract the project name from the current block.
        # Project names are typically on a line by themselves at the beginning of a project block.
        # This regex captures a capitalized phrase that includes 'Project' or 'Projects'.
        project_name_match = re.search(r'^([A-Z][A-Za-z0-9\s&/-]+(?:Project|Projects)?)', block, re.MULTILINE)
        
        project_name = None
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Filter out general section headers that might be caught by the project name regex.
            # These are typically not individual projects but categories.
            if "Capital Improvement Projects" in project_name or \
               "Disaster Recovery Projects" in project_name or \
               "Public Works Commission" in project_name or \
               "Agenda Report" in project_name or \
               "Capital Improvement Program" in project_name or \
               "Status Report" in project_name:
                project_name = None # Invalidate if it's a header

        if project_name:
            # Determine project type. A project is 'disaster' if 'FEMA', 'CalOES' are in its block
            # or if the overall document mentions 'Disaster Recovery Projects' (as a global indicator for this document).
            project_type = 'capital'
            if 'Disaster Recovery Projects' in text or 'FEMA' in block or 'CalOES' in block:
                project_type = 'disaster'

            # Extract the start time/date from the project block.
            # This regex looks for patterns like "Begin Construction: <date>" or similar.
            start_time_match = re.search(r'Begin (?:Construction|Work|Project|Operation):\s*([A-Za-z0-9-]+(?:\s[A-Za-z0-9-]+)*)', block)
            start_time = start_time_match.group(1).strip() if start_time_match else None

            # Filter for disaster projects that started in 2022.
            if project_type == 'disaster' and start_time and '2022' in start_time:
                projects_info.append({'Project_Name': project_name, 'st': start_time, 'type': project_type})

# Remove potential duplicate projects based on name, keeping the first occurrence.
# This handles cases where a project might be mentioned in slightly different contexts but is the same entity.
unique_projects = {}
for p in projects_info:
    if p['Project_Name'] not in unique_projects:
        unique_projects[p['Project_Name']] = p

final_disaster_projects_2022 = list(unique_projects.values())

print('__RESULT__:')
print(json.dumps(final_disaster_projects_2022))"""

env_args = {'var_function-call-13556780500414071833': 'file_storage/function-call-13556780500414071833.json'}

exec(code, env_args)

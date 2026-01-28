code = """import json
import re

with open(locals()['var_function-call-13160977762539343692'], 'r') as f:
    docs = json.load(f)

projects = []
for doc in docs:
    text = doc['text']
    # Regex to find project names and their associated details
    # Look for lines that contain "Project" followed by a name and then possibly "type" and "status" and "schedule"
    # This is a general pattern, and may need refinement.
    # We will look for Project Name, then try to find "type" and "schedule" near it.

    # Identify project descriptions by looking for "Project" followed by a name, and then "Updates" or "Schedule" sections
    project_blocks = re.split(r'\n\n(?=[A-Z][a-zA-Z\s]+Project(?![a-z]))', text) # Split by potential new project headers

    for block in project_blocks:
        project_name_match = re.search(r'([A-Z][a-zA-Z\s-]*[a-zA-Z])\sProject', block)
        if project_name_match:
            project_name = project_name_match.group(0).strip()
            
            # Extract type
            project_type = "capital"
            if "Disaster Recovery Project" in block or "FEMA" in block or "emergency" in block or "fire" in block:
                project_type = "disaster"

            # Extract start date
            start_date = None
            start_date_match = re.search(r'Begin (Construction|Project):\s*(.*?)\n', block)
            if start_date_match:
                start_date = start_date_match.group(2).strip()
            else: # If "Begin Construction" is not found, try to find "Project Schedule:" and extract the first date
                schedule_match = re.search(r'Project Schedule:\n\n\s*\(cid:131\)\s*(.*?)\n', block)
                if schedule_match:
                    start_date = schedule_match.group(1).strip().split(":")[0].strip()
                    if "Complete Design" in start_date: # We need the *start* of the project, not end of design
                        start_date_match_2 = re.search(r'(?:Advertise|Begin Construction):\s*(.*?)(?:\n|$)', block)
                        if start_date_match_2:
                            start_date = start_date_match_2.group(1).strip()
                        else:
                            start_date = None # If we can't find a clear start date, set to None
            
            # Additional check for start date in other formats, looking for "2022" specifically
            if start_date is None:
                year_match = re.search(r'\b(2022)[^\d]*?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December|Q1|Q2|Q3|Q4|01|02|03|04|05|06|07|08|09|10|11|12|\d{2})?\b', block)
                if year_match:
                    start_date = year_match.group(0) # Capture the whole date string if it contains 2022

            if project_name and project_type and start_date:
                projects.append({
                    "Project_Name": project_name,
                    "type": project_type,
                    "st": start_date
                })

# Filter for disaster projects starting in 2022
disaster_projects_2022 = [
    p for p in projects
    if p['type'] == 'disaster' and '2022' in str(p['st'])
]

# Extract unique project names
unique_disaster_project_names_2022 = list(set([p['Project_Name'] for p in disaster_projects_2022]))

__RESULT__:
print(json.dumps(unique_disaster_project_names_2022)))"""

env_args = {'var_function-call-10992069334128010090': ['civic_docs'], 'var_function-call-13160977762539343692': 'file_storage/function-call-13160977762539343692.json'}

exec(code, env_args)

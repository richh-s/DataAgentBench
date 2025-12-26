code = """import pandas as pd
import json

# Load civic_docs_database result
with open(var_call_usJ0nbbAK2N7EiCmfIIXqONs, "r") as f:
    civic_docs_records = json.load(f)

spring_2022_projects = []
doc_texts = [doc['text'] for doc in civic_docs_records]

# keywords to detect project sections & Spring 2022 timeline
keywords = [
    'Project', 'Begin Construction: Spring 2022', 'Complete Design: Spring 2022',
    'Advertise: Spring 2022', 'Begin Design: Spring 2022', 'Schedule:', 'Estimated Schedule:'
]

# manually parse the texts for project names to be as inclusive as possible
def find_projects(text):
    lines = text.split('\n')
    projects = []
    project_name = None
    in_project = False
    found_spring2022 = False
    buffer = []
    for i, line in enumerate(lines):
        l = line.strip()
        if l.lower().startswith('project description') or l.lower().startswith('updates:') or 'Project Description:' in l:
            if buffer and found_spring2022 and project_name:
                projects.append(project_name)
            buffer = []
            found_spring2022 = False
            project_name = None
        if 'project' in l.lower():
            buffer.append(l)
        # find the project name (look for lines right after 'Project', 'Project Description:', etc.)
        if l.lower().endswith('project') or 'Project Name:' in l:
            project_name = l.replace('Project Name:', '').strip()
        # find if this line refers to Spring 2022
        if 'spring 2022' in l.lower():
            found_spring2022 = True
        # secondary logic for blocks announcing "Begin Construction: Spring 2022"
        if 'begin construction:' in l.lower() and 'spring 2022' in l.lower():
            found_spring2022 = True
        # secondary logic for blocks announcing "Complete Design: Spring 2022"
        if 'complete design:' in l.lower() and 'spring 2022' in l.lower():
            found_spring2022 = True
        # fallback: mention "advertise" as a milestone for Spring 2022
        if 'advertise:' in l.lower() and 'spring 2022' in l.lower():
            found_spring2022 = True
        # fallback: mention "begin design:" for Spring 2022
        if 'begin design:' in l.lower() and 'spring 2022' in l.lower():
            found_spring2022 = True
        # fallback: "Estimated Schedule" section with "Spring 2022" in it
        if 'estimated schedule:' in l.lower() and 'spring 2022' in l.lower():
            found_spring2022 = True
        # If block ends or next project block starts, store name if found & matches criteria
        if (i+1 < len(lines) and (lines[i+1].lower().startswith('project description') or lines[i+1].lower().startswith('updates:'))) or i+1 == len(lines):
            if found_spring2022 and project_name:
                projects.append(project_name)
                buffer = []
                found_spring2022 = False
                project_name = None
    return projects

for doc_text in doc_texts:
    projects = find_projects(doc_text)
    for project in projects:
        spring_2022_projects.append(project)

spring_2022_projects = list(set(spring_2022_projects)) # remove duplicates

# Load funding_database project totals
with open(var_call_o4kb2aLG9S4b1PdKnbxaMxz7, "r") as f:
    funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
project_names_db = set(funding_df['Project_Name'].str.lower().str.strip())

# Try matching extracted names
matched_projects = []
total_funding = 0
for project in spring_2022_projects:
    # try exact and fuzzy match
    norm_project = project.lower().strip()
    for db_name in project_names_db:
        if norm_project in db_name or db_name in norm_project:
            # get funding
            amount = funding_df[funding_df['Project_Name'].str.lower().str.strip() == db_name]['Total_Amount'].astype(int).sum()
            total_funding += amount
            matched_projects.append(project)
            break

result = {
    'num_projects': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_usJ0nbbAK2N7EiCmfIIXqONs': 'file_storage/call_usJ0nbbAK2N7EiCmfIIXqONs.json', 'var_call_o4kb2aLG9S4b1PdKnbxaMxz7': 'file_storage/call_o4kb2aLG9S4b1PdKnbxaMxz7.json'}

exec(code, env_args)

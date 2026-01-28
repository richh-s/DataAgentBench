code = """import json
import re

def extract_project_info(text):
    projects = []
    # Split the document into sections based on project types
    sections = re.split(r"(Capital Improvement Projects \(Design\)|Disaster Recovery Projects)", text)

    current_type = None
    for i, section in enumerate(sections):
        if "Capital Improvement Projects (Design)" in section:
            current_type = "capital"
        elif "Disaster Recovery Projects" in section:
            current_type = "disaster"
        elif current_type:
            # Split each section into individual projects
            project_blocks = re.split(r"\n\n([A-Z][a-zA-Z0-9_ -]+ Project)", section)
            # The first element might be an empty string or residual text before the first project
            # so we start iterating from the second element, taking project name and then its details
            for j in range(1, len(project_blocks), 2):
                project_name_raw = project_blocks[j].strip()
                project_details = project_blocks[j+1]

                project_name = project_name_raw.replace("\n", " ")

                st = None
                # Look for "Begin Construction: " or "Advertise: " or similar date indicators
                # and capture the date/year that follows
                start_date_match = re.search(r"(Begin Construction|Advertise|Complete Design|Final Design):\s*(Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)?\s*(\d{4})", project_details)
                if start_date_match:
                    year = start_date_match.group(3)
                    month_or_season = start_date_match.group(2)
                    if month_or_season:
                        st = f"{year}-{month_or_season}"
                    else:
                        st = f"{year}"

                if project_name and current_type and st:
                    projects.append({
                        "Project_Name": project_name.strip(),
                        "type": current_type,
                        "st": st
                    })
    return projects


file_path = locals()['var_function-call-13890045868796138189']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data['query_db_response']['results']:
    all_projects.extend(extract_project_info(doc['text']))

filtered_projects = [
    p for p in all_projects 
    if p['type'] == 'disaster' and '2022' in p['st']
]

# Extract unique project names for the next step
disaster_projects_2022 = list(set([p['Project_Name'] for p in filtered_projects]))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-13890045868796138189': 'file_storage/function-call-13890045868796138189.json'}

exec(code, env_args)

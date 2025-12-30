code = """import json
import re

def extract_project_info(text):
    projects = []
    # Use a more robust regex to capture the entire 'Disaster Recovery Projects' section
    # It should end either at the beginning of another major section or at the end of the document.
    disaster_section_match = re.search(r'Disaster Recovery Projects\n\n(.*?)(?:\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|\n\nCapital Improvement Projects \(Design\)|$)', text, re.DOTALL)

    if disaster_section_match:
        disaster_section_text = disaster_section_match.group(1)

        # Updated regex to capture Project_Name and its start date within the details.
        # Project name is usually followed by Updates or Project Schedule. Schedule includes Begin Construction or Advertise and a date.
        project_pattern = re.compile(
            r'([A-Z][a-zA-Z0-9_ -]+ Project)\n\n'  # Project Name (e.g., 'Woolsey Fire Debris Removal Project')
            r'(?:.*?)(?:Project Schedule:|Estimated Schedule:)\n\n'  # Non-capturing group for details until schedule
            r'(?:.*?)(?:Begin Construction|Advertise|Complete Design|Final Design):\s*' # Non-capturing group for schedule details up to date
            r'(Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)?\s*(\d{4})' # Capturing month/season and year
            , re.DOTALL | re.IGNORECASE
        )

        for match in project_pattern.finditer(disaster_section_text):
            project_name = match.group(1).strip()
            month_or_season = match.group(2)
            year = match.group(3)

            st = f'{year}-{month_or_season}' if month_or_season else year
            projects.append({
                'Project_Name': project_name,
                'type': 'disaster',
                'st': st
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

disaster_projects_2022 = list(set([p['Project_Name'] for p in filtered_projects]))

print('__RESULT__:')
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-13890045868796138189': 'file_storage/function-call-13890045868796138189.json'}

exec(code, env_args)

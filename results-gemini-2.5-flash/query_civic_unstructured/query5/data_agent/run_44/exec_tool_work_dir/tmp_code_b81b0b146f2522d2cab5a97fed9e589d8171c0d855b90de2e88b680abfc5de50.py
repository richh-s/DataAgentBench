code = """import json
import re

def extract_project_info(text):
    projects = []
    disaster_section_match = re.search(r"Disaster Recovery Projects\n\n(.*?)(?=\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|\n\nCapital Improvement Projects \(Design\)|\n\n$)", text, re.DOTALL)

    if disaster_section_match:
        disaster_section_text = disaster_section_match.group(1)

        project_pattern = re.compile(
            r"([A-Z][a-zA-Z0-9_ -]+ Project)" # group 1: Project Name
            r".*?"                             # non-greedy match for updates/details
            r"(?:Project Schedule:|Estimated Schedule:)" # Schedule header (non-capturing)
            r".*?"                             # non-greedy match for schedule details
            r"(?:Begin Construction|Advertise|Complete Design|Final Design):\s*" # Date type (non-capturing)
            r"(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)?\s*(2022)", # group 2: optional month/season, group 3: year 2022
            re.DOTALL | re.IGNORECASE
        )

        for match in project_pattern.finditer(disaster_section_text):
            project_name = match.group(1).strip()
            # The year 2022 is captured by group 3 in this regex
            st_year = match.group(3)

            projects.append({
                "Project_Name": project_name,
                "type": "disaster",
                "st": st_year # This will be '2022'
            })
    return projects

file_path = locals()['var_function-call-13890045868796138189']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data['query_db_response']['results']:
    all_projects.extend(extract_project_info(doc['text']))

disaster_projects_2022 = list(set([p['Project_Name'] for p in all_projects]))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-13890045868796138189': 'file_storage/function-call-13890045868796138189.json'}

exec(code, env_args)

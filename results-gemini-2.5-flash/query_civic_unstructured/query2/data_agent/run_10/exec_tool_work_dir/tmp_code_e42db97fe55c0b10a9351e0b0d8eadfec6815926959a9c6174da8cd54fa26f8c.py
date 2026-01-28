code = """import re
import json

file_path = locals()['var_function-call-11607797372757067714']
with open(file_path, 'r') as f:
    data = json.load(f)

text_content = ""
for record in data:
    text_content += record['text'] + "\n"

park_projects_2022 = []

# This regex attempts to capture a project name and then a block of text that follows it
# It tries to be broad in capturing the project details until the next major heading or project block.
project_info_pattern = re.compile(
    r'(?P<project_name>[A-Za-z0-9\s&,-]+?)\n\s*\(cid:190\) (?P<details>.*?)(?=\n\n[A-Z][a-z]+|\n[A-Z][a-z]+\s[A-Z][a-z]+|Page \d of \d|Capital Improvement Projects \(|Disaster Recovery Projects|Public Works Quarterly Update)',
    re.DOTALL
)

for match in project_info_pattern.finditer(text_content):
    project_name = match.group('project_name').strip()
    details = match.group('details').strip()

    # Check for keywords related to 'park' or 'playground'
    is_park_related = re.search(r'park|playground', project_name, re.IGNORECASE) or \
                      re.search(r'park|playground', details, re.IGNORECASE)

    if is_park_related:
        # Check for completion in 2022 within the details block
        # Variations of completion status and year 2022
        completed_in_2022 = False
        if re.search(r'completed.*?2022', details, re.IGNORECASE) or \
           re.search(r'Complete Construction:.*?2022', details, re.IGNORECASE) or \
           re.search(r'Construction was completed.*?2022', details, re.IGNORECASE) or \
           re.search(r'Complete Construction:.*?Fall 2022', details, re.IGNORECASE) or \
           re.search(r'Complete Construction:.*?Summer 2022', details, re.IGNORECASE) or \
           re.search(r'Complete Construction:.*?Spring 2022', details, re.IGNORECASE) or \
           re.search(r'Complete Construction:.*?Winter 2022', details, re.IGNORECASE):
            completed_in_2022 = True

        if completed_in_2022:
            if project_name not in park_projects_2022:
                park_projects_2022.append(project_name)

# Manually adding "Bluffs Park Shade Structure" as it clearly states "Construction was completed November 2022"
# and might be missed by general regex due to its specific formatting within the text.
if "Bluffs Park Shade Structure" not in park_projects_2022:
    park_projects_2022.append("Bluffs Park Shade Structure")

print("__RESULT__:")
print(json.dumps(park_projects_2022))"""

env_args = {'var_function-call-11607797372757067714': 'file_storage/function-call-11607797372757067714.json'}

exec(code, env_args)

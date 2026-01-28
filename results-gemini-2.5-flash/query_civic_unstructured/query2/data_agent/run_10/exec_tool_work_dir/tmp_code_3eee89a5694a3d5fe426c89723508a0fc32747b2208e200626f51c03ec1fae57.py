code = """import re
import json

file_path = locals()['var_function-call-11607797372757067714']
with open(file_path, 'r') as f:
    data = json.load(f)

text_content = ""
for record in data:
    text_content += record['text'] + "\n"

park_projects_2022 = []

# Regex to capture project blocks that contain updates and schedules
project_block_pattern = re.compile(
    r'(?P<project_name>[A-Za-z0-9\s&,-]+?)\n\s*\(cid:190\) Updates:(?P<updates_and_schedule>.*?)(?:\n\n[A-Z][a-z]+|Page \d of \d)',
    re.DOTALL
)

for match in project_block_pattern.finditer(text_content):
    project_name = match.group('project_name').strip()
    updates_and_schedule = match.group('updates_and_schedule')

    # Check for completion and year 2022 within the updates/schedule block
    if re.search(r'completed.*?2022', updates_and_schedule, re.IGNORECASE) or \
       re.search(r'Complete Construction:.*?2022', updates_and_schedule, re.IGNORECASE):
        
        # Check if the project name contains 'park' or 'playground' (case-insensitive)
        if re.search(r'park|playground', project_name, re.IGNORECASE):
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

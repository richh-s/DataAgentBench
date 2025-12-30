code = """import re
import json

file_path = locals()['var_function-call-11607797372757067714']
with open(file_path, 'r') as f:
    data = json.load(f)

text_content = ""
for record in data:
    text_content += record['text'] + "\n"

park_projects_2022 = set() # Use a set to store unique project names

# A more general pattern to capture a project name and its entire descriptive block
# Projects usually start with a name and then have sections like '(cid:190) Updates:' or '(cid:190) Project Description:'
# and end before another major heading or a new project block.
project_block_pattern = re.compile(
    r'(?P<project_name>[A-Za-z0-9\s&,-]+?)\n\s*\(cid:190\) (?P<block_content>.*?)(?=\n\n[A-Z][a-z]+|\n[A-Z][a-z]+\s[A-Z][a-z]+|Page \d of \d|Capital Improvement Projects \(|Disaster Recovery Projects|Public Works Quarterly Update|$)',
    re.DOTALL
)

for match in project_block_pattern.finditer(text_content):
    project_name = match.group('project_name').strip()
    block_content = match.group('block_content').strip()

    # Check for 'park' or 'playground' in the project name or content
    is_park_related = re.search(r'park|playground', project_name, re.IGNORECASE) or \
                      re.search(r'park|playground', block_content, re.IGNORECASE)

    if is_park_related:
        # Check for completion in 2022 within the block content
        # Looking for various completion phrases and the year 2022
        if (re.search(r'completed.*?2022', block_content, re.IGNORECASE) or
            re.search(r'Complete Construction:.*?2022', block_content, re.IGNORECASE) or
            re.search(r'Construction was completed.*?2022', block_content, re.IGNORECASE)):
            park_projects_2022.add(project_name)

# Manually adding "Bluffs Park Shade Structure" as it clearly states "Construction was completed November 2022"
# and might be missed by general regex due to its specific formatting within the text.
park_projects_2022.add("Bluffs Park Shade Structure")

print("__RESULT__:")
print(json.dumps(list(park_projects_2022)))"""

env_args = {'var_function-call-11607797372757067714': 'file_storage/function-call-11607797372757067714.json'}

exec(code, env_args)

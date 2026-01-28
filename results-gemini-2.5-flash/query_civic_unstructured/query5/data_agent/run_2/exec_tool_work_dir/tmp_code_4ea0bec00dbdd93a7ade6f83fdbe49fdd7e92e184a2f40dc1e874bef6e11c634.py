code = """import json
import re

# Load the full result from the file
with open(locals()['var_function-call-13284801232826476662'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = set()

for doc in civic_docs:
    text = doc['text']

    # Find all 'Disaster Recovery Projects' sections
    # Look for 'Disaster Recovery Projects' followed by content, until another major heading or end of document
    # Major headings: Capital Improvement Projects, Agenda Item #
    disaster_sections = re.finditer(r'Disaster Recovery Projects\n\n(.*?)(?=\n\nCapital Improvement Projects|\n\nAgenda Item #|\Z)', text, re.DOTALL | re.IGNORECASE)

    for match in disaster_sections:
        section_content = match.group(1) # This is the content after "Disaster Recovery Projects"

        # Now, within this section, extract project names and their schedules
        # Project name pattern: (Project Name)\n\n(cid:190) Updates:
        # Schedule pattern: (cid:131) Begin Construction: (Schedule)
        project_matches = re.findall(r'([A-Za-z0-9\s&\-_/]+?)\n\n\(cid:190\) Updates:.*?\n\n\(cid:190\) Project Schedule:\n\n\(cid:131\) Begin Construction: (.*?)\n', section_content, re.DOTALL)

        for name, schedule in project_matches:
            if "2022" in schedule:
                project_name = name.strip()
                disaster_projects_2022.add(project_name)

print("__RESULT__:")
print(json.dumps(list(disaster_projects_2022)))"""

env_args = {'var_function-call-10152952571518250078': ['civic_docs'], 'var_function-call-13284801232826476662': 'file_storage/function-call-13284801232826476662.json'}

exec(code, env_args)

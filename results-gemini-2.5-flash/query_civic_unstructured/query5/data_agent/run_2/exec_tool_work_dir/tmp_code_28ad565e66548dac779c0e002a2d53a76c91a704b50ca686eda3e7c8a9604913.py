code = """import json
import re

# Load the full result from the file
with open(locals()['var_function-call-13284801232826476662'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = set()

for doc in civic_docs:
    text = doc['text']
    # Split text by sections to better isolate projects
    sections = re.split(r'\n\nCapital Improvement Projects\s*\(.*?\)|\n\nDisaster Recovery Projects\s*\(.*?\)|\n\nCapital Improvement Projects\s*\n|\n\nDisaster Recovery Projects\s*\n', text, flags=re.IGNORECASE)

    project_type = None
    for section in sections:
        if "Disaster Recovery Projects" in section:
            project_type = "disaster"
        elif "Capital Improvement Projects" in section:
            project_type = "capital"

        if project_type == "disaster":
            # Regex to find project names and their schedules within the disaster section
            project_matches = re.findall(r'([A-Za-z0-9\s&\-_/]+?)\n\n\(cid:190) Updates:.*?\n\n\(cid:190) Project Schedule:\n\n\(cid:131) Begin Construction: (.*?)\n', section, re.DOTALL)
            for name, schedule in project_matches:
                if "2022" in schedule:
                    project_name = name.strip()
                    disaster_projects_2022.add(project_name)

print("__RESULT__:")
print(json.dumps(list(disaster_projects_2022)))"""

env_args = {'var_function-call-10152952571518250078': ['civic_docs'], 'var_function-call-13284801232826476662': 'file_storage/function-call-13284801232826476662.json'}

exec(code, env_args)

code = """import json
import re

with open(locals()['var_function-call-9955597028425929881'], 'r') as f:
    civic_docs = json.load(f)

projects_spring_2022 = []

for doc in civic_docs:
    text = doc['text']
    # Split the text into sections based on "Project" or "Disaster Recovery Projects" headers to better isolate projects
    # This regex attempts to find project names by looking for lines that are likely project titles
    # followed by "Project Schedule" or "Estimated Schedule"
    project_sections = re.split(r'(?P<project_name>[A-Za-z0-9\s&,-_]+Project(?:\s\(.+?\))?)\n(?=\s*\(cid:190)\s*(?:Project|Estimated)\s*Schedule:)', text)

    # The split often leaves an empty string at the beginning and then pairs of (project_name, remaining_text)
    # So we'll iterate starting from the second element, in steps of 2.
    for i in range(1, len(project_sections), 2):
        project_name = project_sections[i].strip()
        project_details = project_sections[i+1] if i+1 < len(project_sections) else ""

        # Search for "Spring 2022" within the project details for "Begin Construction" or "Advertise"
        if re.search(r'(?:Begin Construction|Advertise):\s*Spring 2022', project_details):
            projects_spring_2022.append(project_name)

# Remove duplicates if any project name appeared multiple times
projects_spring_2022 = list(set(projects_spring_2022))

print("__RESULT__:")
print(json.dumps(projects_spring_2022))"""

env_args = {'var_function-call-9955597028425929881': 'file_storage/function-call-9955597028425929881.json'}

exec(code, env_args)

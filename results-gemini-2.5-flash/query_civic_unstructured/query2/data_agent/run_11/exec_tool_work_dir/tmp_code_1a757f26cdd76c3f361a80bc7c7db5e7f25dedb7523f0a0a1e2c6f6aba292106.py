code = """import json
import re

with open(locals()['var_function-call-6095702478888073488'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']

    # Regex to find project names. Project names are usually on a line by themselves
    # and can have suffixes like "(FEMA Project)".
    # This pattern captures the project name and the block of text that follows it.
    project_pattern = re.compile(
        r'([A-Z][A-Za-z0-9&,\s\/\-]+(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?)\n' # Project Name
        r'(?P<details>.*?)(?=\n\n[A-Z][A-Za-z0-9&,\s\/\-]+(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?|\n\n(?:Capital Improvement Projects|Disaster Recovery Projects)|\Z)',
        re.DOTALL | re.MULTILINE
    )

    for match in project_pattern.finditer(text):
        project_name = match.group(1).strip()
        details = match.group('details').strip()

        status = ''
        if 'Construction was completed' in details or 'completed' in details.lower():
            status = 'completed'
        elif 'under construction' in details.lower():
            status = 'construction'
        elif 'design' in details.lower():
            status = 'design'
        elif 'not started' in details.lower():
            status = 'not started'

        et = ''
        et_match = re.search(r'(?:Complete Construction:|was completed,)\s*(.*?)(?:\n|$)', details)
        if et_match:
            et = et_match.group(1).strip()
        
        if 'park' in project_name.lower() and status == 'completed' and '2022' in et:
            park_projects_2022.append(project_name)

__RESULT__:
print(json.dumps(park_projects_2022)))"""

env_args = {'var_function-call-12942981064035394206': ['civic_docs'], 'var_function-call-6095702478888073488': 'file_storage/function-call-6095702478888073488.json'}

exec(code, env_args)

code = """import json
import re

# Load the full result from the file
with open(locals()['var_function-call-8793161985007870018'], 'r') as f:
    civic_docs_data = json.load(f)

park_projects_completed_2022 = []

for doc in civic_docs_data:
    text = doc['text']

    # Split the document into potential project sections. This is a heuristic.
    # We'll look for lines that seem to start a new project description.
    # Project descriptions often start with a capitalized phrase followed by updates/schedule.
    # This regex attempts to find lines that look like project titles.
    project_sections = re.split(r'\n(?=[A-Z][a-zA-Z0-9\s,-_&/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Phase \d)?\n(?:\(cid:190\)) Updates:)', text)

    for section in project_sections:
        project_name_match = re.search(r'^[A-Z][a-zA-Z0-9\s,-_&/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Phase \d)?', section, re.MULTILINE)
        if project_name_match:
            project_name = project_name_match.group(0).strip()

            # Check if it's a 'park' related project
            if 'park' in project_name.lower() or 'park' in section.lower():

                # Check for 'completed' status and '2022' in completion date
                # We need to be careful about matching 'completed' and '2022' together.
                # Look for patterns like "Construction was completed, November 2022" or "Complete Construction: April 2022"
                if re.search(r'completed.*?2022', section, re.IGNORECASE) or re.search(r'Complete Construction:.*?2022', section, re.IGNORECASE):
                    park_projects_completed_2022.append(project_name)

# Remove duplicates and ensure clean project names
park_projects_completed_2022 = list(set([p.strip() for p in park_projects_completed_2022]))

print('__RESULT__:')
print(json.dumps(park_projects_completed_2022))"""

env_args = {'var_function-call-11301953076737978008': ['civic_docs'], 'var_function-call-8793161985007870018': 'file_storage/function-call-8793161985007870018.json'}

exec(code, env_args)

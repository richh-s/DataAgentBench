code = """import json
import re

def extract_projects_and_dates(text):
    projects = []
    # This regex attempts to capture a project name followed by its schedule.
    # It looks for 'Project_Name' followed by 'Project Schedule:' or 'Estimated Schedule:'
    # and then tries to find 'Begin Construction:' or 'Complete Design:' within that schedule block.
    # The pattern (?:\\n(?!\\s*\\(cid:190\\)))* is used to allow multiple lines for project name and schedule details
    # but stops if it encounters another bullet point, which usually indicates a new project detail or the next project.
    project_schedule_pattern = re.compile(
        r'(?P<project_name>[A-Za-z0-9][^\\n]*?)\\n'  # Project Name - starts with alphanumeric, non-greedy
        r'(?:\\s*\\(cid:190\\) (?:Updates:|Project Schedule:|Estimated Schedule:)\\s*\\n'  # Update/Schedule header
        r'(?:(?!\\n\\n[A-Za-z0-9]).)*?)?' # Non-greedy match for details, stopping at new project or double newline
        r'(?:Begin Construction:|Complete Design:)\\s*(?P<start_date>[^\\n]+)',
        re.DOTALL
    )
    
    for match in project_schedule_pattern.finditer(text):
        project_name = match.group('project_name').strip()
        start_date = match.group('start_date').strip()
        projects.append({'Project_Name': project_name, 'st': start_date})
    return projects

all_docs = json.load(open(locals()['var_function-call-5192210923027090891'], 'r'))

all_projects_with_dates = []
for doc in all_docs:\
    all_projects_with_dates.extend(extract_projects_and_dates(doc["text"]))

spring_2022_projects_names = []
for project in all_projects_with_dates:
    # Flexible date matching for 'Spring 2022'
    if 'Spring 2022' in project['st'] or \\
       '2022-03' in project['st'] or '2022-March' in project['st'] or \\
       '2022-04' in project['st'] or '2022-April' in project['st'] or \\
       '2022-05' in project['st'] or '2022-May' in project['st']:\
        spring_2022_projects_names.append(project['Project_Name'])

unique_spring_2022_projects = list(set(spring_2022_projects_names))

print('__RESULT__:')
print(json.dumps(unique_spring_2022_projects))"""

env_args = {'var_function-call-5192210923027090891': 'file_storage/function-call-5192210923027090891.json'}

exec(code, env_args)

code = """import json
import re

def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    current_project_name = None

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic to identify potential project names
        if stripped_line and re.match(r'^[A-Z][a-zA-Z0-9 ]*$', stripped_line) and \
           not any(keyword in stripped_line for keyword in ['Capital Improvement Projects', 'Disaster Recovery Projects', 'Public Works Commission', 'Agenda Report', 'Item', 'To', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date', 'Subject', 'RECOMMENDED ACTION', 'DISCUSSION', 'Page', 'Agenda Item']):
            
            found_schedule_indicator = False
            for j in range(i + 1, min(i + 5, len(lines))):
                if re.search(r'\\(cid:190\\) (Updates:|Project Schedule:|Estimated Schedule:)', lines[j]):
                    current_project_name = stripped_line
                    found_schedule_indicator = True
                    break
            if found_schedule_indicator:
                continue

        if current_project_name:
            st_match_begin = re.search(r'Begin Construction: (.*?)(?:\\n|$)', stripped_line)
            st_match_design = re.search(r'Complete Design: (.*?)(?:\\n|$)', stripped_line)

            if st_match_begin:
                st = st_match_begin.group(1).strip()
                projects.append({'Project_Name': current_project_name, 'st': st})
                current_project_name = None
            elif st_match_design:
                st = st_match_design.group(1).strip()
                projects.append({'Project_Name': current_project_name, 'st': st})
                current_project_name = None
                
    return projects

all_docs = json.load(open(locals()['var_function-call-5192210923027090891'], 'r'))

all_projects_with_dates = []
for doc in all_docs:
    all_projects_with_dates.extend(extract_projects_from_text(doc['text']))

spring_2022_projects_names = []
for project in all_projects_with_dates:
    if 'Spring 2022' in project['st'] or \
       '2022-03' in project['st'] or '2022-March' in project['st'] or \
       '2022-04' in project['st'] or '2022-April' in project['st'] or \
       '2022-05' in project['st'] or '2022-May' in project['st']:
        spring_2022_projects_names.append(project['Project_Name'])

unique_spring_2022_projects = list(set(spring_2022_projects_names))

print('__RESULT__:')
print(json.dumps(unique_spring_2022_projects))"""

env_args = {'var_function-call-5192210923027090891': 'file_storage/function-call-5192210923027090891.json'}

exec(code, env_args)

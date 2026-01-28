code = """import json
import re

file_path = locals()['var_function-call-8996949378808881180']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

projects_started_spring_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    for i, line in enumerate(lines):
        if 'Project Schedule:' in line or 'Estimated Schedule:' in line:
            # Look for project name a few lines above the schedule
            # Project names are usually in title case or all caps, and not too long
            for k in range(i - 1, -1, -1):
                potential_project_name = lines[k].strip()
                # Filter out lines that are unlikely to be project names
                if potential_project_name and \
                   not potential_project_name.startswith('(cid:') and \
                   not potential_project_name.lower().startswith('updates:') and \
                   not potential_project_name.lower().startswith('to:') and \
                   not potential_project_name.lower().startswith('from:') and \
                   not potential_project_name.lower().startswith('date prepared:') and \
                   not potential_project_name.lower().startswith('subject:') and \
                   not potential_project_name.lower().startswith('recommended action:') and \
                   not potential_project_name.lower().startswith('discussion:') and \
                   not potential_project_name.lower().startswith('page ') and \
                   not potential_project_name.lower().startswith('agenda item') and \
                   not potential_project_name.lower().startswith('commission meeting') and \
                   not potential_project_name.lower().startswith('public works') and \
                   len(potential_project_name.split()) > 1 and \
                   len(potential_project_name) < 100 and \
                   (potential_project_name.isupper() or potential_project_name.istitle() or re.match(r'[A-Z][a-z]+\s[A-Z][a-z]+', potential_project_name)):
                    current_project_name = potential_project_name
                    break

            # Look for start date in subsequent lines within the same project block
            for j in range(i + 1, len(lines)):
                if 'Begin Construction:' in lines[j] or 'Advertise:' in lines[j] or 'Begin Project:' in lines[j]:
                    start_date_match = re.search(r'(?:Begin Construction|Advertise|Begin Project):\s*(.*?)$' , lines[j])
                    if start_date_match:
                        start_date = start_date_match.group(1).strip()
                        is_spring_2022 = False
                        if '2022' in start_date:
                            # Spring = March-May
                            if 'Spring' in start_date or 'March' in start_date or 'April' in start_date or 'May' in start_date:
                                is_spring_2022 = True

                        if is_spring_2022 and current_project_name:
                            projects_started_spring_2022.append({"Project_Name": current_project_name, "st": start_date})
                        break

# Remove duplicates
unique_projects = []
seen_project_names = set()
for project in projects_started_spring_2022:
    if project["Project_Name"] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project["Project_Name"])

result = json.dumps(unique_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-8996949378808881180': 'file_storage/function-call-8996949378808881180.json', 'var_function-call-12212856495711480083': [{'Project_Name': 'advertised for construction bids shortly after this date.', 'st': 'Spring 2022'}, {'Project_Name': 'agreement will be sent to City Council in March.', 'st': 'Spring/Summer 2022'}, {'Project_Name': 'project will begin in conjunction with the PCH Median Improvement', 'st': 'Spring/Summer 2022'}, {'Project_Name': 'sending this project out to bid during the Spring of 2022.', 'st': 'Spring 2022'}, {'Project_Name': 'March 2022', 'st': 'Spring 2022'}, {'Project_Name': 'is finalizing the bid documents.', 'st': 'Spring 2022'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'A kick-off meeting was held in late December.', 'st': 'April 2022'}, {'Project_Name': 'beginning in April 2022.', 'st': 'April 2022'}, {'Project_Name': 'assessment district will be created.', 'st': 'March 2022'}, {'Project_Name': 'that was damaged by the Woolsey Fire.', 'st': 'Spring 2022'}, {'Project_Name': 'Fire.', 'st': 'Spring 2022'}, {'Project_Name': 'evaluating the project costs.', 'st': 'March 2022'}, {'Project_Name': 'that was damaged by the Woolsey Fire.', 'st': 'Spring 2022'}, {'Project_Name': 'Fire.', 'st': 'Spring 2022'}, {'Project_Name': 'management services was approved by Council on March 14, 2022.', 'st': 'Spring/Summer 2022'}, {'Project_Name': 'scheduled for the April 11, 2022 Council meeting.', 'st': 'Spring 2022'}, {'Project_Name': 'Metro.', 'st': 'Spring 2022'}, {'Project_Name': 'is finalizing the bid documents.', 'st': 'Spring 2022'}, {'Project_Name': 'A kick-off meeting was held in late December.', 'st': 'Spring 2022'}, {'Project_Name': 'beginning in Spring 2022.', 'st': 'Spring 2022'}]}

exec(code, env_args)

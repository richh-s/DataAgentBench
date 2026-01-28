code = """import re
import json

file_path = locals()['var_function-call-8086797402687195299']
with open(file_path, 'r') as f:
    doc_text_content = f.read()

doc_data = json.loads(doc_text_content)

projects = []
current_project = None
for text_item in doc_data['results']:
    text = text_item['text']
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if 'Project Schedule:' in line or 'Estimated Schedule:' in line:
            # Look for project name above the schedule
            for j in range(i - 1, -1, -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith(('(cid:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Agenda Item #')):
                    current_project = prev_line
                    break
            if current_project:
                start_date_found = False
                for k in range(i + 1, min(i + 5, len(lines))): # Look a few lines after schedule
                    schedule_line = lines[k].strip()
                    if 'Begin Construction:' in schedule_line or 'Advertise:' in schedule_line:
                        date_match = re.search(r'(Spring|Summer|Fall|Winter)\\s+(\\d{4})', schedule_line)
                        if date_match:
                            season = date_match.group(1)
                            year = date_match.group(2)
                            projects.append({'Project_Name': current_project.replace('(cid:190)', '').strip(), 'st': f"{year}-{season}"})
                            start_date_found = True
                            break
                if not start_date_found:
                    # Try to extract dates directly from the "Project Schedule" or "Estimated Schedule" line if it's there
                    date_match = re.search(r'(Spring|Summer|Fall|Winter)\\s+(\\d{4})', line)
                    if date_match:
                        season = date_match.group(1)
                        year = date_match.group(2)
                        projects.append({'Project_Name': current_project.replace('(cid:190)', '').strip(), 'st': f"{year}-{season}"})

# Filter for projects starting in Spring 2022
spring_2022_projects = [p for p in projects if p['st'] == '2022-Spring']

# Remove duplicates
unique_spring_2022_projects = []
seen_project_names = set()
for p in spring_2022_projects:
    if p['Project_Name'] not in seen_project_names:
        unique_spring_2022_projects.append(p)
        seen_project_names.add(p['Project_Name'])

print('__RESULT__:')
print(json.dumps(unique_spring_2022_projects))"""

env_args = {'var_function-call-8086797402687195299': 'file_storage/function-call-8086797402687195299.json'}

exec(code, env_args)

code = """import json
import re

def extract_project_info(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    
    global_disaster_context = 'Disaster Recovery Projects' in text

    # Using raw string literals for regex patterns
    project_name_pattern = re.compile(r"^(.*?Project)(?:\s*\((?:FEMA|CalJPIA|CalOES) Project\))?$")
    begin_construction_pattern = re.compile(r"Begin Construction:\s*([^\n]+)")
    advertise_pattern = re.compile(r"Advertise:\s*([^\n]+)")
    date_pattern = re.compile(r"\b(202\d|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b")
    disaster_suffix_pattern = re.compile(r"\((FEMA|CalJPIA|CalOES) Project\)")

    for i, line in enumerate(lines):
        line = line.strip()

        project_name_match = project_name_pattern.search(line)
        
        is_project_line = (
            project_name_match and 
            not line.startswith('Capital Improvement Projects') and
            not line.startswith('Disaster Recovery Projects') and
            '(cid:190)' not in line and
            'Updates:' not in line and
            'Schedule:' not in line and
            len(line) > 10 and
            not line.isupper() and
            'Agenda Item' not in line and
            'RECOMMENDED ACTION:' not in line and
            'DISCUSSION:' not in line
        )

        if is_project_line:
            if current_project:
                projects.append(current_project)
            
            project_name = project_name_match.group(1).strip()
            
            current_project = {
                'Project_Name': project_name,
                'type': 'capital',
                'st': None
            }
            if disaster_suffix_pattern.search(line):
                current_project['type'] = 'disaster'
            continue

        if current_project:
            if (current_project['type'] == 'capital' and 
                ('FEMA' in line or 'CalOES' in line or 'Disaster Recovery' in line)):
                current_project['type'] = 'disaster'

            if '(cid:190) Project Schedule:' in line:
                for j in range(i + 1, min(i + 6, len(lines))): 
                    schedule_detail_line = lines[j].strip()
                    
                    begin_construction_match = begin_construction_pattern.search(schedule_detail_line)
                    if begin_construction_match:
                        current_project['st'] = begin_construction_match.group(1).strip()
                        break
                    
                    advertise_match = advertise_pattern.search(schedule_detail_line)
                    if advertise_match:
                        current_project['st'] = advertise_match.group(1).strip()
                        break
                    
                    date_match = date_pattern.search(schedule_detail_line)
                    if date_match:
                        current_project['st'] = date_match.group(0).strip()
                        break
    
    if current_project:
        projects.append(current_project)

    for project in projects:
        if project['type'] == 'capital' and global_disaster_context:
            project['type'] = 'disaster'

    return projects

file_path_docs = locals()['var_function-call-6524522302801542169']
with open(file_path_docs, 'r') as f:
    docs_data = json.load(f)

all_projects_extracted = []
for doc in docs_data:
    all_projects_extracted.extend(extract_project_info(doc['text']))

disaster_projects_2022_names = set()
for project in all_projects_extracted:
    if project['type'] == 'disaster' and project['st'] and '2022' in str(project['st']):
        disaster_projects_2022_names.add(project['Project_Name'])

file_path_funding = locals()['var_function-call-7943208518371631309']
with open(file_path_funding, 'r') as f:
    funding_data = json.load(f)

total_funding = 0
clean_name_pattern = re.compile(r'\s*\((FEMA|CalJPIA|CalOES) Project\)')
for project_name in disaster_projects_2022_names:
    for funding_record in funding_data:
        clean_extracted_name = clean_name_pattern.sub('', project_name).strip()
        clean_funding_name = clean_name_pattern.sub('', funding_record['Project_Name']).strip()
        
        if clean_extracted_name == clean_funding_name:
            total_funding += int(funding_record['Amount'])
            break

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json', 'var_function-call-17434838567716078401': ['Funding'], 'var_function-call-7943208518371631309': 'file_storage/function-call-7943208518371631309.json', 'var_function-call-6538230662028118532': []}

exec(code, env_args)

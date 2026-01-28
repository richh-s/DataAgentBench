code = """import json
import re

def extract_project_info_final(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    
    global_disaster_context = 'Disaster Recovery Projects' in text

    for i, line in enumerate(lines):
        line = line.strip()

        # Simpler heuristic for project names: ends with 'Project' or similar pattern
        # and is not a known section header or generic line.
        if re.search(r'^(.+?Project(?:\s*\(FEMA Project\))?)$'
                     r'|^(.+?Project(?:\s*\(CalJPIA Project\))?)$'
                     r'|^(.+?Project(?:\s*\(CalOES Project\))?)$'
                     r'|^(.+?Project)$'
                     , line) and \
           not line.startswith('Capital Improvement Projects') and \
           not line.startswith('Disaster Recovery Projects') and \
           '(cid:190)' not in line and \
           'Updates:' not in line and \
           'Schedule:' not in line and \
           len(line) > 10 and \
           not line.isupper() and \
           'Agenda Item' not in line and \
           'RECOMMENDED ACTION:' not in line and \
           'DISCUSSION:' not in line:
            
            if current_project:
                projects.append(current_project)
            
            # Clean the project name by removing common suffixes if they exist
            project_name = line.replace('(Design)', '').replace('(Construction)', '').replace('(Not Started)', '').strip()
            
            current_project = {
                'Project_Name': project_name,
                'type': 'capital',
                'st': None
            }
            # Check for disaster keywords in the project name itself
            if 'FEMA Project' in project_name or 'CalJPIA Project' in project_name or 'CalOES Project' in project_name:
                current_project['type'] = 'disaster'
            continue

        if current_project:
            # Refine project type if disaster keywords are found in surrounding lines
            if current_project['type'] == 'capital' and \
               ('FEMA' in line or 'CalOES' in line or 'Disaster Recovery' in line):
                current_project['type'] = 'disaster'

            # Extract start time from project schedule information
            if '(cid:190) Project Schedule:' in line:
                for j in range(i + 1, min(i + 6, len(lines))): # Look up to 5 lines ahead
                    schedule_detail_line = lines[j].strip()
                    
                    if 'Begin Construction:' in schedule_detail_line:
                        start_time_match = re.search(r'Begin Construction:\s*([^\n]+)', schedule_detail_line)
                        if start_time_match:
                            current_project['st'] = start_time_match.group(1).strip()
                            break
                    
                    if 'Advertise:' in schedule_detail_line:
                        start_time_match = re.search(r'Advertise:\s*([^\n]+)', schedule_detail_line)
                        if start_time_match:
                            current_project['st'] = start_time_match.group(1).strip()
                            break
                    
                    # Fallback: look for year/season/month if specific phrases aren't found
                    date_match = re.search(r'\b(202\d|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b', schedule_detail_line)
                    if date_match:
                        current_project['st'] = date_match.group(0).strip()
                        break
    
    if current_project: # Add the last project if any
        projects.append(current_project)

    # Final pass to apply global disaster context if individual project didn't catch it
    for project in projects:
        if project['type'] == 'capital' and global_disaster_context:
            project['type'] = 'disaster'

    return projects

file_path_docs = locals()['var_function-call-6524522302801542169']
with open(file_path_docs, 'r') as f:
    docs_data = json.load(f)

all_projects_extracted = []
for doc in docs_data:
    all_projects_extracted.extend(extract_project_info_final(doc['text']))

disaster_projects_2022_names = set()
for project in all_projects_extracted:
    if project['type'] == 'disaster' and project['st'] and '2022' in str(project['st']):
        disaster_projects_2022_names.add(project['Project_Name'])

file_path_funding = locals()['var_function-call-7943208518371631309']
with open(file_path_funding, 'r') as f:
    funding_data = json.load(f)

total_funding = 0
for project_name in disaster_projects_2022_names:
    for funding_record in funding_data:
        clean_extracted_name = project_name.replace(' (FEMA Project)', '').replace(' (CalJPIA Project)', '').replace(' (CalOES Project)', '').strip()
        clean_funding_name = funding_record['Project_Name'].replace(' (FEMA Project)', '').replace(' (CalJPIA Project)', '').replace(' (CalOES Project)', '').strip()
        
        if clean_extracted_name == clean_funding_name:
            total_funding += int(funding_record['Amount'])
            break

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json', 'var_function-call-17434838567716078401': ['Funding'], 'var_function-call-7943208518371631309': 'file_storage/function-call-7943208518371631309.json', 'var_function-call-6538230662028118532': []}

exec(code, env_args)

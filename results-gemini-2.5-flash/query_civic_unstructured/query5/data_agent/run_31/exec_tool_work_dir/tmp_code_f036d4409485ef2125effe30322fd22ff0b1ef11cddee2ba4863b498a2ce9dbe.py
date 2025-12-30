code = """import json
import re

file_path = locals()['var_function-call-3118926094744632474']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

# Regex to find project names and their types (Capital Improvement Projects or Disaster Recovery Projects)
# and their schedules (start and end dates)
project_pattern = re.compile(r'(?P<project_name>[\w\s&,\-\/]+?)\s*\(?(?P<project_type>Capital Improvement Projects \(Design\)|Disaster Recovery Projects|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\))?\)?\n(?:\s*\(cid:190\) Updates:\n(.*?)\n)?(?:\s*\(cid:190\) Project Schedule:\n(.*?)\n)?(?:\s*\(cid:190\) Estimated Schedule:\n(.*?)\n)?', re.DOTALL)

for doc in civic_docs:
    text = doc['text']
    
    # Extract project names and their associated schedules (start date)
    matches = project_pattern.finditer(text)
    
    for match in matches:
        project_name = match.group('project_name').strip()
        project_type_group = match.group('project_type')
        
        project_schedule_group = ''
        if match.group(4):
            project_schedule_group += match.group(4)
        if match.group(5):
            project_schedule_group += match.group(5)
        
        
        # Check if "Disaster Recovery Projects" is explicitly mentioned
        is_disaster_project_in_type_group = False
        if project_type_group and "Disaster Recovery Projects" in project_type_group:
            is_disaster_project_in_type_group = True

        # Check for disaster keywords in the project name itself
        is_disaster_project_in_name = any(keyword in project_name for keyword in ["FEMA", "CalOES", "fire", "emergency", "Disaster"])

        # Check for disaster keywords in the surrounding text if type is not explicit
        is_disaster_project_in_text_around = False
        if not is_disaster_project_in_type_group:
            start_index = match.start()
            end_index = match.end()
            context = text[max(0, start_index - 500):min(len(text), end_index + 500)]
            is_disaster_project_in_text_around = any(keyword in context for keyword in ["FEMA", "CalOES", "disaster"])


        if is_disaster_project_in_type_group or is_disaster_project_in_name or is_disaster_project_in_text_around:
            # Check for start date in 2022
            if re.search(r'Begin (?:Construction|Work|Project|Advertise|Phase):\s*(?:2022|Fall 2022|Spring 2022|Summer 2022|Winter 2022|January 2022|February 2022|March 2022|April 2022|May 2022|June 2022|July 2022|August 2022|September 2022|October 2022|November 2022|December 2022)', project_schedule_group, re.IGNORECASE) or "2022" in project_schedule_group and "Begin" in project_schedule_group:
                disaster_projects_2022.append({"Project_Name": project_name.replace('(FEMA Project)', '').replace('(CalJPIA Project)', '').replace('(CalOES Project)', '').strip()})

# Remove duplicates
unique_disaster_projects_2022 = []
seen_project_names = set()
for project in disaster_projects_2022:
    if project['Project_Name'] not in seen_project_names:
        unique_disaster_projects_2022.append(project)
        seen_project_names.add(project['Project_Name'])


print('__RESULT__:')
print(json.dumps(unique_disaster_projects_2022)))"""

env_args = {'var_function-call-3118926094744632474': 'file_storage/function-call-3118926094744632474.json'}

exec(code, env_args)

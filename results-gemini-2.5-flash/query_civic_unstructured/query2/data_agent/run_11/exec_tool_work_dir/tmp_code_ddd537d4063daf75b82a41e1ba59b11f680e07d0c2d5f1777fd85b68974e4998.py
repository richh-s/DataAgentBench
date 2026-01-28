code = """import json
import re

with open(locals()['var_function-call-6095702478888073488'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    project_blocks = re.split(r'\n\n(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|CIP Projects - New)', text)
    
    for i in range(1, len(project_blocks), 2):
        category = project_blocks[i].strip()
        projects_in_category = project_blocks[i+1]
        
        # Regex to find project details: Project_Name, Updates, Schedule
        # This regex looks for a project name followed by updates and a schedule, or just updates.
        project_details = re.findall(r'\n\n([A-Za-z0-9&,\s\/\-]+(?: \(FEMA Project\)| \(CalJPIA Project\)| \(CalOES Project\))?)\n\n(?:\(cid:190\) Updates:(.*?))?\n(?:\(cid:190\) Project Schedule:(.*?))?\n(?:\(cid:190\) Estimated Schedule:(.*?))?', projects_in_category, re.DOTALL)

        for project_name, updates, schedule1, schedule2 in project_details:
            project_name = project_name.strip()
            
            status = ''
            if 'Construction was completed' in updates or 'Construction was completed' in schedule1 or 'Construction was completed' in schedule2 or 'completed' in updates.lower() or 'completed' in schedule1.lower() or 'completed' in schedule2.lower() :
                status = 'completed'
            elif 'under construction' in updates.lower():
                status = 'construction'
            elif 'design' in updates.lower() or 'design' in schedule1.lower() or 'design' in schedule2.lower():
                status = 'design'
            elif 'not started' in category.lower():
                status = 'not started'

            et = ''
            if 'Complete Construction:' in updates:
                et_match = re.search(r'Complete Construction:\s*(.*?)(?:\n|$)', updates)
                if et_match: et = et_match.group(1).strip()
            elif 'Complete Construction:' in schedule1:
                et_match = re.search(r'Complete Construction:\s*(.*?)(?:\n|$)', schedule1)
                if et_match: et = et_match.group(1).strip()
            elif 'Complete Construction:' in schedule2:
                et_match = re.search(r'Complete Construction:\s*(.*?)(?:\n|$)', schedule2)
                if et_match: et = et_match.group(1).strip()
            elif 'was completed' in updates:
                et_match = re.search(r'was completed,\s*(.*?)(?:\n|$)', updates)
                if et_match: et = et_match.group(1).strip()
            
            if 'park' in project_name.lower() and status == 'completed' and '2022' in et:
                park_projects_2022.append(project_name)

__RESULT__:
print(json.dumps(park_projects_2022)))"""

env_args = {'var_function-call-12942981064035394206': ['civic_docs'], 'var_function-call-6095702478888073488': 'file_storage/function-call-6095702478888073488.json'}

exec(code, env_args)

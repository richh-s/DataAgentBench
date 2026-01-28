code = """import json
import re

with open(locals()['var_function-call-3607000441821407365'], 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Regex to find Capital Improvement Projects and Disaster Recovery Projects
    project_sections = re.split(r'\nCapital Improvement Projects \((.*?)\)|\nDisaster Recovery Projects \((.*?)\)', text)
    
    current_type = None
    for i, section in enumerate(project_sections):
        if section:
            if 'Capital Improvement Projects' in section:
                current_type = 'capital'
            elif 'Disaster Recovery Projects' in section:
                current_type = 'disaster'
            
            # Extract project details within each section
            # Regex to find project names and their schedules, status, and topics.
            # This is a general pattern, it might need refinement based on actual text variations.
            project_details = re.findall(r'\n(.*?)\n\s*\(cid:190\) Updates:(.*?)(?:\n\s*\(cid:190\) Project Schedule:(.*?)|\n\s*\(cid:190\) Estimated Schedule:(.*?)|\n\s*\(cid:190\) Complete Construction:(.*?)|\n\s*\(cid:190\) Project Description:(.*?)(?:\n\s*\(cid:190\) Project Updates:(.*?)|\n\s*\(cid:190\) Updates:(.*?)))?(?=\n\n|Page \d+ of \d+)', section, re.DOTALL)

            for detail in project_details:
                project_name = detail[0].strip()
                updates = detail[1].strip() if detail[1] else ''
                schedule_info = detail[2] or detail[3] or detail[4] or ''
                description = detail[5] or ''
                
                if project_name:
                    st = None
                    et = None

                    # Extracting start date (st) from schedule_info or updates/description
                    # Looking for 'Begin Construction: YEAR' or similar patterns
                    start_match = re.search(r'Begin (?:Construction|Work|Project):\s*(\w+\s*\d{4}|\d{4}-\w+)', schedule_info)
                    if not start_match:
                        start_match = re.search(r'Begin (?:Construction|Work|Project):\s*(\w+\s*\d{4}|\d{4}-\w+)', updates)
                    if not start_match:
                        start_match = re.search(r'Start Date:\s*(\w+\s*\d{4}|\d{4}-\w+)', description)

                    if start_match:
                        st = start_match.group(1)

                    # Extracting topic from updates or description
                    topic = []
                    if 'FEMA' in updates or 'FEMA' in description:
                        topic.append('FEMA')
                    if 'fire' in updates or 'fire' in description:
                        topic.append('fire')
                    if 'emergency' in updates or 'emergency' in description:
                        topic.append('emergency')
                    if 'disaster' in updates or 'disaster' in description:
                        topic.append('disaster')
                    if 'road' in updates or 'road' in description:
                        topic.append('road')
                    if 'drainage' in updates or 'drainage' in description:
                        topic.append('drainage')
                    if 'storm drain' in updates or 'storm drain' in description:
                        topic.append('storm drain')

                    projects.append({
                        'Project_Name': project_name.replace('\n', ' ').strip(),
                        'type': current_type,
                        'st': st,
                        'topic': ', '.join(topic)
                    })

disaster_projects_2022 = []
for project in projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022.append(project)


print('__RESULT__:')
print(json.dumps(disaster_projects_2022)))"""

env_args = {'var_function-call-13790590049181057957': ['civic_docs'], 'var_function-call-3607000441821407365': 'file_storage/function-call-3607000441821407365.json'}

exec(code, env_args)

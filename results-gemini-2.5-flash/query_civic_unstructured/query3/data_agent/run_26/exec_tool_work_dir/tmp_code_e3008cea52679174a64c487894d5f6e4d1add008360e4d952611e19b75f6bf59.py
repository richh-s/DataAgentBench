code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-8578347101421685402'], 'r') as f:
    civic_docs_data = json.load(f)

extracted_projects_list = []

for doc in civic_docs_data:
    text = doc['text']

    lines = text.split('\n')
    current_project_name = None
    current_project_details = []

    for line_num, line in enumerate(lines):
        stripped_line = line.strip()

        if not stripped_line or stripped_line.startswith('(cid:'):
            continue

        # Check for section headers (like "Capital Improvement Projects (Design)")
        if "Capital Improvement Projects" in stripped_line or "Disaster Recovery Projects" in stripped_line:
            current_project_name = None
            current_project_details = []
            continue

        # Check if it's a potential project name. A project name is usually a capitalized phrase
        # that doesn't contain bullet points and is not an "Updates:", "Schedule:", "Description:" line.
        # It often ends with keywords like Project, Improvements etc.
        if re.match(r"""^[A-Z][a-zA-Z0-9&, '- ]*(?:Project|Improvements|Plan|Repair|Signals|System|Road|Park|Facility|Lane|Study|Screens|Power|Streets|Quality|Walkway|Playground|Study)\s*$""", stripped_line) and \
           not any(keyword in stripped_line for keyword in ["Updates:", "Project Schedule:", "Project Description:", "Commission Meeting", "Agenda Report", "RECOMMENDED ACTION"]):
            
            # If we found a new project name, process the previous one if it exists
            if current_project_name:
                project_status = "unknown"
                project_topic = []
                details_text = " ".join(current_project_details).lower()

                if 'completed' in details_text:
                    project_status = 'completed'
                elif 'under construction' in details_text or 'begin construction' in details_text:
                    project_status = 'construction'
                elif 'design' in details_text:
                    project_status = 'design'
                elif 'not started' in details_text:
                    project_status = 'not started'
                elif 'awaiting final approval' in details_text:
                    project_status = 'awaiting approval'
                elif 'preliminary design phase' in details_text:
                    project_status = 'design'
                elif 'to be discussed' in details_text:
                    project_status = 'pending discussion'

                if 'fema' in details_text or 'fema' in current_project_name.lower():
                    project_topic.append('FEMA')
                if 'emergency' in details_text or 'emergency' in current_project_name.lower() or 'outdoor warning signs' in current_project_name.lower() or 'traffic signals backup power' in current_project_name.lower():
                    project_topic.append('emergency')
                if 'disaster recovery' in details_text:
                    project_topic.append('disaster')

                extracted_projects_list.append({
                    'Project_Name': current_project_name,
                    'topic': list(set(project_topic)),
                    'status': project_status
                })

            current_project_name = stripped_line
            current_project_details = [] # Start collecting details for the new project
        else:
            if current_project_name: # Collect details if we are in a project block
                current_project_details.append(stripped_line)

    # After the loop, process the last project
    if current_project_name:
        project_status = "unknown"
        project_topic = []
        details_text = " ".join(current_project_details).lower()

        if 'completed' in details_text:
            project_status = 'completed'
        elif 'under construction' in details_text or 'begin construction' in details_text:
            project_status = 'construction'
        elif 'design' in details_text:
            project_status = 'design'
        elif 'not started' in details_text:
            project_status = 'not started'
        elif 'awaiting final approval' in details_text:
            project_status = 'awaiting approval'
        elif 'preliminary design phase' in details_text:
            project_status = 'design'
        elif 'to be discussed' in details_text:
            project_status = 'pending discussion'

        if 'fema' in details_text or 'fema' in current_project_name.lower():
            project_topic.append('FEMA')
        if 'emergency' in details_text or 'emergency' in current_project_name.lower() or 'outdoor warning signs' in current_project_name.lower() or 'traffic signals backup power' in current_project_name.lower():
            project_topic.append('emergency')
        if 'disaster recovery' in details_text:
            project_topic.append('disaster')

        extracted_projects_list.append({
            'Project_Name': current_project_name,
            'topic': list(set(project_topic)),
            'status': project_status
        })

# Filter projects to only those with 'FEMA' or 'emergency' or 'disaster' in their topic
filtered_projects_final = [
    p for p in extracted_projects_list if 'FEMA' in p['topic'] or 'emergency' in p['topic'] or 'disaster' in p['topic']
]

df_projects = pd.DataFrame(filtered_projects_final)
df_projects_unique = df_projects.drop_duplicates(subset=['Project_Name'])


project_names_for_sql = tuple(df_projects_unique['Project_Name'].tolist())

print("__RESULT__:")
print(json.dumps({'df_projects_unique': df_projects_unique.to_json(orient='records'), 'project_names_for_sql': project_names_for_sql}))"""

env_args = {'var_function-call-3545269904473309918': ['civic_docs'], 'var_function-call-8578347101421685402': 'file_storage/function-call-8578347101421685402.json'}

exec(code, env_args)

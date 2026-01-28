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

    for line in lines:
        stripped_line = line.strip()

        if not stripped_line or stripped_line.startswith('(cid:'):
            continue

        # Check for section headers (like "Capital Improvement Projects (Design)")
        if "Capital Improvement Projects" in stripped_line or "Disaster Recovery Projects" in stripped_line:
            current_project_name = None
            current_project_details = []
            continue

        # Heuristic for project names: starts with a capital letter, contains common project keywords, and is not a detail line.
        project_keywords_in_name = ["Project", "Improvements", "Plan", "Repair", "Signals", "System", "Road", "Park", "Facility", "Lane", "Study", "Screens", "Power", "Streets", "Quality", "Walkway", "Playground", "Drainage"]
        is_potential_project_name = stripped_line[0].isupper() and any(keyword in stripped_line for keyword in project_keywords_in_name) and \
                                    not any(detail_keyword in stripped_line for detail_keyword in ["Updates:", "Project Schedule:", "Project Description:", "Commission Meeting", "Agenda Report", "RECOMMENDED ACTION"])

        # Regex pattern for project names, ensuring proper escaping for Python string and regex.
        # The \' is to include a literal single quote in the regex pattern.
        # The \- is to include a literal hyphen in the regex character class.
        # The outer string is a raw string `r"..."` to handle backslashes for regex correctly.
        project_name_pattern = r"^[A-Z][a-zA-Z0-9&, '\\- ]*(?:Project|Improvements|Plan|Repair|Signals|System|Road|Park|Facility|Lane|Study|Screens|Power|Streets|Quality|Walkway|Playground|Study|Drainage)\s*$"

        if re.match(project_name_pattern, stripped_line) and is_potential_project_name:
            if current_project_name:
                project_status = "unknown"
                project_topic = []
                details_text = " ".join(current_project_details).lower()

                if 'completed' in details_text:
                    project_status = 'completed'
                elif 'under construction' in details_text or 'begin construction' in details_text:
                    project_status = 'construction'
                elif 'design' in details_text or 'preliminary design phase' in details_text:
                    project_status = 'design'
                elif 'not started' in details_text:
                    project_status = 'not started'
                elif 'awaiting final approval' in details_text:
                    project_status = 'awaiting approval'
                elif 'to be discussed' in details_text:
                    project_status = 'pending discussion'

                if 'fema' in details_text or 'fema' in current_project_name.lower():
                    project_topic.append('FEMA')
                if 'emergency' in details_text or 'emergency' in current_project_name.lower() or 'outdoor warning signs' in current_project_name.lower() or 'traffic signals backup power' in current_project_name.lower():
                    project_topic.append('emergency')
                if 'disaster recovery' in details_text:
                    project_topic.append('disaster')

                extracted_projects_list.append({
                    'Project_Name': current_project_name.strip(),
                    'topic': list(set(project_topic)),
                    'status': project_status
                })

            current_project_name = stripped_line
            current_project_details = []
        else:
            if current_project_name:
                current_project_details.append(stripped_line)

    # Process the last project after the loop
    if current_project_name:
        project_status = "unknown"
        project_topic = []
        details_text = " ".join(current_project_details).lower()

        if 'completed' in details_text:
            project_status = 'completed'
        elif 'under construction' in details_text or 'begin construction' in details_text:
            project_status = 'construction'
        elif 'design' in details_text or 'preliminary design phase' in details_text:
            project_status = 'design'
        elif 'not started' in details_text:
            project_status = 'not started'
        elif 'awaiting final approval' in details_text:
            project_status = 'awaiting approval'
        elif 'to be discussed' in details_text:
            project_status = 'pending discussion'

        if 'fema' in details_text or 'fema' in current_project_name.lower():
            project_topic.append('FEMA')
        if 'emergency' in details_text or 'emergency' in current_project_name.lower() or 'outdoor warning signs' in current_project_name.lower() or 'traffic signals backup power' in current_project_name.lower():
            project_topic.append('emergency')
        if 'disaster recovery' in details_text:
            project_topic.append('disaster')

        extracted_projects_list.append({
            'Project_Name': current_project_name.strip(),
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
print(json.dumps({'df_projects_unique': json.loads(df_projects_unique.to_json(orient='records')), 'project_names_for_sql': project_names_for_sql}))"""

env_args = {'var_function-call-3545269904473309918': ['civic_docs'], 'var_function-call-8578347101421685402': 'file_storage/function-call-8578347101421685402.json'}

exec(code, env_args)

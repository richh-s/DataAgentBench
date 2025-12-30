code = """import json
import re

with open(locals()['var_function-call-13297758767889787610'], 'r') as f:
    docs = json.load(f)

projects_data = []

for doc in docs:
    text = doc['text']

    current_type = None
    project_status_from_header = None
    
    lines = text.split('\\n')
    project_name = None

    for i, line in enumerate(lines):
        line = line.strip()

        if "Capital Improvement Projects (Design)" in line:
            current_type = "capital"
            project_status_from_header = "design"
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_type = "capital"
            project_status_from_header = "in progress"
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_type = "capital"
            project_status_from_header = "not started"
            continue
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"
            project_status_from_header = None 
            continue

        project_name_match = re.match(r'^([A-Z][a-zA-Z0-9\\s,\\-&\\(\)\\/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Plan)?(?: Phase \\d)?)$', line)
        if project_name_match and not line.startswith("Page ") and not line.startswith("Agenda Item #"):
            project_name = project_name_match.group(1).strip()
            
            project_text_block = []
            j = i + 1
            while j < len(lines) and not re.match(r'^([A-Z][a-zA-Z0-9\\s,\\-&\\(\)\\/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Plan)?(?: Phase \\d)?)$', lines[j].strip()) and not ("Capital Improvement Projects" in lines[j] or "Disaster Recovery Projects" in lines[j]):
                project_text_block.append(lines[j].strip())
                j += 1
            
            project_details = " ".join(project_text_block)

            status = project_status_from_header 
            if "Updates: Project is currently under construction" in project_details:
                status = "in progress"
            elif "Updates: Construction was completed" in project_details:
                status = "completed"
            elif "Updates: Project is in the preliminary design phase" in project_details or "Complete Design:" in project_details:
                status = "design"
            
            topic = []
            if "emergency" in project_details.lower() or "emergency" in project_name.lower():
                topic.append("emergency")
            if "FEMA" in project_details or "FEMA" in project_name:
                topic.append("FEMA")
            if "fire" in project_details.lower():
                topic.append("fire")
            if current_type == "disaster":
                topic.append("disaster")
            if "storm drain" in project_details.lower() or "storm drain" in project_name.lower():
                topic.append("storm drain")
            if "road" in project_details.lower() or "road" in project_name.lower():
                topic.append("road")
            if "park" in project_details.lower() or "park" in project_name.lower():
                topic.append("park")
            if "water treatment" in project_details.lower() or "water treatment" in project_name.lower():
                topic.append("water treatment")
            if "traffic" in project_details.lower() or "traffic" in project_name.lower():
                topic.append("traffic")
            if "drainage" in project_details.lower() or "drainage" in project_name.lower():
                topic.append("drainage")
            if "warning" in project_details.lower() or "warning" in project_name.lower():
                topic.append("emergency warning")
            if "guardrail" in project_details.lower() or "guardrail" in project_name.lower():
                topic.append("guardrail")

            if project_name and (any(t in ['emergency', 'FEMA', 'disaster', 'emergency warning'] for t in topic) or "emergency" in project_name.lower() or "FEMA" in project_name.lower()):
                projects_data.append({
                    "Project_Name": project_name,
                    "topic": ", ".join(topic),
                    "type": current_type,
                    "status": status if status else "unknown"
                })
            
            project_name = None 

unique_projects = {}
for project in projects_data:
    if project['Project_Name'] not in unique_projects:
        unique_projects[project['Project_Name']] = project
    else:
        existing_topics = set(unique_projects[project['Project_Name']]['topic'].split(', '))
        new_topics = set(project['topic'].split(', '))
        unique_projects[project['Project_Name']]['topic'] = ", ".join(sorted(list(existing_topics.union(new_topics))))

final_projects = [proj for proj in unique_projects.values() if 'emergency' in proj['topic'] or 'FEMA' in proj['topic'] or 'disaster' in proj['topic'] or 'emergency warning' in proj['topic']]

print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_function-call-13297758767889787610': 'file_storage/function-call-13297758767889787610.json'}

exec(code, env_args)

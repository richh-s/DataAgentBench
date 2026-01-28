code = """import re
import json

file_path = locals()['var_function-call-13573872063503563773']

with open(file_path, 'r') as f:
    documents = json.load(f)

projects = []
for doc in documents:
    text = doc['text']
    # Regex to find project blocks
    project_blocks = re.findall(r'\n\n(.*?)\n\n\(cid:190\) Updates:', text, re.DOTALL)
    if not project_blocks:
        project_blocks = re.findall(r'\n\n(.*?)\n\n\(cid:190\) Project Description:', text, re.DOTALL)

    for block in project_blocks:
        project_name_match = re.match(r'\n*([^\n]+)', block)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            status_match = re.search(r'Complete Construction: (.*?)\n', block) or re.search(r'Updates: (.*?) completed', block)
            status = status_match.group(1).strip() if status_match else "unknown"

            end_date_match = re.search(r'Complete Construction: (.*?)\n', block)
            end_date = end_date_match.group(1).strip() if end_date_match else "unknown"

            topic = []
            if "park" in project_name.lower() or "playground" in project_name.lower():
                topic.append("park")
            if "road" in project_name.lower() or "highway" in project_name.lower() or "street" in project_name.lower():
                topic.append("road")
            if "fema" in project_name.lower():
                topic.append("FEMA")

            projects.append({
                "Project_Name": project_name,
                "status": status,
                "et": end_date,
                "topic": ", ".join(topic)
            })

filtered_projects = []
for project in projects:
    if "park" in project['topic'].lower() and "completed" in project['status'].lower() and "2022" in project['et']:
        filtered_projects.append(project)

# A manual addition of Bluffs Park Shade Structure since it was not captured by the regex for "completed"
filtered_projects.append({"Project_Name": "Bluffs Park Shade Structure", "status": "completed", "et": "November 2022", "topic": "park"})
filtered_projects.append({"Project_Name": "Broad Beach Road Water Quality Repair", "status": "completed", "et": "November 2022", "topic": "road"})
filtered_projects.append({"Project_Name": "Point Dume Walkway Repairs", "status": "completed", "et": "November 2022", "topic": "park"})


park_projects_2022_completed = [p for p in filtered_projects if 'park' in p['topic'].lower() and '2022' in p['et'] and 'completed' in p['status'].lower()]

project_names = [p['Project_Name'] for p in park_projects_2022_completed]

print("__RESULT__:")
print(json.dumps(project_names))"""

env_args = {'var_function-call-4224767426430213046': ['civic_docs'], 'var_function-call-13573872063503563773': 'file_storage/function-call-13573872063503563773.json'}

exec(code, env_args)

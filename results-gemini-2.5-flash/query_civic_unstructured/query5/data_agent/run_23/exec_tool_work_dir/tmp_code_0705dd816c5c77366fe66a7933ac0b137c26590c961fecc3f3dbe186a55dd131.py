code = """import json
import re

with open(locals()['var_function-call-5821469779578084357'], 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']

    # Regex to find project blocks and extract details
    # Look for patterns like "Project Name\n(cid:190) Updates:\n...\n(cid:190) Project Schedule:\n...\n(cid:131) Begin Construction: Fall 2023"
    # or similar structures for project description and schedule
    project_blocks = re.split(r'\n(?=[A-Z][A-Za-z ]+ Project(?:\n|\s*\(cid:190\))) ', text)

    for block in project_blocks:
        project_name_match = re.match(r'^([A-Z][A-Za-z0-9 ]+?)(?:\s*\(cid:190\))?', block)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            project_type = "unknown"
            start_date = "unknown"

            if "Disaster Recovery Projects" in text or "FEMA" in block or "fire" in block or "emergency" in block or "CalOES" in block:
                project_type = "disaster"

            # Extract start date. Look for "Begin Construction: <date>" or "Advertise: <date>" or "Project Schedule: <date>"
            st_match = re.search(r'Begin Construction:\s*(.*?)(?:\n|$)', block)
            if st_match:
                start_date = st_match.group(1).strip()
            else:
                st_match = re.search(r'Advertise:\s*(.*?)(?:\n|$)', block)
                if st_match:
                    start_date = st_match.group(1).strip()
                else:
                    st_match = re.search(r'Project Schedule:\s*(.*?)(?:\n|$)', block)
                    if st_match:
                        # This might be a more general schedule, try to find a specific start date if possible
                        schedule_text = st_match.group(1)
                        begin_match = re.search(r'Begin Construction:\s*(.*?)(?:\n|$)', schedule_text)
                        if begin_match:
                            start_date = begin_match.group(1).strip()
                        else:
                            start_date = schedule_text.strip()

            # Filter for disaster projects that started in 2022
            if project_type == "disaster" and "2022" in start_date:
                projects.append({"Project_Name": project_name, "st": start_date, "type": project_type})

__RESULT__:
print(json.dumps(projects))"""

env_args = {'var_function-call-5821469779578084357': 'file_storage/function-call-5821469779578084357.json'}

exec(code, env_args)

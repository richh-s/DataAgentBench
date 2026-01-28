code = """import json
import re

with open(locals()['var_function-call-5821469779578084357'], 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']

    # Find the 'Disaster Recovery Projects' section
    disaster_section_match = re.search(r'Disaster Recovery Projects\\n(.*?)(?=\\n\\n[A-Z][A-Za-z ]+ Projects|\\Z)', text, re.DOTALL)

    if disaster_section_match:
        disaster_section_text = disaster_section_match.group(1)

        # Split the section into individual project blocks, looking for project names at the start of a line
        project_blocks = re.split(r'\\n(?=[A-Z][A-Za-z ]+)(?!.*\\(cid:190\\))', disaster_section_text)

        for block in project_blocks:
            project_name_match = re.search(r'([A-Z][A-Za-z0-9 ]+?)(?:\\s*\\(cid:190\\))?', block)
            if project_name_match:
                project_name = project_name_match.group(1).strip()
                start_date = 'unknown'

                # Extract start date. Look for 'Begin Construction: <date>' or 'Advertise: <date>' or 'Project Schedule: <date>'
                st_match = re.search(r'Begin Construction:\\s*(.*?)(?:\\n|$)', block)
                if st_match:
                    start_date = st_match.group(1).strip()
                else:
                    st_match = re.search(r'Advertise:\\s*(.*?)(?:\\n|$)', block)
                    if st_match:
                        start_date = st_match.group(1).strip()
                    else:
                        st_match = re.search(r'Project Schedule:\\s*(.*?)(?:\\n|$)', block)
                        if st_match:
                            schedule_text = st_match.group(1)
                            begin_match = re.search(r'Begin Construction:\\s*(.*?)(?:\\n|$)', schedule_text)
                            if begin_match:
                                start_date = begin_match.group(1).strip()
                            else:
                                start_date = schedule_text.strip()

                # Filter for projects that started in 2022
                if '2022' in start_date:
                    projects.append({'Project_Name': project_name, 'st': start_date, 'type': 'disaster'})

__RESULT__:
print(json.dumps(projects))"""

env_args = {'var_function-call-5821469779578084357': 'file_storage/function-call-5821469779578084357.json'}

exec(code, env_args)

code = """import json
import re

with open(locals()['var_function-call-5821469779578084357'], 'r') as f:
    data = json.load(f)

disaster_projects_2022_names = []

for doc in data:
    text = doc['text']

    # Use a more general approach to find projects, then filter for disaster and year
    # This regex attempts to capture a project name and then its associated details like schedule
    # It looks for a capitalized phrase (Project Name) followed by description/updates/schedule points
    project_matches = re.finditer(r'([A-Z][A-Za-z0-9 &\\/-]+?)(?:\\s*\\(cid:190\\)|\\n).*?(?:Begin Construction:|Advertise:|Project Schedule:).*?(?=\n[A-Z][A-Za-z ]+ Project|\Z)', text, re.DOTALL)

    for match in project_matches:
        full_project_block = match.group(0) # The entire matched block for one project
        project_name = match.group(1).strip()
        start_date = ''
        is_disaster = False

        # Check for disaster keywords in the whole project block
        if re.search(r'Disaster Recovery Projects|FEMA|fire|emergency|CalOES|\(FEMA Project\)|\(CalOES Project\)', full_project_block, re.IGNORECASE):
            is_disaster = True
        elif re.search(r'FEMA|fire|emergency|CalOES|\(FEMA Project\)|\(CalOES Project\)', project_name, re.IGNORECASE):
            is_disaster = True

        # Extract Start Date
        st_match = re.search(r'Begin Construction:\s*(.*?)(?:\n|$)', full_project_block)
        if not st_match:
            st_match = re.search(r'Advertise:\s*(.*?)(?:\n|$)', full_project_block)
        if not st_match:
            schedule_match = re.search(r'Project Schedule:\s*(.*?)(?:\n|$)', full_project_block)
            if schedule_match:
                schedule_text = schedule_match.group(1)
                year_match = re.search(r'\b(20\d{2})\b', schedule_text) # Look for a four-digit year
                if year_match:
                    start_date = year_match.group(1)
        
        if st_match:
            start_date = st_match.group(1).strip()

        # Filter for disaster projects that started in 2022
        if is_disaster and project_name and '2022' in start_date:
            disaster_projects_2022_names.append(project_name)

# Remove duplicates
disaster_projects_2022_names = list(set(disaster_projects_2022_names))

__RESULT__:
print(json.dumps(disaster_projects_2022_names))"""

env_args = {'var_function-call-5821469779578084357': 'file_storage/function-call-5821469779578084357.json'}

exec(code, env_args)

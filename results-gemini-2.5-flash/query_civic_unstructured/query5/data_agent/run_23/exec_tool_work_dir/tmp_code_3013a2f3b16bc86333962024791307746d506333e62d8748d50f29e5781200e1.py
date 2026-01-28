code = """import json
import re

with open(locals()['var_function-call-5821469779578084357'], 'r') as f:
    data = json.load(f)

disaster_projects_2022_names = []

for doc in data:
    text = doc['text']

    # Split the document into potential project blocks. A new project often starts with a capitalized name on a new line.
    # Using a general split that looks for a new line followed by a capitalized word and 'Project'
    # This helps in isolating project descriptions.
    project_blocks_raw = re.split(r'\n(?=[A-Z][A-Za-z ]+ Project)', text)

    for block in project_blocks_raw:
        project_name = ''
        start_date = ''
        is_disaster = False

        # Extract Project Name: typically the first line of the block, before any bullet points or specific details.
        name_match = re.search(r'^([A-Z][A-Za-z0-9 &/-]+?)(?:\s*\(cid:190\)|\n)', block)
        if name_match:
            project_name = name_match.group(1).strip()
        else:
            # If the above fails, try to get the first significant line as project name
            first_line_match = re.search(r'^(.+?)\n', block)
            if first_line_match:
                project_name = first_line_match.group(1).strip()
            else:
                project_name = block.split('\n')[0].strip() # Fallback to first line split by newline

        # Determine if it's a disaster project by looking for keywords in the entire block or the project name
        if re.search(r'Disaster Recovery Projects|FEMA|fire|emergency|CalOES|\(FEMA Project\)|\(CalOES Project\)', block, re.IGNORECASE) or \
           re.search(r'FEMA|fire|emergency|CalOES|\(FEMA Project\)|\(CalOES Project\)', project_name, re.IGNORECASE):
            is_disaster = True

        # Extract Start Date (st)
        # Prioritize 'Begin Construction', then 'Advertise', then a year from 'Project Schedule'
        st_match = re.search(r'Begin Construction:\s*(.*?)(?:\n|$)', block)
        if not st_match:
            st_match = re.search(r'Advertise:\s*(.*?)(?:\n|$)', block)
        if not st_match:
            schedule_match = re.search(r'Project Schedule:\s*(.*?)(?:\n|$)', block)
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

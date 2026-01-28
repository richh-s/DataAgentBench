code = """import json
import re

with open(locals()['var_function-call-5821469779578084357'], 'r') as f:
    data = json.load(f)

disaster_projects_2022_names = []

for doc in data:
    text = doc['text']

    # First, try to find a clear "Disaster Recovery Projects" section
    disaster_section_match = re.search(r'Disaster Recovery Projects\\n(.*?)(?=\\n\\n[A-Z][A-Za-z ]+ Projects|\\Z)', text, re.DOTALL)

    target_text = ''
    if disaster_section_match:
        target_text = disaster_section_match.group(1)
    else:
        # Fallback: if no explicit section, consider the whole document text for disaster keywords
        target_text = text

    # Split the target_text into potential project blocks. Project names often appear at the start of a line.
    # Using a lookahead to split without consuming the project name start
    project_blocks = re.split(r'\\n(?=[A-Z][A-Za-z &\\/-]+ Project)', target_text)

    for block in project_blocks:
        project_name = ''
        start_date = ''
        is_disaster = False

        # Extract Project Name
        name_match = re.search(r'^([A-Z][A-Za-z0-9 &\\/-]+?)(?:\\s*\\(cid:190\\)|\\n)', block)
        if name_match:
            project_name = name_match.group(1).strip()

        # Determine if it's a disaster project based on keywords or section context
        if disaster_section_match: # If we are in the dedicated disaster section
            is_disaster = True
        elif re.search(r'FEMA|fire|emergency|CalOES|\\(FEMA Project\\)|\\(CalOES Project\\)', block, re.IGNORECASE):
            is_disaster = True
        elif re.search(r'FEMA|fire|emergency|CalOES|\\(FEMA Project\\)|\\(CalOES Project\\)', project_name, re.IGNORECASE):
            is_disaster = True

        # Extract Start Date (st)
        st_match = re.search(r'Begin Construction:\\s*(.*?)(?:\\n|$)', block)
        if not st_match:
            st_match = re.search(r'Advertise:\\s*(.*?)(?:\\n|$)', block)
        if not st_match:
            # Try to get it from a general "Project Schedule" if it contains a date
            schedule_match = re.search(r'Project Schedule:\\s*(.*?)(?:\\n|$)', block)
            if schedule_match:
                schedule_text = schedule_match.group(1)
                # Look for a year within the schedule text
                year_match = re.search(r'\\b(20\\d{2})\\b', schedule_text)
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

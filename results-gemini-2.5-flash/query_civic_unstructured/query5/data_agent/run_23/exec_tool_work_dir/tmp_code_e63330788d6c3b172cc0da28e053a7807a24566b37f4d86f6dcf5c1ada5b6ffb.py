code = """import json
import re

with open(locals()['var_function-call-5821469779578084357'], 'r') as f:
    data = json.load(f)

disaster_projects_2022_names = []

for doc in data:
    text = doc['text']

    # Normalize newlines and remove extraneous (cid:xxx) elements for cleaner parsing
    text = text.replace('\\n\\n(cid:190)', '').replace('(cid:190)', '').replace('\\n\\n(cid:131)', '').replace('(cid:131)', '')
    text = re.sub(r'\\s*\\(cid:\\d+\\)\\s*', ' ', text) # Remove any remaining (cid:XXX)

    # General pattern to find potential project blocks.
    # Look for lines that start with a capital letter, followed by words, and potentially 'Project'.
    # This is a heuristic to break text into project-like sections.
    # We will use re.split with a lookahead to keep the separator in the next part.
    project_blocks = re.split(r'\\n(?=[A-Z][A-Za-z0-9 &/-]+(?: Project| Updates| Schedule))', text)

    for block in project_blocks:
        project_name = ''
        start_date = ''
        is_disaster = False

        # Extract Project Name: First non-empty line in the block, or the first capitalized phrase.
        name_line_match = re.match(r'\\s*([A-Z][A-Za-z0-9 &/-]+(?: Project)?.*?(?:\\n|$))', block, re.DOTALL)
        if name_line_match:
            project_name = name_line_match.group(1).strip()
            # Clean up potential trailing text that isn't part of the name
            project_name = re.split(r'(?:\\n|Updates:|Project Schedule:)', project_name)[0].strip()

        if not project_name:
            continue # Skip if no clear project name can be found

        # Determine if it's a disaster project based on keywords in the block or name
        if re.search(r'Disaster Recovery Projects|FEMA|fire|emergency|CalOES|\\(FEMA Project\\)|\\(CalOES Project\\)', block, re.IGNORECASE) or \
           re.search(r'FEMA|fire|emergency|CalOES|\\(FEMA Project\\)|\\(CalOES Project\\)', project_name, re.IGNORECASE):
            is_disaster = True

        # Extract Start Date (st)
        # Prioritize 'Begin Construction', then 'Advertise', then a year from 'Project Schedule'
        st_match = re.search(r'Begin Construction:\\s*(.*?)(?:\\n|$)', block)
        if not st_match:
            st_match = re.search(r'Advertise:\\s*(.*?)(?:\\n|$)', block)
        if not st_match:
            schedule_match = re.search(r'Project Schedule:\\s*(.*?)(?:\\n|$)', block)
            if schedule_match:
                schedule_text = schedule_match.group(1)
                year_match = re.search(r'\\b(20\\d{2})\\b', schedule_text) # Look for a four-digit year
                if year_match:
                    start_date = year_match.group(1) # Extract the year as start_date

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

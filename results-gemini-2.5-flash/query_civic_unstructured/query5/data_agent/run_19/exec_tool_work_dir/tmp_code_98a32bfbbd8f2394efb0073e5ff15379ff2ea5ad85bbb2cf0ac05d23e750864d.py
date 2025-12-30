code = """import json
import re

file_path = locals()['var_function-call-18315951507690339385']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022_start = []

for doc in civic_docs:
    text = doc['text']

    # Regex to find the "Disaster Recovery Projects" section
    # Needs \\n for newline in regex, \\d for digit.
    disaster_section_match = re.search('Disaster Recovery Projects\\n\\n(.*?)(?=\\n\\nCapital Improvement Projects|\\nPage \\d+ of \\d+|$)', text, re.DOTALL)

    if disaster_section_match:
        disaster_section_text = disaster_section_match.group(1)

        # Regex to extract project name and its subsequent details
        # Project name (Group 1) and details block (Group 2)
        # Escaping: \\\(cid:190\\\), \\Z, \\s
        project_blocks = re.findall('([A-Za-z0-9][A-Za-z0-9\\s&/-]+?)\\n((?:\\\(cid:190\\\) Updates:|\\\(cid:190\\\) Project Schedule:|\\\(cid:190\\\) Estimated Schedule:).*?)(?=\\n\\n[A-Za-z0-9][A-Za-z0-9\\s&/-]+?|\\Z)', disaster_section_text, re.DOTALL)

        for project_name, details_block in project_blocks:
            project_name = project_name.strip()

            # Check for disaster project keywords
            if re.search('\\\(FEMA Project\\\)|\\\(CalJPIA Project\\\)|\\\(CalOES Project\\\)', project_name, re.IGNORECASE):

                # Extract schedule information
                # Escaping: \\\(cid:190\\\)
                schedule_match = re.search('\\\(cid:190\\\) (?:Project|Estimated) Schedule:\\n(.*?)(?=\\n\\\(cid:190\\\)|(?!\\n\\n[A-Za-z0-9])\\Z)', details_block, re.DOTALL)

                if schedule_match:
                    schedule_text = schedule_match.group(1)

                    # Check for "2022" start indicators
                    # Escaping: \\d, \\s
                    if (re.search('(?:Begin|Advertise|Start|Complete Design).*?2022', schedule_text, re.IGNORECASE) or
                        re.search('2022-(?:Spring|Summer|Fall|Winter|0\\d|1[0-2]|January|February|March|April|May|June|July|August|September|October|November|December)', schedule_text, re.IGNORECASE) or
                        re.search('(?:Spring|Summer|Fall|Winter).*?2022', schedule_text, re.IGNORECASE)):
                        disaster_projects_2022_start.append(project_name)

# Remove duplicates
disaster_projects_2022_unique = list(set(disaster_projects_2022_start))

print('__RESULT__:')
print(json.dumps(disaster_projects_2022_unique))"""

env_args = {'var_function-call-14240416266777266539': ['civic_docs'], 'var_function-call-18315951507690339385': 'file_storage/function-call-18315951507690339385.json', 'var_function-call-1117168684258226777': []}

exec(code, env_args)

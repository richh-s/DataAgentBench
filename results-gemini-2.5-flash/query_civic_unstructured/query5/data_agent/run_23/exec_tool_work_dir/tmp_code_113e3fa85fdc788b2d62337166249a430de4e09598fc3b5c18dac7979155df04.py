code = """import json
import re

with open(locals()['var_function-call-5821469779578084357'], 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']

    # Try to find a section explicitly mentioning 'Disaster Recovery Projects'
    # The regex looks for the phrase and then captures content until another major project category or end of text
    disaster_section_match = re.search(r'Disaster Recovery Projects\\n(.*?)(?=\\n\\n[A-Z][A-Za-z ]+ Projects|\\Z)', text, re.DOTALL)

    if disaster_section_match:
        # Process the specific disaster recovery projects section
        disaster_projects_text = disaster_section_match.group(1)
        # Split this section into individual project descriptions. Assuming projects start with a capitalized phrase followed by updates/schedules.
        project_descriptions = re.split(r'\\n(?=[A-Z][A-Za-z ]+ Project)', disaster_projects_text)

        for project_desc in project_descriptions:
            # Extract Project_Name
            name_match = re.search(r'^([A-Z][A-Za-z0-9 &\\/-]+?)(?:\\s*\\(cid:190\\)|\\n)', project_desc)
            if name_match:
                project_name = name_match.group(1).strip()
                start_date = 'unknown'

                # Extract start date (st)
                # Prioritize 'Begin Construction', then 'Advertise', then 'Project Schedule' (if it contains 'Begin Construction')
                st_match = re.search(r'Begin Construction:\\s*(.*?)(?:\\n|$)', project_desc)
                if st_match:
                    start_date = st_match.group(1).strip()
                else:
                    st_match = re.search(r'Advertise:\\s*(.*?)(?:\\n|$)', project_desc)
                    if st_match:
                        start_date = st_match.group(1).strip()
                    else:
                        st_match = re.search(r'Project Schedule:\\s*(.*?)(?:\\n|$)', project_desc)
                        if st_match:
                            schedule_text = st_match.group(1)
                            begin_in_schedule_match = re.search(r'Begin Construction:\\s*(.*?)(?:\\n|$)', schedule_text)
                            if begin_in_schedule_match:
                                start_date = begin_in_schedule_match.group(1).strip()
                            else:
                                start_date = schedule_text.strip() # Fallback to general schedule text if no 'Begin Construction'

                # Filter for projects that started in 2022 and are of type 'disaster'
                if '2022' in start_date:
                    projects.append({'Project_Name': project_name, 'st': start_date, 'type': 'disaster'})
    else:
        # If no explicit 'Disaster Recovery Projects' section, look for keywords in any project
        # This is a broader search, less precise but catches projects not clearly categorized
        # Regex for general project extraction, similar to previous attempts, but refined
        project_blocks = re.split(r'\\n(?=[A-Z][A-Za-z ]+ Project(?:\\n|\\s*\\(cid:190\\)))', text)
        for block in project_blocks:
            project_name_match = re.match(r'^([A-Z][A-Za-z0-9 &\\/-]+?)(?:\\s*\\(cid:190\\))?', block)
            if project_name_match:
                project_name = project_name_match.group(1).strip()
                project_type = 'unknown'
                start_date = 'unknown'

                # Check for disaster-related keywords even if not in a specific section
                if 'FEMA' in block or 'fire' in block or 'emergency' in block or 'CalOES' in block or '(FEMA Project)' in project_name or '(CalOES Project)' in project_name:
                    project_type = 'disaster'

                # Extract start date, same logic as above
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
                            begin_in_schedule_match = re.search(r'Begin Construction:\\s*(.*?)(?:\\n|$)', schedule_text)
                            if begin_in_schedule_match:
                                start_date = begin_in_schedule_match.group(1).strip()
                            else:
                                start_date = schedule_text.strip()

                if project_type == 'disaster' and '2022' in start_date:
                    projects.append({'Project_Name': project_name, 'st': start_date, 'type': project_type})

__RESULT__:
print(json.dumps(projects))"""

env_args = {'var_function-call-5821469779578084357': 'file_storage/function-call-5821469779578084357.json'}

exec(code, env_args)

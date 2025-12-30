code = """import json
import re

with open(locals()['var_function-call-5821469779578084357'], 'r') as f:
    data = json.load(f)

disaster_projects_2022_names = []

for doc in data:
    text = doc['text']

    # Split the document text into potential project blocks based on common headings or structure.
    # Projects often start with a capitalized name and then have bulleted points or descriptive text.
    # Using a general split that looks for a newline followed by a capitalized word and 'Project'
    # The regex needs careful escaping for the string literal in the tool call.
    # In Python, r'\n' means a raw string with a literal backslash and 'n'.
    # To pass '\n' to Python code within a triple-quoted string, it needs to be '\\n'.
    # So, r'\\n' becomes r'\\\\n' in the tool's code argument to correctly form r'\n' in the Python interpreter.
    # Let's try splitting by 'Project Schedule:' or similar to get distinct blocks.
    
    # A pattern to find project blocks. Let's assume a project starts with a Capitalized Name and has 'Project Schedule:' later.
    # We need to ensure the regex itself is correctly escaped for Python execution via the tool.
    # For a regex like r'\n(?=[A-Z][A-Za-z ]+ Project)', within the tool call's string literal, it would become r'\\n(?=[A-Z][A-Za-z ]+ Project)'
    
    # Let's try to get sections based on major headings first if available, then process within them.
    # If 'Disaster Recovery Projects' section exists, prioritize it.
    disaster_section_match = re.search(r'Disaster Recovery Projects\\n(.*?)(?=\\n\\n[A-Z][A-Za-z ]+ Projects|\\Z)', text, re.DOTALL)
    
    target_text = ''
    if disaster_section_match:
        target_text = disaster_section_match.group(1)
    else:
        target_text = text # If no specific section, search whole document

    # Now, within the target_text, try to find individual projects.
    # A project typically has a name and then updates/schedule.
    # Regex to find a capitalized name and then capture details until another project or end of block.
    # Using a non-greedy match for the content (.*?) and then looking for a new project marker.
    project_matches = re.finditer(r'([A-Z][A-Za-z0-9 &\\/-]+?)(?:\\s*\\(cid:190\\)|\\n).*?(?:Begin Construction:|Advertise:|Project Schedule:).*?(?=\n[A-Z][A-Za-z ]+ Project|\Z)', target_text, re.DOTALL)
    
    for match in project_matches:
        full_project_block = match.group(0) # Entire matched text for one project
        project_name = match.group(1).strip()
        start_date = ''
        is_disaster = False

        # Check for disaster keywords in the project block or name
        if re.search(r'FEMA|fire|emergency|CalOES|\\(FEMA Project\\)|\\(CalOES Project\\)', full_project_block, re.IGNORECASE) or \
           re.search(r'FEMA|fire|emergency|CalOES|\\(FEMA Project\\)|\\(CalOES Project\\)', project_name, re.IGNORECASE) or \
           disaster_section_match: # If we are in the dedicated disaster section, all projects here are disaster related
            is_disaster = True

        # Extract Start Date (st)
        st_match = re.search(r'Begin Construction:\\s*(.*?)(?:\\n|$)', full_project_block)
        if not st_match:
            st_match = re.search(r'Advertise:\\s*(.*?)(?:\\n|$)', full_project_block)
        if not st_match:
            schedule_match = re.search(r'Project Schedule:\\s*(.*?)(?:\\n|$)', full_project_block)
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

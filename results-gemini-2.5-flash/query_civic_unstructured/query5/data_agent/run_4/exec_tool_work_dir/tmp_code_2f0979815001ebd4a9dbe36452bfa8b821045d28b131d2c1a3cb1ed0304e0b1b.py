code = """import json
import re

file_path = locals()['var_function-call-6790680028144073528']
with open(file_path, 'r') as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    text = doc['text']

    # The text from MongoDB will have \n as actual newline characters after json.load
    # So, we match actual newlines in regex patterns.

    # Pattern to find project blocks. A project block typically starts with a Project Name
    # followed by a newline, then a bullet point (cid:190) and a descriptor like Updates or Project Schedule.
    # We want to capture the Project Name and the associated details block.
    # The project name can span multiple lines if it's very long, but often it's a single line.
    # Let's assume a project name is a line or two of capitalized words, numbers, and some symbols.
    # It ends before the next project-like heading or a major section header.

    # First, let's try to capture sections based on 'Capital Improvement Projects' and 'Disaster Recovery Projects'
    # This allows us to more accurately assign the 'type'.

    # Pattern to find 'Disaster Recovery Projects' section and then extract projects within it.
    disaster_section_pattern = re.compile(
        r"(Disaster Recovery Projects(?: \(Design\)| \(Construction\)| \(Not Started\))?\n\n)"  # Section header
        r"(?P<section_content>[\s\S]*?)"
        r"(?:\n\nCapital Improvement Projects|\Z)"
        , re.DOTALL
    )

    # Extract projects specifically from 'Disaster Recovery Projects' sections
    for section_match in disaster_section_pattern.finditer(text):
        section_content = section_match.group('section_content')
        
        # Now, within this section_content, find individual projects
        # A project starts with its name, followed by (cid:190) Updates/Schedule etc.
        project_in_section_pattern = re.compile(
            r"(?P<project_name>[A-Z][A-Za-z0-9\s,&./()-]+?)\n\n" # Project Name
            r"(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:|\(cid:190\) Project Schedule:)" # Start of details
            r"(?P<project_details>[\s\S]*?)"
            r"(?=(?:[A-Z][A-Za-z0-9\s,&./()-]+?\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:|\(cid:190\) Project Schedule:))|\Z)"
            , re.DOTALL
        )

        for project_match in project_in_section_pattern.finditer(section_content):
            project_name = project_match.group('project_name').strip()
            project_details_text = project_match.group('project_details').strip()
            
            start_date = 'Unknown'
            start_date_match = re.search(
                r'(?:Begin Construction|Advertise|Complete Design|Final Design|Project Schedule):\s*((?:2022|2023|Spring|Summer|Fall|Winter)[a-zA-Z0-9-]*)',
                project_details_text, re.IGNORECASE
            )
            if start_date_match:
                start_date = start_date_match.group(1)

            extracted_projects.append({
                'Project_Name': project_name,
                'type': 'disaster', # Explicitly a disaster project from this section
                'st': start_date
            })

    # Now, also scan the entire document for projects that might not be in a specific 'Disaster Recovery Projects' section
    # but contain 'FEMA' or 'CalOES' in their name or details, implying they are disaster-related.
    # This pattern is more general for any project block.
    general_project_pattern = re.compile(
        r"(?P<project_name>[A-Z][A-Za-z0-9\s,&./()-]+?)\n\n" # Project Name
        r"(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:|\(cid:190\) Project Schedule:)" # Start of details
        r"(?P<project_details>[\s\S]*?)"
        r"(?=(?:[A-Z][A-Za-z0-9\s,&./()-]+?\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:|\(cid:190\) Project Schedule:))|\Z|Capital Improvement Projects|Disaster Recovery Projects)"
        , re.DOTALL
    )

    for match in general_project_pattern.finditer(text):
        project_name = match.group('project_name').strip()
        project_details_text = match.group('project_details').strip()

        project_type = 'capital' # Default to capital if not explicitly set
        # If it was already identified as disaster from the section, keep it.
        # Otherwise, check for FEMA/CalOES in name or details.
        if ('FEMA' in project_details_text or
            'CalOES' in project_details_text or
            '(FEMA Project)' in project_name or
            '(CalOES Project)' in project_name):
            project_type = 'disaster'
        
        # Avoid adding duplicates if already added from the disaster section extraction
        if not any(p['Project_Name'] == project_name and p['type'] == project_type for p in extracted_projects):
            start_date = 'Unknown'
            start_date_match = re.search(
                r'(?:Begin Construction|Advertise|Complete Design|Final Design|Project Schedule):\s*((?:2022|2023|Spring|Summer|Fall|Winter)[a-zA-Z0-9-]*)',
                project_details_text, re.IGNORECASE
            )
            if start_date_match:
                start_date = start_date_match.group(1)

            extracted_projects.append({
                'Project_Name': project_name,
                'type': project_type,
                'st': start_date
            })

# Filter for disaster projects that started in 2022
disaster_projects_2022_names = []
for project in extracted_projects:
    if project['type'] == 'disaster' and isinstance(project['st'], str) and '2022' in project['st']:
        disaster_projects_2022_names.append(project['Project_Name'])

unique_disaster_projects_2022_names = list(set(disaster_projects_2022_names))

print('__RESULT__:')
print(json.dumps(unique_disaster_projects_2022_names))"""

env_args = {'var_function-call-6790680028144073528': 'file_storage/function-call-6790680028144073528.json', 'var_function-call-12440770224826216985': []}

exec(code, env_args)

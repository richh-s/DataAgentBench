code = """import json
import re

def parse_project_info_revised(text):
    projects = []
    
    # Use a single regex to find all project blocks
    # A project block starts with a project name and continues until another project name or a major section header.
    # This regex is an attempt to capture project name, and then all text until the next project or a new section starts.
    project_block_regex = re.compile(r'\n\n([A-Za-z0-9][A-Za-z0-9\\s&,-/]+?)\n\n\\(cid:190\\) (Updates:|Project Description:|Project Schedule:|Estimated Schedule:)(.*?)(?=\n\n[A-Za-z0-9][A-Za-z0-9\\s&,-/]+?\n\n\\(cid:190\\) |Capital Improvement Projects|Disaster Recovery Projects|Public Works Commission|Agenda Report|RECOMMENDED ACTION:)', re.DOTALL)

    # Find section headers to determine project type and general status
    capital_design_regex = re.compile(r'Capital Improvement Projects \(Design\)')
    capital_construction_regex = re.compile(r'Capital Improvement Projects \(Construction\)')
    capital_not_started_regex = re.compile(r'Capital Improvement Projects \(Not Started\)')
    disaster_recovery_regex = re.compile(r'Disaster Recovery Projects')

    current_project_type = None
    current_status = None

    # Iterate through the text to establish the current section type and status
    # This needs to be done more carefully, as project blocks might not strictly follow these headers line by line.
    # Let's first extract all project blocks and then determine their context.

    matches = list(project_block_regex.finditer(text))

    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        project_details_block = match.group(0) # This includes the project name and the details
        
        project_topic = []
        if re.search(r'emergency', project_details_block, re.IGNORECASE):
            project_topic.append('emergency')
        if re.search(r'FEMA', project_details_block, re.IGNORECASE):
            project_topic.append('FEMA')

        # Determine type and status based on preceding section headers
        # This is a bit tricky, and ideally, we'd know the section context of each project.
        # For now, let's assume the most recently encountered section header applies to the projects that follow.
        # This isn't perfect but a pragmatic approach given the unstructured nature of the text.
        
        # To handle this more robustly, we need to know the offset of each project and the section headers
        
        # Re-scan the text for section headers to get the correct context for each project block
        # This is not efficient, but demonstrates the logic.
        block_start_index = match.start()
        
        # Find the last occurring section header before this project block
        last_section_header_index = -1
        temp_project_type = None
        temp_status = None

        for header_match in capital_design_regex.finditer(text):
            if header_match.start() < block_start_index and header_match.start() > last_section_header_index:
                last_section_header_index = header_match.start()
                temp_project_type = 'capital'
                temp_status = 'design'
        for header_match in capital_construction_regex.finditer(text):
            if header_match.start() < block_start_index and header_match.start() > last_section_header_index:
                last_section_header_index = header_match.start()
                temp_project_type = 'capital'
                temp_status = 'under construction'
        for header_match in capital_not_started_regex.finditer(text):
            if header_match.start() < block_start_index and header_match.start() > last_section_header_index:
                last_section_header_index = header_match.start()
                temp_project_type = 'capital'
                temp_status = 'not started'
        for header_match in disaster_recovery_regex.finditer(text):
            if header_match.start() < block_start_index and header_match.start() > last_section_header_index:
                last_section_header_index = header_match.start()
                temp_project_type = 'disaster'
                temp_status = 'disaster recovery'

        if project_topic:
            projects.append({
                'Project_Name': project_name,
                'status': temp_status,
                'type': temp_project_type,
                'topic': ', '.join(project_topic)
            })
    
    return projects

all_projects = []
with open(locals()['var_function-call-5052213206219168496'], 'r') as f:
    docs = json.load(f)

for doc in docs:
    all_projects.extend(parse_project_info_revised(doc['text']))

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for project in all_projects:
    if project['Project_Name'] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-5052213206219168496': 'file_storage/function-call-5052213206219168496.json'}

exec(code, env_args)

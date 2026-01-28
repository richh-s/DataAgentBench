code = """import json
import re

def parse_civic_document_v4(text):
    projects = []
    
    # Regex to find potential project names. Project names often appear on a line by themselves.
    # We'll use a broad pattern and then filter later.
    # Looking for lines that start with an uppercase letter or number, followed by other characters.
    project_name_candidates = re.finditer(r'\n\n([A-Z0-9][A-Za-z0-9\s&,.-/]+?)(?=\n\n|\n\(cid:190\))', text)

    project_candidates_list = []
    for match in project_name_candidates:
        project_name = match.group(1).strip()
        # Filter out headers that might be mistakenly identified as project names
        if not any(re.search(keyword, project_name, re.IGNORECASE) for keyword in [
            'Public Works Commission', 'Agenda Report', 'RECOMMENDED ACTION', 'Capital Improvement Projects', 'Disaster Recovery Projects'
        ]) and len(project_name) > 5: # Basic length check to filter out very short phrases
            project_candidates_list.append({'name': project_name, 'start': match.start(), 'end': match.end()})

    # Regex for section headers
    capital_design_header = re.compile(r'Capital Improvement Projects \(Design\)')
    capital_construction_header = re.compile(r'Capital Improvement Projects \(Construction\)')
    capital_not_started_header = re.compile(r'Capital Improvement Projects \(Not Started\)')
    disaster_recovery_header = re.compile(r'Disaster Recovery Projects')
    
    for i, project_candidate in enumerate(project_candidates_list):
        project_name = project_candidate['name']
        project_start_index = project_candidate['start']
        project_end_index = len(text)
        if i + 1 < len(project_candidates_list):
            project_end_index = project_candidates_list[i+1]['start']
        
        project_context_block = text[project_start_index:project_end_index] # Text from project name to next project

        current_type = None
        current_status = None
        last_header_index = -1

        # Search for headers before the current project candidate
        # We need to search the *entire document* for headers to ensure we get the closest one
        # up to the project_start_index.
        search_area_for_headers = text[:project_start_index]

        for header_match in capital_design_header.finditer(search_area_for_headers):
            if header_match.end() > last_header_index:
                current_type = 'capital'
                current_status = 'design'
                last_header_index = header_match.end()
        
        for header_match in capital_construction_header.finditer(search_area_for_headers):
            if header_match.end() > last_header_index:
                current_type = 'capital'
                current_status = 'under construction'
                last_header_index = header_match.end()

        for header_match in capital_not_started_header.finditer(search_area_for_headers):
            if header_match.end() > last_header_index:
                current_type = 'capital'
                current_status = 'not started'
                last_header_index = header_match.end()

        for header_match in disaster_recovery_header.finditer(search_area_for_headers):
            if header_match.end() > last_header_index:
                current_type = 'disaster'
                current_status = 'disaster recovery'
                last_header_index = header_match.end()
        
        # Check for 'emergency' or 'FEMA' keywords within the project's context block
        project_topic = []
        if re.search(r'emergency', project_context_block, re.IGNORECASE):
            project_topic.append('emergency')
        if re.search(r'FEMA', project_context_block, re.IGNORECASE):
            project_topic.append('FEMA')
        
        # Only add the project if it has relevant topics and a determined type/status
        if project_topic and current_type and current_status:
            projects.append({
                'Project_Name': project_name,
                'status': current_status,
                'type': current_type,
                'topic': ', '.join(project_topic)
            })
            
    return projects

all_projects = []
with open(locals()['var_function-call-5052213206219168496'], 'r') as f:
    docs = json.load(f)

for doc in docs:
    all_projects.extend(parse_civic_document_v4(doc['text']))

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

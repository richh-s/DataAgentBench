code = """import json
import re

def extract_disaster_projects_2022(text):
    projects = []
    
    # First, try to extract the entire 'Disaster Recovery Projects' section.
    # It starts with "Disaster Recovery Projects" and ends before another major project section or end of document.
    # Using raw string for the regex pattern and ensuring proper escaping
    disaster_section_pattern = re.compile(
        r'Disaster Recovery Projects\n\n(.*?)'
        r'(?:\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|\n\nCapital Improvement Projects \(Design\)|$)',
        re.DOTALL
    )
    
    disaster_section_match = disaster_section_pattern.search(text)
    if not disaster_section_match:
        return projects # No disaster section found

    disaster_section_text = disaster_section_match.group(1)

    # Now, within this disaster_section_text, find individual projects that started in 2022.
    # A project starts with its name (e.g., 'Project Name Project'), followed by details, 
    # and somewhere in the details, there should be a schedule indicating a 2022 start.
    project_and_2022_start_pattern = re.compile(
        r'([A-Z][a-zA-Z0-9_ -]+ Project)\n\n'  # Capture Project Name (Group 1)
        r'(?:.*?)'  # Non-greedy match for any details in between
        r'(?:Project Schedule:|Estimated Schedule:)\n\n'  # Schedule header
        r'(?:.*?)'  # Non-greedy match for any details in between schedule header and 2022
        r'(?:Begin Construction|Advertise|Complete Design|Final Design):\s*'  # Start date indicator
        r'(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)?\s*(2022)',  # Capture 2022 (Group 2)
        re.DOTALL | re.IGNORECASE
    )

    for match in project_and_2022_start_pattern.finditer(disaster_section_text):
        project_name = match.group(1).strip()
        start_year = match.group(2) # This will be '2022'

        projects.append({
            'Project_Name': project_name,
            'type': 'disaster',
            'st': start_year
        })

    return projects

file_path = locals()['var_function-call-13890045868796138189']
with open(file_path, 'r') as f:
    data_from_file = json.load(f)

all_projects = []
# The structure is data_from_file -> 'query_db_response' -> 'results' which is a list of dicts
for doc in data_from_file['query_db_response']['results']:
    all_projects.extend(extract_disaster_projects_2022(doc['text']))

# Filter to get unique project names that are disaster-related and started in 2022
disaster_projects_2022 = list(set([p['Project_Name'] for p in all_projects]))

print('__RESULT__:')
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-13890045868796138189': 'file_storage/function-call-13890045868796138189.json'}

exec(code, env_args)

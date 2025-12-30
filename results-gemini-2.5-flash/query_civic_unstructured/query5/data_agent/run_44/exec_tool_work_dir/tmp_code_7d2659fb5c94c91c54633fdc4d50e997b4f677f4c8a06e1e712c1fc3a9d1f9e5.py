code = """import json
import re

def extract_disaster_projects_2022(text):
    projects = []
    # Define markers for the start and end of the 'Disaster Recovery Projects' section
    disaster_section_start_marker = r'Disaster Recovery Projects\n\n'
    capital_section_markers = [
        r'Capital Improvement Projects \(Construction\)',
        r'Capital Improvement Projects \(Not Started\)',
        r'Capital Improvement Projects \(Design\)'
    ]

    # Find the start of the disaster section
    start_match = re.search(disaster_section_start_marker, text)
    if not start_match:
        return projects

    disaster_section_start_idx = start_match.end()

    # Find the end of the disaster section (before the next capital section or end of text)
    disaster_section_end_idx = len(text)
    for marker in capital_section_markers:
        end_match = re.search(marker, text[disaster_section_start_idx:])
        if end_match:
            disaster_section_end_idx = disaster_section_start_idx + end_match.start()
            break

    disaster_section_text = text[disaster_section_start_idx:disaster_section_end_idx]

    # Regex to find project name and then look for 2022 in its schedule
    # This pattern looks for a project name (Group 1), then any content until 'Project Schedule:' or 'Estimated Schedule:'
    # followed by content that contains '2022'.
    project_and_2022_schedule_pattern = re.compile(
        r'([A-Z][a-zA-Z0-9_ -]+ Project)\n\n'  # Project Name
        r'(?:(?!([A-Z][a-zA-Z0-9_ -]+ Project)).)*?'  # Non-greedy match until next project or schedule
        r'(?:Project Schedule:|Estimated Schedule:)\n\n'  # Schedule header
        r'(?:(?!([A-Z][a-zA-Z0-9_ -]+ Project)).)*?'  # Non-greedy match until next project or 2022
        r'2022'  # Look for '2022'
        , re.DOTALL | re.IGNORECASE
    )

    for match in project_and_2022_schedule_pattern.finditer(disaster_section_text):
        project_name = match.group(1).strip()
        projects.append({
            'Project_Name': project_name,
            'type': 'disaster',
            'st': '2022' # We know it's 2022 based on the regex match
        })

    return projects

file_path = locals()['var_function-call-13890045868796138189']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data['query_db_response']['results']:
    all_projects.extend(extract_disaster_projects_2022(doc['text']))

disaster_projects_2022 = list(set([p['Project_Name'] for p in all_projects]))

print('__RESULT__:')
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-13890045868796138189': 'file_storage/function-call-13890045868796138189.json'}

exec(code, env_args)

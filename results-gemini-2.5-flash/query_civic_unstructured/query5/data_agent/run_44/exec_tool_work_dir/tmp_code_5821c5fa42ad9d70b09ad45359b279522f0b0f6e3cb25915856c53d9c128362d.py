code = """import json
import re

def extract_disaster_projects_2022(text):
    projects = []
    
    # Use raw string literals for regex patterns to avoid issues with backslashes and quotes
    # First, try to extract the entire 'Disaster Recovery Projects' section.
    # It starts with "Disaster Recovery Projects" and ends before another major project section or end of document.
    disaster_section_pattern = re.compile(
        r'Disaster Recovery Projects\n\n(.*?)('
        r'(?:\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|\n\nCapital Improvement Projects \(Design\)|$)'
        r')', re.DOTALL
    )
    
    disaster_section_match = disaster_section_pattern.search(text)
    if not disaster_section_match:
        return projects # No disaster section found

    disaster_section_text = disaster_section_match.group(1)

    # Now, within this disaster_section_text, find individual projects that started in 2022.
    # A project starts with its name (e.g., 'Project Name Project'), followed by details, 
    # and somewhere in the details, there should be a schedule indicating a 2022 start.
    # Project name (Group 1), then look for 2022 within its schedule. The schedule section can be complex.
    # Simplified: Look for a project name followed by '2022' anywhere in its subsequent details.
    project_and_2022_start_pattern = re.compile(
        r'([A-Z][a-zA-Z0-9_ -]+ Project)'  # Capture Project Name (Group 1)
        r'.*?' # Non-greedy match for any details in between until 2022 or next project
        r'2022' # Look for '2022' as an indicator of start year
        r'.*?' # Non-greedy match for any remaining details until the end of the project block or end of section
        r'(?=\n\n[A-Z][a-zA-Z0-9_ -]+ Project|$)', # Positive lookahead for next project or end of section
        re.DOTALL | re.IGNORECASE
    )

    for match in project_and_2022_start_pattern.finditer(disaster_section_text):
        project_name = match.group(1).strip()
        # Since we found '2022' in the text associated with this project, we can assume it started in 2022.
        projects.append({
            'Project_Name': project_name,
            'type': 'disaster',
            'st': '2022'
        })

    return projects

file_path = locals()['var_function-call-13890045868796138189']
with open(file_path, 'r') as f:
    data_from_file = json.load(f)

all_projects = []
for doc in data_from_file['query_db_response']['results']:
    all_projects.extend(extract_disaster_projects_2022(doc['text']))

# Filter to get unique project names that are disaster-related and started in 2022
disaster_projects_2022 = list(set([p['Project_Name'] for p in all_projects]))

print('__RESULT__:')
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-13890045868796138189': 'file_storage/function-call-13890045868796138189.json'}

exec(code, env_args)

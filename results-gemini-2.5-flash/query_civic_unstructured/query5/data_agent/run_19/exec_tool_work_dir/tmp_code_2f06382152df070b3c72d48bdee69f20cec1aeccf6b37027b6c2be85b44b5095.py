code = """import json
import re

file_path = locals()['var_function-call-18315951507690339385']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']

    # Regex to find project blocks within "Capital Improvement Projects" or "Disaster Recovery Projects"
    # and then extract individual projects within those blocks.
    # We are particularly interested in "Disaster Recovery Projects" section.

    # This regex attempts to find sections starting with 'Disaster Recovery Projects'
    # and capture all text until the next major section or end of document.
    disaster_section_match = re.search(r'Disaster Recovery Projects(.*?)((?:Capital Improvement Projects|Page \d of \d)|$)', text, re.DOTALL)

    if disaster_section_match:
        disaster_section_text = disaster_section_match.group(1)

        # Regex to find individual project names and their schedules within the disaster section
        # Project Name is usually followed by '(cid:190) Updates:' or '(cid:190) Project Schedule:'
        # and then the schedule details are listed under 'Project Schedule:'
        project_pattern = re.compile(r'([A-Za-z0-9][A-Za-z0-9\s&/-]+?)(?:\n\n|\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:))', re.DOTALL)
        
        # Find all potential project names in the section
        project_names_in_section = [match.group(1).strip() for match in project_pattern.finditer(disaster_section_text)]

        for project_name in project_names_in_section:
            # Look for the specific project details including schedule within the disaster section
            # The pattern is more specific now, looking for Project Schedule or Estimated Schedule after the project name
            project_detail_pattern = re.compile(r'(' + re.escape(project_name) + r')\n(?:.*?)\n\(cid:190\) (?:Project|Estimated) Schedule:\n(.*?)(?=\n\n[A-Za-z0-9]|Page \d of \d|$)', re.DOTALL)
            detail_match = project_detail_pattern.search(disaster_section_text)

            if detail_match:
                schedule_text = detail_match.group(2)
                
                # Check for "2022" in the schedule text to identify start year
                if "2022" in schedule_text:
                    disaster_projects_2022.append(project_name)

# Remove duplicates from the list of project names
disaster_projects_2022_unique = list(set(disaster_projects_2022))

__RESULT__:
print(json.dumps(disaster_projects_2022_unique))"""

env_args = {'var_function-call-14240416266777266539': ['civic_docs'], 'var_function-call-18315951507690339385': 'file_storage/function-call-18315951507690339385.json'}

exec(code, env_args)

code = """import json
import re

with open(locals()['var_function-call-5170959527222557152'], 'r') as f:
    funded_projects_data = json.load(f)

with open(locals()['var_function-call-1640262124798972523'], 'r') as f:
    civic_docs_data = json.load(f)

funded_project_names = {project['Project_Name'] for project in funded_projects_data}

capital_design_projects = set()

for doc in civic_docs_data:
    text = doc['text']
    # Find the section for 'Capital Improvement Projects (Design)'
    # The ending condition ensures we don't accidentally include projects from other sections.
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:|Staff has also prepared a Public Works Quarterly Update flier|Page \d of \d|$)', text, re.DOTALL)

    if design_section_match:
        design_section_text = design_section_match.group(1)
        # Split the section into lines and filter for project names
        lines = design_section_text.split('\n')
        for line in lines:
            cleaned_line = line.strip()
            # Heuristic to identify project names:
            # - Not empty
            # - Does not start with common bullet points or section headers
            # - Not in a list of known non-project names (like 'Discussion', 'Recommended Action', etc.)
            if cleaned_line and \
               not cleaned_line.startswith('(cid:190)') and \
               not cleaned_line.startswith('Page') and \
               not cleaned_line.startswith('Agenda Item') and \
               not cleaned_line in ['Discussion', 'Recommended Action', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:']:
                capital_design_projects.add(cleaned_line)

# Find the intersection of projects
intersecting_projects = funded_project_names.intersection(capital_design_projects)

__RESULT__:
print(json.dumps(len(intersecting_projects)))"""

env_args = {'var_function-call-5170959527222557152': 'file_storage/function-call-5170959527222557152.json', 'var_function-call-1640262124798972523': 'file_storage/function-call-1640262124798972523.json'}

exec(code, env_args)

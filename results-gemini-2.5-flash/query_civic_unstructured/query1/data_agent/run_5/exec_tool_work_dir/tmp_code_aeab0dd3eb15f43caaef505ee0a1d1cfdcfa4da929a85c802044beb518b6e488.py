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
    
    # Find the section containing 'Capital Improvement Projects (Design)'
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:|Staff has also prepared a Public Works Quarterly Update flier|Page \d of \d|$)', text, re.DOTALL)

    if design_section_match:
        design_section_text = design_section_match.group(1)
        # Project names are usually on a single line, followed by bullet points describing updates or schedules.
        # We are looking for lines that do not start with a bullet point but are followed by one.
        # This pattern captures the line before the bullet point line.
        project_name_candidates = re.findall(r'([^\n]+)\s*\n\s*\(cid:190\) (?:Updates:|Project Schedule:|Estimated Schedule:|Project Description:)', design_section_text)
        
        for name in project_name_candidates:
            cleaned_name = name.strip()
            # Filter out non-project names that might match the pattern (like section headers)
            if cleaned_name and not cleaned_name.startswith(('Discussion', 'Recommended Action', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'Page', 'Agenda Item')):
                capital_design_projects.add(cleaned_name)

intersecting_projects = funded_project_names.intersection(capital_design_projects)

__RESULT__:
print(json.dumps(len(intersecting_projects)))"""

env_args = {'var_function-call-5170959527222557152': 'file_storage/function-call-5170959527222557152.json', 'var_function-call-1640262124798972523': 'file_storage/function-call-1640262124798972523.json'}

exec(code, env_args)

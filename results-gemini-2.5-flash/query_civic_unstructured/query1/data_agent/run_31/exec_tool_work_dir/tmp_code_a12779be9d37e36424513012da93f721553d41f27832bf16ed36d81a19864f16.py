code = """import json
import re

with open(locals()['var_function-call-9187705618575875999'], 'r') as f:
    civic_docs_data = json.load(f)

projects_data = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Capture the section for 'Capital Improvement Projects (Design)'
    design_section_match = re.search(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|\Z)", text, re.DOTALL)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        # Extract project names within the design section that are followed by '(cid:190) Updates:'
        # Project names usually appear on a new line and before '(cid:190) Updates:'
        project_names = re.findall(r"\n([A-Za-z0-9&,\- ]+?)\n\s*\(cid:190\) Updates:", design_section)
        for name in project_names:
            projects_data.append({'Project_Name': name.strip(), 'type': 'capital', 'status': 'design'})
        
        # Also consider Project names followed by '(cid:190) Estimated Schedule:' as they could be in design stage
        project_names_est_schedule = re.findall(r"\n([A-Za-z0-9&,\- ]+?)\n\s*\(cid:190\) Estimated Schedule:", design_section)
        for name in project_names_est_schedule:
            projects_data.append({'Project_Name': name.strip(), 'type': 'capital', 'status': 'design'})

# Remove duplicates
unique_projects = []
seen_projects = set()
for project in projects_data:
    project_tuple = (project['Project_Name'], project['type'], project['status'])
    if project_tuple not in seen_projects:
        unique_projects.append(project)
        seen_projects.add(project_tuple)

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-1231612348361666956': ['civic_docs'], 'var_function-call-9187705618575875999': 'file_storage/function-call-9187705618575875999.json', 'var_function-call-13415763849644264601': ['Funding']}

exec(code, env_args)

code = """import json
import re

with open(locals()['var_function-call-9187705618575875999'], 'r') as f:
    civic_docs_data = json.load(f)

projects_data = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to find project sections and their projects
    # This regex is simplified and might need adjustment based on typical document structure
    # It looks for headers like "Capital Improvement Projects (Design)" and captures projects listed under them until the next header or end of document.
    
    # Pattern to capture project type and status from headers, and then the project names
    # Example: "Capital Improvement Projects (Design)" followed by project names
    # This pattern will need to be robust to variations.
    
    # Let's try to extract project names under specific headings.
    # Grouping by type and status.
    
    # Capital Improvement Projects
    capital_design_projects = re.findall(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects|Disaster Recovery Projects|Public Works Commission|Agenda Report|RECOMMENDED ACTION|DISCUSSION|Page \d of \d|Subject:|Item)", text, re.DOTALL)
    for section in capital_design_projects:
        project_names = re.findall(r"\n\n([A-Za-z0-9&,\- ]+?)\n\n(cid:190) Updates:", section)
        for name in project_names:
            projects_data.append({'Project_Name': name.strip(), 'type': 'capital', 'status': 'design'})
        
        project_names = re.findall(r"\n([A-Za-z0-9&,\- ]+?)\n\n(cid:190) Updates:", section)
        for name in project_names:
            projects_data.append({'Project_Name': name.strip(), 'type': 'capital', 'status': 'design'})


    capital_construction_projects = re.findall(r"Capital Improvement Projects \(Construction\)(.*?)(?:Capital Improvement Projects|Disaster Recovery Projects|Public Works Commission|Agenda Report|RECOMMENDED ACTION|DISCUSSION|Page \d of \d|Subject:|Item)", text, re.DOTALL)
    for section in capital_construction_projects:
        project_names = re.findall(r"\n\n([A-Za-z0-9&,\- ]+?)\n\n(cid:190) Updates:", section)
        for name in project_names:
            projects_data.append({'Project_Name': name.strip(), 'type': 'capital', 'status': 'construction'})
        project_names = re.findall(r"\n([A-Za-z0-9&,\- ]+?)\n\n(cid:190) Updates:", section)
        for name in project_names:
            projects_data.append({'Project_Name': name.strip(), 'type': 'capital', 'status': 'construction'})
    
    capital_not_started_projects = re.findall(r"Capital Improvement Projects \(Not Started\)(.*?)(?:Capital Improvement Projects|Disaster Recovery Projects|Public Works Commission|Agenda Report|RECOMMENDED ACTION|DISCUSSION|Page \d of \d|Subject:|Item)", text, re.DOTALL)
    for section in capital_not_started_projects:
        project_names = re.findall(r"\n\n([A-Za-z0-9&,\- ]+?)\n\n(cid:190) Project Description:", section)
        for name in project_names:
            projects_data.append({'Project_Name': name.strip(), 'type': 'capital', 'status': 'not started'})
        project_names = re.findall(r"\n([A-Za-z0-9&,\- ]+?)\n\n(cid:190) Project Description:", section)
        for name in project_names:
            projects_data.append({'Project_Name': name.strip(), 'type': 'capital', 'status': 'not started'})

    
    # Disaster Recovery Projects - this query specifically asks for "capital" projects, so disaster recovery projects are not directly needed, 
    # but parsing them can help delineate sections better in the regex.
    # For now, let's just focus on capital projects.

# Remove duplicates
unique_projects = []
seen_projects = set()
for project in projects_data:
    if (project['Project_Name'], project['type'], project['status']) not in seen_projects:
        unique_projects.append(project)
        seen_projects.add((project['Project_Name'], project['type'], project['status']))

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-1231612348361666956': ['civic_docs'], 'var_function-call-9187705618575875999': 'file_storage/function-call-9187705618575875999.json', 'var_function-call-13415763849644264601': ['Funding']}

exec(code, env_args)

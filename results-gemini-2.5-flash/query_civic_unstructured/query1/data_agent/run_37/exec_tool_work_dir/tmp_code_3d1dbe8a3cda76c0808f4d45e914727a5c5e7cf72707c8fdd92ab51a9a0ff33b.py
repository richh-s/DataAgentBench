code = """import json
import re

def extract_design_projects(text):
    projects = []
    design_section_match = re.search(
        r"Capital Improvement Projects \\(Design\\)(.*?)(?:Capital Improvement Projects \\(Construction\\)|Capital Improvement Projects \\(Not Started\\)|Disaster Recovery Projects|RECOMMENDED ACTION:|\\Z)",
        text, re.DOTALL
    )

    if design_section_match:
        design_content = design_section_match.group(1)
        
        lines = design_content.split('\\n')
        current_project_name_parts = []

        for line in lines:
            stripped_line = line.strip()

            if not stripped_line or stripped_line.startswith('(cid:') or stripped_line.lower().startswith('page') or stripped_line.lower().startswith('agenda item'):
                if current_project_name_parts:
                    project_name = ' '.join(current_project_name_parts).strip()
                    projects.append({"Project_Name": project_name, "type": "capital", "status": "design"})
                    current_project_name_parts = []
                continue

            if re.search(r'(?:Updates:|Project Schedule:|Estimated Schedule:)', stripped_line):
                if current_project_name_parts:
                    project_name = ' '.join(current_project_name_parts).strip()
                    projects.append({"Project_Name": project_name, "type": "capital", "status": "design"})
                    current_project_name_parts = []
                continue
            
            current_project_name_parts.append(stripped_line)
        
        if current_project_name_parts:
            project_name = ' '.join(current_project_name_parts).strip()
            projects.append({"Project_Name": project_name, "type": "capital", "status": "design"})

    return projects

file_path = locals()['var_function-call-16303420803371647737']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

all_extracted_projects = []
for doc in civic_docs:
    all_extracted_projects.extend(extract_design_projects(doc['text']))

final_projects = []
seen_project_names = set()

for p in all_extracted_projects:
    cleaned_name = re.sub(r'\\(cid:\\d+\\)', '', p["Project_Name"]).strip()
    
    if (
        5 < len(cleaned_name) < 100 and
        cleaned_name.count(' ') < 15 and
        not re.search(r'(updates:|project schedule:|estimated schedule:|project description:|this project will consist of|staff is working with)', cleaned_name.lower())
    ):
        if cleaned_name not in seen_project_names:
            seen_project_names.add(cleaned_name)
            final_projects.append({"Project_Name": cleaned_name, "type": p["type"], "status": p["status"]})

print("__RESULT__:")
print(json.dumps(final_projects))"""

env_args = {'var_function-call-841909728376098398': ['civic_docs'], 'var_function-call-16303420803371647737': 'file_storage/function-call-16303420803371647737.json', 'var_function-call-15519595974979010567': 'file_storage/function-call-15519595974979010567.json'}

exec(code, env_args)

code = """import json
import re

def extract_projects(text):
    projects = []
    # Find the "Capital Improvement Projects (Design)" section
    design_section_match = re.search(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:)", text, re.DOTALL)

    if design_section_match:
        design_section = design_section_match.group(1)
        lines = design_section.split('\n')
        current_project_name_parts = []
        for line in lines:
            stripped_line = line.strip()
            if not stripped_line:  # Skip empty lines
                continue
            if stripped_line.startswith('(cid:') or stripped_line.startswith('Page') or stripped_line.startswith('Agenda Item'):
                # These are usually bullet points, page numbers, or agenda items, not project names
                if current_project_name_parts:
                    project_name = ' '.join(current_project_name_parts).strip()
                    projects.append({"Project_Name": project_name, "type": "capital", "status": "design"})
                    current_project_name_parts = [] # Reset for next project
                continue
            # If we encounter an 'Updates:' or 'Project Schedule:' line, it means the previous lines formed a project name
            if 'Updates:' in stripped_line or 'Project Schedule:' in stripped_line or 'Estimated Schedule:' in stripped_line:
                if current_project_name_parts:
                    project_name = ' '.join(current_project_name_parts).strip()
                    projects.append({"Project_Name": project_name, "type": "capital", "status": "design"})
                    current_project_name_parts = [] # Reset for next project
                continue
            current_project_name_parts.append(stripped_line)
        # Add the last project if any parts are remaining
        if current_project_name_parts:
            project_name = ' '.join(current_project_name_parts).strip()
            projects.append({"Project_Name": project_name, "type": "capital", "status": "design"})

    return projects

file_path = locals()['var_function-call-16303420803371647737']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

all_projects = []
for doc in civic_docs:
    all_projects.extend(extract_projects(doc['text']))

# Remove duplicates based on Project_Name
project_names_set = set()
clean_unique_projects = []
for p in all_projects:
    if p["Project_Name"] not in project_names_set:
        project_names_set.add(p["Project_Name"])
        clean_unique_projects.append(p)

print("__RESULT__:")
print(json.dumps(clean_unique_projects))"""

env_args = {'var_function-call-841909728376098398': ['civic_docs'], 'var_function-call-16303420803371647737': 'file_storage/function-call-16303420803371647737.json'}

exec(code, env_args)

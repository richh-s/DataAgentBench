code = """import json
import re

def extract_projects(text):
    projects = []
    design_section_match = re.search(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:|\\Z)", text, re.DOTALL)

    if design_section_match:
        design_section = design_section_match.group(1)
        lines = design_section.split('\n')
        current_project_name_parts = []

        for line in lines:
            stripped_line = line.strip()

            # Skip empty lines and lines that are clearly not project names
            if not stripped_line or stripped_line.startswith('(cid:') or stripped_line.lower().startswith('page') or stripped_line.lower().startswith('agenda item'):
                if current_project_name_parts: # If we've collected parts, the project name has ended
                    project_name = ' '.join(current_project_name_parts).strip()
                    projects.append({"Project_Name": project_name, "type": "capital", "status": "design"})
                    current_project_name_parts = []
                continue

            # If we encounter an 'Updates:' or 'Project Schedule:' line, the project name is complete
            if re.search(r'(?:Updates:|Project Schedule:|Estimated Schedule:)', stripped_line):
                if current_project_name_parts:
                    project_name = ' '.join(current_project_name_parts).strip()
                    projects.append({"Project_Name": project_name, "type": "capital", "status": "design"})
                    current_project_name_parts = []
                continue

            # If none of the above, it's likely part of a project name
            current_project_name_parts.append(stripped_line)
        
        # After the loop, add any remaining project name parts
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

# Filter and clean up the extracted projects
project_names_set = set()
clean_unique_projects = []
for p in all_projects:
    clean_name = re.sub(r'\\(cid:\\d+\\)', '', p["Project_Name"]).strip()
    # Further heuristic: project names should generally be concise and not sound like full sentences or descriptions.
    # Filter out names that are very short (e.g., just 'project') or very long, or contain too many keywords that indicate a description.
    if 5 < len(clean_name) < 150 and clean_name.count(' ') < 25 and not re.search(r'(this project will consist of|project description|staff is working with the consultant|updates:|project schedule:)', clean_name.lower()):
        if clean_name not in project_names_set:
            project_names_set.add(clean_name)
            p["Project_Name"] = clean_name
            clean_unique_projects.append(p)

print("__RESULT__:")
print(json.dumps(clean_unique_projects))"""

env_args = {'var_function-call-841909728376098398': ['civic_docs'], 'var_function-call-16303420803371647737': 'file_storage/function-call-16303420803371647737.json', 'var_function-call-15519595974979010567': 'file_storage/function-call-15519595974979010567.json'}

exec(code, env_args)

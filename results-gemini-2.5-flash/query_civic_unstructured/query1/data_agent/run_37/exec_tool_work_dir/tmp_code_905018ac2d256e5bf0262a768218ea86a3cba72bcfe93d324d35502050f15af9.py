code = """import json
import re

def extract_projects(text):
    projects = []
    # Find the \"Capital Improvement Projects (Design)\" section
    design_section_match = re.search(\"Capital Improvement Projects \\\\(Design\\\\)(.*?)(?:Capital Improvement Projects \\\\(Construction\\\\)|Capital Improvement Projects \\\\(Not Started\\\\)|Disaster Recovery Projects|RECOMMENDED ACTION:)\", text, re.DOTALL)

    if design_section_match:
        design_section = design_section_match.group(1)
        lines = design_section.split('\\n')
        current_project_name_parts = []

        for line in lines:
            stripped_line = line.strip()

            # Skip empty lines, lines starting with (cid:), Page, or Agenda Item
            if not stripped_line or stripped_line.startswith('(cid:') or stripped_line.startswith('Page') or stripped_line.startswith('Agenda Item'):
                if current_project_name_parts:  # If we have accumulated parts, this indicates the end of a project name
                    project_name = ' '.join(current_project_name_parts).strip()
                    projects.append({\"Project_Name\": project_name, \"type\": \"capital\", \"status\": \"design\"})
                    current_project_name_parts = []
                continue

            # If we see an update or schedule line, it marks the end of a project name
            if 'Updates:' in stripped_line or 'Project Schedule:' in stripped_line or 'Estimated Schedule:' in stripped_line:
                if current_project_name_parts:
                    project_name = ' '.join(current_project_name_parts).strip()
                    projects.append({\"Project_Name\": project_name, \"type\": \"capital\", \"status\": \"design\"})
                    current_project_name_parts = []
                continue

            # Otherwise, append the line to the current project name parts
            current_project_name_parts.append(stripped_line)
        
        # Add any remaining project name parts after the loop finishes
        if current_project_name_parts:
            project_name = ' '.join(current_project_name_parts).strip()
            projects.append({\"Project_Name\": project_name, \"type\": \"capital\", \"status\": \"design\"})

    return projects

file_path = locals()['var_function-call-16303420803371647737']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

all_projects = []
for doc in civic_docs:
    all_projects.extend(extract_projects(doc['text']))

# Remove duplicates based on Project_Name and clean the name further
project_names_set = set()
clean_unique_projects = []
for p in all_projects:
    # Remove any stray (cid:*) tags that might have slipped through
    clean_name = re.sub(r'\\(cid:\\\\d+\\)', '', p[\"Project_Name\"]).strip()
    if clean_name not in project_names_set:
        project_names_set.add(clean_name)
        p[\"Project_Name\"] = clean_name
        clean_unique_projects.append(p)

print(\"__RESULT__:\")
print(json.dumps(clean_unique_projects))"""

env_args = {'var_function-call-841909728376098398': ['civic_docs'], 'var_function-call-16303420803371647737': 'file_storage/function-call-16303420803371647737.json'}

exec(code, env_args)

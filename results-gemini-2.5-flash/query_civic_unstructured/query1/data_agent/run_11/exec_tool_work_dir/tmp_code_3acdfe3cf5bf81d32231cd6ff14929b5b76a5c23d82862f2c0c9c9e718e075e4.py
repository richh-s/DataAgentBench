code = """import json
import re

def extract_projects_from_text(text):
    projects = []
    design_section_start = text.find("Capital Improvement Projects (Design)")
    end_markers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects",
        "RECOMMENDED ACTION:"
    ]
    design_section_end = len(text)

    for marker in end_markers:
        marker_index = text.find(marker, design_section_start)
        if marker_index != -1 and marker_index < design_section_end:
            design_section_end = marker_index

    if design_section_start != -1:
        design_section_content = text[design_section_start:design_section_end]
        for line in design_section_content.split('\n'):
            stripped_line = line.strip()
            if stripped_line and re.match(r'^[A-Z]', stripped_line) and \
               not ("Updates:" in stripped_line or "Project Schedule:" in stripped_line or "(cid:" in stripped_line) and \
               len(stripped_line) > 10:
                clean_name = re.sub(r"\\(cid:\\d+\\) ", "", stripped_line).strip()
                if clean_name:
                    projects.append({'Project_Name': clean_name, 'type': 'capital', 'status': 'design'})
    return projects

with open(locals()['var_function-call-4307287955121684053'], 'r') as f:
    civic_docs = json.load(f)

all_projects = []
for doc in civic_docs:
    all_projects.extend(extract_projects_from_text(doc['text']))

unique_projects = []
project_names_seen = set()
for project in all_projects:
    if project['Project_Name'] not in project_names_seen:
        unique_projects.append(project)
        project_names_seen.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-3903943541476756532': ['civic_docs'], 'var_function-call-4307287955121684053': 'file_storage/function-call-4307287955121684053.json'}

exec(code, env_args)

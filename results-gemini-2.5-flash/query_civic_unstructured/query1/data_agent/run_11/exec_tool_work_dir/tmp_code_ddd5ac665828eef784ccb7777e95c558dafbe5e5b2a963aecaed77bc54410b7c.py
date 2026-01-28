code = """import json
import re

def extract_projects_from_text(text):
    projects = []
    # Regex to find "Capital Improvement Projects (Design)" section and extract project names
    design_section_match = re.search(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:)", text, re.DOTALL)
    if design_section_match:
        design_section = design_section_match.group(1)
        project_names = re.findall(r"\n\n([A-Z].*?)\n\n", design_section)
        for name in project_names:
            # Clean up the name, remove (cid:190) and similar artifacts
            clean_name = re.sub(r"\(cid:\d+\)", "", name).strip()
            if clean_name:
                projects.append({'Project_Name': clean_name, 'type': 'capital', 'status': 'design'})
    return projects


# Load the full text data
with open(locals()['var_function-call-4307287955121684053'], 'r') as f:
    civic_docs = json.load(f)

all_projects = []
for doc in civic_docs:
    all_projects.extend(extract_projects_from_text(doc['text']))

# Filter for unique projects as some might be mentioned in multiple documents or sections
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

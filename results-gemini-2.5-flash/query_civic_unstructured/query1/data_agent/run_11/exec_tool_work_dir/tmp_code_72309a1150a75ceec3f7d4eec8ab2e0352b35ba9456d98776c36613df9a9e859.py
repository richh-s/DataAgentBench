code = """import json
import re

def extract_design_capital_projects(text):
    projects = []
    # Find the section for 'Capital Improvement Projects (Design)'
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:)', text, re.DOTALL)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        # Iterate through lines in the design section
        for line in design_section.split('\n'):
            stripped_line = line.strip()
            # Heuristic to identify project names: starts with a capital letter, is not an 'Updates:' or 'Project Schedule:' line, and does not contain '(cid:' which is a formatting artifact.
            if stripped_line and re.match(r'^[A-Z]', stripped_line) and 
               not 'Updates:' in stripped_line and 
               not 'Project Schedule:' in stripped_line and 
               not '(cid:' in stripped_line:
                # Clean the project name from any remaining artifacts or extra spaces
                clean_name = re.sub(r'\\(cid:\\d+\\) ', '', stripped_line).strip()
                if clean_name:
                    projects.append({'Project_Name': clean_name, 'type': 'capital', 'status': 'design'})
    return projects

# Load the full text data from the file path
with open(locals()['var_function-call-4307287955121684053'], 'r') as f:
    civic_docs = json.load(f)

all_capital_design_projects = []
for doc in civic_docs:
    all_capital_design_projects.extend(extract_design_capital_projects(doc['text']))

# Filter for unique projects as some might be mentioned in multiple documents or sections
unique_capital_design_projects = []
project_names_seen = set()
for project in all_capital_design_projects:
    if project['Project_Name'] not in project_names_seen:
        unique_capital_design_projects.append(project)
        project_names_seen.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_capital_design_projects))"""

env_args = {'var_function-call-3903943541476756532': ['civic_docs'], 'var_function-call-4307287955121684053': 'file_storage/function-call-4307287955121684053.json', 'var_function-call-6712936743636236687': 'file_storage/function-call-6712936743636236687.json'}

exec(code, env_args)

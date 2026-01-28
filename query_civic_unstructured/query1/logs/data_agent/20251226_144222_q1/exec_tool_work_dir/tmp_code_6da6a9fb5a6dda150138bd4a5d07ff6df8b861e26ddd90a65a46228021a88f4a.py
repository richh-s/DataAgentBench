code = """import json
import pandas as pd

# Load Funding table query result
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funding_data = json.load(f)
funded_projects = set([item['Project_Name'].strip().lower() for item in funding_data])

# Load civic docs query result
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    civic_docs = json.load(f)

def find_design_capital_projects(civic_docs):
    project_names = set()
    for doc in civic_docs:
        text = doc['text'].lower()
        if 'capital improvement projects (design)' in text:
            part = text.split('capital improvement projects (design)')[1]
            for line in part.split('\n'):
                l = line.strip()
                # Detect project names: line must contain 'project' but not 'updates', 'schedule', or ':'
                if 'project' in l and not any(x in l for x in ['updates', 'schedule', ':']):
                    # Clean up, just keep line
                    project_names.add(l)
                # Stop if a new section is reached
                if any(header in l for header in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'discussion:', 'public works commission']):
                    break
    return set([name.strip().lower() for name in project_names])

design_projects = find_design_capital_projects(civic_docs)
count = len(funded_projects & design_projects)
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

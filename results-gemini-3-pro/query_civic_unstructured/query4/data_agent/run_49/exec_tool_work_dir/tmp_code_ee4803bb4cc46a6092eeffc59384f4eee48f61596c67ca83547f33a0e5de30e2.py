code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-1003584179187242714'], 'r') as f:
    funding_data = json.load(f)

funding_projects = {item['Project_Name']: item for item in funding_data}
project_names = list(funding_projects.keys())

# Load Civic Docs
with open(locals()['var_function-call-1003584179187241629'], 'r') as f:
    civic_docs = json.load(f)

def normalize(text):
    return text.strip().lower()

started_projects = set()

# Targeted phrases for Spring 2022
target_dates = ["spring 2022", "march 2022", "april 2022", "may 2022", "spring, 2022"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue
            
        # Check for project name
        # Exact match logic
        found_name = None
        norm_line = normalize(line_str)
        for name in project_names:
            if normalize(name) == norm_line:
                found_name = name
                break
        
        if found_name:
            current_project = found_name
            continue
        
        if current_project:
            # Check for start indicators
            lower_line = line_str.lower()
            
            # Start indicators
            if "begin construction" in lower_line or "start" in lower_line:
                # Check for target dates
                for date_str in target_dates:
                    if date_str in lower_line:
                        started_projects.add(current_project)
                        break

total_funding = 0
for p in started_projects:
    total_funding += int(funding_projects[p]['Amount'])

print("__RESULT__:")
print(json.dumps({
    "count": len(started_projects),
    "total_funding": total_funding,
    "projects": list(started_projects)
}))"""

env_args = {'var_function-call-1003584179187242714': 'file_storage/function-call-1003584179187242714.json', 'var_function-call-1003584179187241629': 'file_storage/function-call-1003584179187241629.json'}

exec(code, env_args)

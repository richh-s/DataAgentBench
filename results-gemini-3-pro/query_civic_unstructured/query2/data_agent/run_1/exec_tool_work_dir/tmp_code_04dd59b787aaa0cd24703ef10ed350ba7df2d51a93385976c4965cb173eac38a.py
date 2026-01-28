code = """import json
import re

# Load data
with open(locals()['var_function-call-11007729145767623025'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-2656858989978563996'], 'r') as f:
    civic_docs_data = json.load(f)

# Process Funding
project_funding = {}
for record in funding_data:
    p_name = record['Project_Name']
    amount = int(record['Amount'])
    if p_name in project_funding:
        project_funding[p_name] += amount
    else:
        project_funding[p_name] = amount

project_names = list(project_funding.keys())

# Combine texts
text_list = [doc['text'] for doc in civic_docs_data]
# Use chr(10) for newline to avoid escaping issues
total_text = chr(10).join(text_list)

# Find projects
def find_projects(text, p_names):
    occurrences = []
    for p_name in p_names:
        start = 0
        while True:
            idx = text.find(p_name, start)
            if idx == -1:
                break
            occurrences.append((idx, p_name))
            start = idx + len(p_name)
    
    occurrences.sort()
    
    segments = []
    for i in range(len(occurrences)):
        start, name = occurrences[i]
        end = occurrences[i+1][0] if i+1 < len(occurrences) else len(text)
        segment = text[start:end]
        segments.append((name, segment))
    return segments

segments = find_projects(total_text, project_names)

completed_park_projects = set()
debug_info = []

for p_name, segment in segments:
    if 'park' in p_name.lower():
        # Check completion in 2022
        # regex: completed ... 2022
        match = re.search(r'completed.{0,50}2022', segment, re.IGNORECASE)
        if match:
            completed_park_projects.add(p_name)
            debug_info.append(p_name)

total = 0
for p in completed_park_projects:
    total += project_funding[p]

print("__RESULT__:")
print(json.dumps({'total': total, 'projects': list(completed_park_projects), 'debug': debug_info}))"""

env_args = {'var_function-call-4881455227376236038': ['civic_docs'], 'var_function-call-4881455227376238215': ['Funding'], 'var_function-call-11007729145767623596': 'file_storage/function-call-11007729145767623596.json', 'var_function-call-11007729145767623025': 'file_storage/function-call-11007729145767623025.json', 'var_function-call-12661878134790433858': 'file_storage/function-call-12661878134790433858.json', 'var_function-call-2656858989978563996': 'file_storage/function-call-2656858989978563996.json'}

exec(code, env_args)

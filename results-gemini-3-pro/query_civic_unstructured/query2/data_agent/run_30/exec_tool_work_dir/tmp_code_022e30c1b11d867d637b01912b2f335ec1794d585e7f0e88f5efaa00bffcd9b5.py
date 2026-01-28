code = """import json
import re

# Load Data
with open(locals()['var_function-call-3018582044476684640'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-3018582044476683837'], 'r') as f:
    civic_docs = json.load(f)

full_text = "\n".join([d['text'] for d in civic_docs])
lines = full_text.split('\n')

project_starts = []
keywords = ["Updates:", "Project Description:", "Project Schedule:"]

for i, line in enumerate(lines):
    l_strip = line.strip()
    # Check if this line is a keyword line (often starts with bullet)
    is_keyword_line = False
    for kw in keywords:
        if kw in l_strip:
            is_keyword_line = True
            break
    
    if is_keyword_line:
        # Look for project name in previous non-empty line
        prev = i - 1
        while prev >= 0 and not lines[prev].strip():
            prev -= 1
        
        if prev >= 0:
            # This line 'prev' is the candidate project name
            p_name = lines[prev].strip()
            # Heuristics to avoid garbage
            if len(p_name) < 150 and "Page" not in p_name and "Item" not in p_name:
                project_starts.append((prev, p_name))

# Remove duplicates based on index
project_starts = sorted(list(set(project_starts)), key=lambda x: x[0])

# Extract content
parsed_projects = []
for k in range(len(project_starts)):
    start_idx, name = project_starts[k]
    # content goes until next start
    if k < len(project_starts) - 1:
        end_idx = project_starts[k+1][0]
    else:
        end_idx = len(lines)
    
    content = "\n".join(lines[start_idx:end_idx])
    parsed_projects.append({"name": name, "text": content})

# Filter
target_projects = set()

for p in parsed_projects:
    name = p['name']
    text = p['text'].lower()
    name_lower = name.lower()
    
    # Topic Check
    if "park" in name_lower or "park" in text:
        # Status Check: Completed in 2022
        # We look for "completed" and "2022" in close proximity
        # Or specifically "Construction was completed [Month] 2022"
        # Regex: completed.{0,100}2022
        
        if re.search(r"completed.{0,100}2022", text, re.DOTALL):
            target_projects.add(name)
        elif re.search(r"completion.{0,100}2022", text, re.DOTALL):
            target_projects.add(name)

# Sum Funding
total_funding = 0
matched_list = []

for row in funding_data:
    if row['Project_Name'] in target_projects:
        total_funding += int(row['Amount'])
        matched_list.append(row['Project_Name'])

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_list}))"""

env_args = {'var_function-call-3018582044476684640': 'file_storage/function-call-3018582044476684640.json', 'var_function-call-3018582044476683837': 'file_storage/function-call-3018582044476683837.json'}

exec(code, env_args)

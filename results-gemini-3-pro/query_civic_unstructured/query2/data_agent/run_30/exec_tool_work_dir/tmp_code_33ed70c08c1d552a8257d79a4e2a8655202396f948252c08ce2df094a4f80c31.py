code = """import json
import re

# Load Data
with open(locals()['var_function-call-3018582044476684640'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-3018582044476683837'], 'r') as f:
    civic_docs = json.load(f)

# Join with newline using chr(10) to avoid JSON escaping issues
full_text = chr(10).join([d['text'] for d in civic_docs])
lines = full_text.split(chr(10))

project_starts = []
keywords = ["Updates:", "Project Description:", "Project Schedule:"]

for i, line in enumerate(lines):
    l_strip = line.strip()
    is_keyword_line = False
    for kw in keywords:
        if kw in l_strip:
            is_keyword_line = True
            break
    
    if is_keyword_line:
        # Check previous line
        prev = i - 1
        while prev >= 0 and not lines[prev].strip():
            prev -= 1
        if prev >= 0:
            p_name = lines[prev].strip()
            # Basic filters
            if len(p_name) < 150 and "Page" not in p_name and "Item" not in p_name:
                project_starts.append((prev, p_name))

# Deduplicate
project_starts = sorted(list(set(project_starts)), key=lambda x: x[0])

# Extract
parsed_projects = []
for k in range(len(project_starts)):
    start_idx, name = project_starts[k]
    if k < len(project_starts) - 1:
        end_idx = project_starts[k+1][0]
    else:
        end_idx = len(lines)
    
    content = chr(10).join(lines[start_idx:end_idx])
    parsed_projects.append({"name": name, "text": content})

# Filter
target_projects = set()
for p in parsed_projects:
    name = p['name']
    text = p['text'].lower()
    name_lower = name.lower()
    
    # Topic: park
    if "park" in name_lower or "park" in text:
        # Status: Completed in 2022
        # Use regex with raw string. In JSON "r'regex'" is fine if no backslashes needed.
        # But for 'completed...2022' we use wildcards.
        # We need dot to match newlines for 're.DOTALL'.
        # We can simulate DOTALL with [\s\S] or just passing the flag.
        
        # Pattern: completed followed by 2022 within some distance
        if "completed" in text and "2022" in text:
            # Check range
            idx_c = text.find("completed")
            idx_2 = text.find("2022", idx_c)
            if idx_2 != -1 and (idx_2 - idx_c) < 100:
                target_projects.add(name)
            else:
                 # Check "completion"
                 idx_comp = text.find("completion")
                 idx_2 = text.find("2022", idx_comp)
                 if idx_comp != -1 and idx_2 != -1 and (idx_2 - idx_comp) < 100:
                     target_projects.add(name)

# Funding
total_funding = 0
matched_projects = []
for row in funding_data:
    if row['Project_Name'] in target_projects:
        total_funding += int(row['Amount'])
        matched_projects.append(row['Project_Name'])

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-3018582044476684640': 'file_storage/function-call-3018582044476684640.json', 'var_function-call-3018582044476683837': 'file_storage/function-call-3018582044476683837.json'}

exec(code, env_args)

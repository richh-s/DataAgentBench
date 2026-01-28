code = """import json

with open(locals()['var_function-call-3018582044476683837'], 'r') as f:
    civic_docs = json.load(f)

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
        prev = i - 1
        while prev >= 0 and not lines[prev].strip():
            prev -= 1
        if prev >= 0:
            p_name = lines[prev].strip()
            if len(p_name) < 150 and "Page" not in p_name and "Item" not in p_name:
                project_starts.append((prev, p_name))

project_starts = sorted(list(set(project_starts)), key=lambda x: x[0])

park_projects = []

for k in range(len(project_starts)):
    start_idx, name = project_starts[k]
    if k < len(project_starts) - 1:
        end_idx = project_starts[k+1][0]
    else:
        end_idx = len(lines)
    
    content = chr(10).join(lines[start_idx:end_idx])
    
    if "park" in name.lower() or "park" in content.lower():
        park_projects.append({"name": name, "content": content[:500]}) # Inspect first 500 chars

print("__RESULT__:")
print(json.dumps(park_projects))"""

env_args = {'var_function-call-3018582044476684640': 'file_storage/function-call-3018582044476684640.json', 'var_function-call-3018582044476683837': 'file_storage/function-call-3018582044476683837.json', 'var_function-call-8938805927192840560': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}}

exec(code, env_args)

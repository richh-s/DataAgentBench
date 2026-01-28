code = """import json

path_civic = locals()['var_function-call-16246873831533624735']

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

dates_found = []
projects_count = 0
all_dates = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    project_indices = []
    
    for i, line in enumerate(lines):
        if '(cid:190)' in line:
            k = i - 1
            while k >= 0:
                stripped = lines[k].strip()
                if stripped:
                    project_indices.append((k, stripped))
                    break
                k -= 1
    
    projects_count += len(project_indices)
    
    for j in range(len(project_indices)):
        start_line_idx, p_name = project_indices[j]
        
        if j < len(project_indices) - 1:
            end_line_idx = project_indices[j+1][0]
        else:
            end_line_idx = len(lines)
            
        block_lines = lines[start_line_idx:end_line_idx]
        
        for bl in block_lines:
            lbl = bl.lower()
            if "begin construction" in lbl or "start date" in lbl:
                 dates_found.append({"project": p_name, "line": bl.strip()})
            if "advertise" in lbl:
                 all_dates.append({"project": p_name, "line": bl.strip()})

# check for 'Spring 2022' in raw text
spring_hits = 0
for doc in civic_docs:
    if "Spring 2022" in doc['text'] or "spring 2022" in doc['text']:
        spring_hits += 1

result = {
    "projects_count": projects_count,
    "spring_hits_in_docs": spring_hits,
    "dates_found_sample": dates_found[:10],
    "advertise_sample": all_dates[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16246873831533624735': 'file_storage/function-call-16246873831533624735.json', 'var_function-call-7325626147316931914': 'file_storage/function-call-7325626147316931914.json', 'var_function-call-15565346498784014435': {'count': 0, 'total_funding': 0, 'projects': []}, 'var_function-call-13755215421253914261': 'debug done'}

exec(code, env_args)

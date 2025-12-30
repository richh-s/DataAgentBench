code = """import json

with open(locals()['var_function-call-17402731764388360423'], 'r') as f:
    civic_docs = json.load(f)

projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        is_header = True
        if "Agenda" in line or "Page" in line or line.startswith('('):
            is_header = False
        if "Capital Improvement Projects" in line:
            is_header = False
            
        is_project = False
        if is_header:
            for k in range(1, 6):
                if i + k < len(lines):
                    next_l = lines[i+k]
                    if "Updates:" in next_l or "Project Description:" in next_l or "Project Schedule:" in next_l or "Estimated Schedule:" in next_l:
                        is_project = True
                        break
        
        if is_project:
            p_name = line
            p_name_clean = " ".join(p_name.split())
            
            block_lines = []
            j = i + 1
            while j < len(lines):
                nl = lines[j]
                is_next_proj = False
                if not ("Agenda" in nl or "Page" in nl or nl.startswith('(') or "Capital Improvement Projects" in nl):
                     for m in range(1, 6):
                        if j + m < len(lines):
                            nnl = lines[j+m]
                            if "Updates:" in nnl or "Project Description:" in nnl or "Project Schedule:" in nnl or "Estimated Schedule:" in nnl:
                                is_next_proj = True
                                break
                
                if is_next_proj:
                    break
                
                block_lines.append(nl)
                j += 1
            
            block_text = " ".join(block_lines)
            
            is_completed = "completed" in block_text.lower()
            is_2022 = False
            if is_completed:
                sentences = block_text.split('.')
                for s in sentences:
                    if "completed" in s.lower() and "2022" in s:
                        is_2022 = True
                        break
            
            if is_completed and is_2022:
                projects_2022.append({"name": p_name_clean, "text": block_text})
            
            i = j
        else:
            i += 1

print("__RESULT__:")
print(json.dumps(projects_2022))"""

env_args = {'var_function-call-17402731764388360423': 'file_storage/function-call-17402731764388360423.json', 'var_function-call-17402731764388360612': 'file_storage/function-call-17402731764388360612.json', 'var_function-call-5693258223734184505': {'matches': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}], 'total_funding': 21000}}

exec(code, env_args)

code = """import json
import pandas as pd

# Load funding data
funding_path = locals()['var_function-call-8628233454064463530']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic docs
civic_path = locals()['var_function-call-8628233454064463845']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

projects = []

for doc in civic_data:
    text = doc['text']
    lines = text.splitlines()
    
    current_project = None
    current_text = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        is_title = False
        if line and i + 2 < len(lines):
            l1 = lines[i+1].strip()
            l2 = lines[i+2].strip()
            if l1 == "" and (l2.startswith("(cid:190)") or l2.startswith("(cid:131)")):
                is_title = True
        
        if is_title:
            if current_project:
                projects.append({
                    "name": current_project,
                    "text": " ".join(current_text)
                })
            current_project = line
            current_text = []
            i += 1
        else:
            if current_project:
                current_text.append(line)
            i += 1
            
    if current_project:
        projects.append({
            "name": current_project,
            "text": " ".join(current_text)
        })

target_names = []
for p in projects:
    p_name = p['name']
    p_text = p['text'].lower()
    
    if "park" in p_name.lower():
        if "completed" in p_text and "2022" in p_text:
            words = p_text.split()
            found = False
            for idx, w in enumerate(words):
                if "completed" in w:
                    context = words[idx:idx+10]
                    if any("2022" in cw for cw in context):
                        found = True
                        break
            if found:
                target_names.append(p_name)

merged = funding_df[funding_df['Project_Name'].isin(target_names)]
merged['Amount'] = pd.to_numeric(merged['Amount'])
total = int(merged['Amount'].sum())

print("__RESULT__:")
print(json.dumps({"projects": target_names, "total_funding": total}))"""

env_args = {'var_function-call-8628233454064463530': 'file_storage/function-call-8628233454064463530.json', 'var_function-call-8628233454064463845': 'file_storage/function-call-8628233454064463845.json'}

exec(code, env_args)

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
    lines = text.split('\n')
    
    current_project = None
    current_text = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for project title pattern: Line, Blank Line, Line starting with (cid:190)
        is_title = False
        if line and i + 2 < len(lines):
            l1 = lines[i+1].strip()
            l2 = lines[i+2].strip()
            if l1 == "" and (l2.startswith("(cid:190)") or l2.startswith("(cid:131)")):
                is_title = True
        
        if is_title:
            # Save previous project
            if current_project:
                projects.append({
                    "name": current_project,
                    "text": " ".join(current_text)
                })
            current_project = line
            current_text = []
            i += 1 # skip to next line (the blank one)
        else:
            if current_project:
                current_text.append(line)
            i += 1
            
    # Add last project
    if current_project:
        projects.append({
            "name": current_project,
            "text": " ".join(current_text)
        })

# Filter
target_names = []
for p in projects:
    p_name = p['name']
    p_text = p['text'].lower()
    
    # Check if park
    if "park" in p_name.lower():
        # Check completed in 2022
        if "completed" in p_text and "2022" in p_text:
            # Verify context?
            # "completed November 2022"
            # "completed, November 2022"
            # Let's assume if both words appear, it's a strong candidate, but verify strict proximity if needed.
            # But earlier Regex failed, so let's check proximity manually.
            words = p_text.split()
            found = False
            for idx, w in enumerate(words):
                if "completed" in w: # "completed," or "completed"
                    # Check next few words for 2022
                    context = words[idx:idx+5]
                    if any("2022" in cw for cw in context):
                        found = True
                        break
            if found:
                target_names.append(p_name)

# Join with funding
merged = funding_df[funding_df['Project_Name'].isin(target_names)]
merged['Amount'] = pd.to_numeric(merged['Amount'])
total = merged['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"projects": target_names, "total_funding": total}))"""

env_args = {'var_function-call-8628233454064463530': 'file_storage/function-call-8628233454064463530.json', 'var_function-call-8628233454064463845': 'file_storage/function-call-8628233454064463845.json'}

exec(code, env_args)

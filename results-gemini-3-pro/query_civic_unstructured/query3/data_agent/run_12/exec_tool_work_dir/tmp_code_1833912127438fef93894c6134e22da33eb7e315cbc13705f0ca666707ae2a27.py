code = """import json
import re

# Load data
funding_path = locals()['var_function-call-11245625895433682474']
docs_path = locals()['var_function-call-11245625895433679723']

with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

full_text_lines = []
for doc in civic_docs:
    # Use splitlines to avoid escape char issues
    full_text_lines.extend(doc['text'].splitlines())

projects_extracted = {} 
current_status = "unknown"
current_type = "capital"
capture_mode = False

current_project_name = None
current_project_text = []

ignore_lines = ["Public Works Commission", "Agenda Report", "Page ", "Agenda Item", "Prepared by", "Approved by", "Subject:", "RECOMMENDED ACTION", "DISCUSSION"]

def save_project(name, status, text_lines, p_type):
    if name and name not in projects_extracted:
        full_text = " ".join(text_lines)
        final_status = status
        # Refine status based on text content
        ft_lower = full_text.lower()
        if status == "construction":
            if "construction was completed" in ft_lower or "notice of completion" in ft_lower:
                final_status = "completed"
            elif "project is currently under construction" in ft_lower:
                 final_status = "construction"
        
        projects_extracted[name] = {
            "status": final_status,
            "text": full_text,
            "type": p_type
        }

for line in full_text_lines:
    line_stripped = line.strip()
    if not line_stripped:
        continue
        
    if "Capital Improvement Projects (Design)" in line:
        current_status = "design"
        capture_mode = True
        current_project_name = None
        continue
    elif "Capital Improvement Projects (Construction)" in line:
        current_status = "construction"
        capture_mode = True
        current_project_name = None
        continue
    elif "Capital Improvement Projects (Not Started)" in line:
        current_status = "not started"
        capture_mode = True
        current_project_name = None
        continue
    elif "Disaster Recovery Projects" in line:
        current_status = "design" # Assumption
        current_type = "disaster"
        capture_mode = True
        current_project_name = None
        continue
        
    if not capture_mode:
        continue
        
    if any(x in line for x in ignore_lines) or re.match(r'Page \d+ of \d+', line):
        continue
        
    if line_stripped.startswith("(cid:190)") or line_stripped.startswith("(cid:131)"):
        if current_project_name:
            current_project_text.append(line_stripped)
    else:
        if current_project_name:
            save_project(current_project_name, current_status, current_project_text, current_type)
        current_project_name = line_stripped
        current_project_text = []

if current_project_name:
    save_project(current_project_name, current_status, current_project_text, current_type)

results = []
keywords = ['emergency', 'fema']

def get_status_from_extracted(f_name):
    if f_name in projects_extracted:
        return projects_extracted[f_name]
    
    base_name = re.sub(r'\s*\((FEMA|CalOES|CalJPIA|FEMA/CalOES).*?\)', '', f_name).strip()
    if base_name in projects_extracted:
        return projects_extracted[base_name]
    
    candidates = []
    for k in projects_extracted:
        if k in f_name:
            candidates.append(k)
    if candidates:
        best = max(candidates, key=len)
        return projects_extracted[best]
        
    return None

for record in funding:
    p_name = record['Project_Name']
    p_source = record['Funding_Source']
    p_amount = record['Amount']
    
    is_related = False
    if any(k in p_name.lower() for k in keywords):
        is_related = True
        
    info = get_status_from_extracted(p_name)
    
    if info:
        if any(k in info['text'].lower() for k in keywords):
            is_related = True
            
    if is_related:
        status = info['status'] if info else "not started"
        results.append({
            "Project_Name": p_name,
            "Funding_Source": p_source,
            "Amount": p_amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11245625895433682474': 'file_storage/function-call-11245625895433682474.json', 'var_function-call-11245625895433679723': 'file_storage/function-call-11245625895433679723.json'}

exec(code, env_args)

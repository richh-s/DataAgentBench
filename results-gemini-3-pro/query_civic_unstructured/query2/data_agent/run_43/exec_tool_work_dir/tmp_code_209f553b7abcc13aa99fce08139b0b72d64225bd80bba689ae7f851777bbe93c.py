code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-14368692439626518277'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs Data
with open(locals()['var_function-call-10213598713218167790'], 'r') as f:
    civic_docs = json.load(f)

park_keywords = ["park", "playground", "recreation", "trail", "open space", "walkway"] 

completed_projects = set()

for doc in civic_docs:
    text = doc['text']
    # Use splitlines to avoid escape issues
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    projects = []
    current_proj_name = None
    current_proj_text = []
    
    for line in lines:
        if "Capital Improvement Projects" in line:
            continue
        
        # Skip metadata lines
        if "Agenda Item" in line or "Page " in line or line.startswith("To:") or line.startswith("From:") or line.startswith("Subject:"):
            continue
            
        # Check for Project Start
        # Not starting with (cid:, not starting with keywords
        if not line.startswith("(cid:") and not line.startswith("Updates:") and not line.startswith("Project Schedule:") and not line.startswith("Project Description:") and not line.startswith("Complete Construction:") and not line.startswith("Begin Construction:"):
            if current_proj_name:
                projects.append({'name': current_proj_name, 'text': " ".join(current_proj_text)})
            
            current_proj_name = line
            current_proj_text = []
        else:
            if current_proj_name:
                current_proj_text.append(line)
    
    if current_proj_name:
        projects.append({'name': current_proj_name, 'text': " ".join(current_proj_text)})

    for p in projects:
        p_name = p['name']
        p_text = p['text'].lower()
        
        # Check park
        is_park = False
        if any(k in p_name.lower() for k in park_keywords):
            is_park = True
        
        # Check completed 2022
        is_completed_2022 = False
        
        # Patterns
        # (cid:190) Updates: Construction was completed November 2022
        # (cid:131) Construction was completed, November 2022
        
        if "completed" in p_text and "2022" in p_text:
            if "construction was completed" in p_text:
                is_completed_2022 = True
            elif "notice of completion" in p_text and "2023" in p_text:
                 # Notice of completion in Jan 2023 often means completed in late 2022. 
                 # But text usually says "Construction was completed...".
                 pass
            
            # Regex verify
            # completed [month] 2022
            if re.search(r"completed[,]?\s+\w+\s+2022", p_text):
                is_completed_2022 = True

        if is_park and is_completed_2022:
            completed_projects.add(p_name)

# Match Funding
total_funding = 0
matched_records = []
target_names = {n.strip() for n in completed_projects}

for record in funding_data:
    r_name = record['Project_Name'].strip()
    if r_name in target_names:
        total_funding += int(record['Amount'])
        matched_records.append(record)

print("__RESULT__:")
print(json.dumps({
    "target_projects": list(target_names),
    "total_funding": total_funding,
    "matched_records": matched_records
}))"""

env_args = {'var_function-call-2808116990881149214': ['Funding'], 'var_function-call-2808116990881151343': ['civic_docs'], 'var_function-call-14368692439626518277': 'file_storage/function-call-14368692439626518277.json', 'var_function-call-14368692439626518412': 'file_storage/function-call-14368692439626518412.json', 'var_function-call-10213598713218167790': 'file_storage/function-call-10213598713218167790.json'}

exec(code, env_args)

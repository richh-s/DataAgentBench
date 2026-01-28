code = """import json
import re

with open(locals()['var_function-call-10213598713218167790'], 'r') as f:
    civic_docs = json.load(f)

park_keywords = ["park", "playground", "recreation", "trail", "open space", "walkway"] 

results = []

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    current_proj_name = None
    current_proj_text = []
    
    # Same extraction logic
    for line in lines:
        if "Capital Improvement Projects" in line: continue
        if "Agenda Item" in line or "Page " in line or line.startswith("To:") or line.startswith("Subject:"): continue
            
        if not line.startswith("(cid:") and not line.startswith("Updates:") and not line.startswith("Project Schedule:") and not line.startswith("Project Description:") and not line.startswith("Complete Construction:") and not line.startswith("Begin Construction:"):
            if current_proj_name:
                # Process previous
                is_park = any(k in current_proj_name.lower() for k in park_keywords)
                if is_park:
                    results.append({"name": current_proj_name, "text_snippet": " ".join(current_proj_text)[:300]})
            
            current_proj_name = line
            current_proj_text = []
        else:
            if current_proj_name:
                current_proj_text.append(line)
    
    if current_proj_name:
        is_park = any(k in current_proj_name.lower() for k in park_keywords)
        if is_park:
            results.append({"name": current_proj_name, "text_snippet": " ".join(current_proj_text)[:300]})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2808116990881149214': ['Funding'], 'var_function-call-2808116990881151343': ['civic_docs'], 'var_function-call-14368692439626518277': 'file_storage/function-call-14368692439626518277.json', 'var_function-call-14368692439626518412': 'file_storage/function-call-14368692439626518412.json', 'var_function-call-10213598713218167790': 'file_storage/function-call-10213598713218167790.json', 'var_function-call-17278520441771362203': {'target_projects': ['Point Dume Walkway Repairs', 'Bluffs Park Shade Structure'], 'total_funding': 80000, 'matched_records': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '79', 'Project_Name': 'Point Dume Walkway Repairs', 'Funding_Source': 'International Aid', 'Amount': '59000'}]}}

exec(code, env_args)

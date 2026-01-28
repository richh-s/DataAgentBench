code = """import json
import re

# Load data
with open(locals()['var_function-call-6833374196738575429'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2571732605933953840'], 'r') as f:
    civic_docs = json.load(f)

projects_started_spring_2022 = set()

def is_spring_2022(date_str):
    if not date_str:
        return False
    ds = date_str.lower()
    if "spring 2022" in ds or "spring, 2022" in ds:
        return True
    if "2022" in ds:
        if "march" in ds or "april" in ds or "may" in ds:
            return True
    return False

# Parse documents
for doc in civic_docs:
    text = doc["text"]
    lines = text.split("\n")
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Use double quotes. Check for (cid:190) as a string.
        if "(cid:190)" in line or line.startswith("Updates:") or "Project Schedule:" in line:
            # Look backwards for project name
            project_name = None
            for k in range(i-1, -1, -1):
                prev_line = lines[k].strip()
                if prev_line:
                    if "Capital Improvement Projects" in prev_line or "Agenda" in prev_line:
                        break
                    project_name = prev_line
                    break
            
            if project_name:
                # Look forward for start date
                block_text = ""
                for j in range(i, min(i+50, len(lines))):
                    block_text += lines[j].strip() + " "
                
                # Regex for Begin Construction
                # Avoid single quotes in regex if possible or just be careful
                match = re.search("Begin\\s+Construction:?\\s*([^,.\n]*)", block_text, re.IGNORECASE)
                if match:
                    date_val = match.group(1).strip()
                    if is_spring_2022(date_val):
                        projects_started_spring_2022.add(project_name)

total_funding = 0
funded_projects = []

def clean_name(n):
    return re.sub(r"\s+", " ", n).strip().lower()

funding_map = {clean_name(r["Project_Name"]): int(r["Amount"]) for r in funding_data}
funding_keys = list(funding_map.keys())

matched_projects = set()

for p_name in projects_started_spring_2022:
    cn = clean_name(p_name)
    
    amount = 0
    match_found = False
    
    if cn in funding_map:
        amount = funding_map[cn]
        match_found = True
    else:
        for k in funding_keys:
            if k in cn or cn in k:
                amount = funding_map[k]
                match_found = True
                break
    
    if match_found:
        if p_name not in matched_projects:
            total_funding += amount
            funded_projects.append(p_name)
            matched_projects.add(p_name)

result = {
    "count": len(funded_projects),
    "total_funding": total_funding,
    "projects": funded_projects,
    "debug_extracted": list(projects_started_spring_2022)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3413924578737441379': ['civic_docs'], 'var_function-call-3413924578737439684': ['Funding'], 'var_function-call-6833374196738575429': 'file_storage/function-call-6833374196738575429.json', 'var_function-call-6833374196738572946': 'file_storage/function-call-6833374196738572946.json', 'var_function-call-2571732605933953840': 'file_storage/function-call-2571732605933953840.json'}

exec(code, env_args)

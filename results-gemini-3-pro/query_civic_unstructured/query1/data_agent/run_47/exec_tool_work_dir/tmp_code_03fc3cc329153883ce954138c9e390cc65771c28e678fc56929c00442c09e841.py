code = """import json
import pandas as pd

# Load Funding data
with open(locals()["var_function-call-12574336957284000911"], "r") as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding["Amount"] = pd.to_numeric(df_funding["Amount"])

# Load Civic Docs data
with open(locals()["var_function-call-12574336957284002122"], "r") as f:
    civic_docs = json.load(f)

design_projects = []

for doc in civic_docs:
    text = doc.get("text", "")
    
    start_marker = "Capital Improvement Projects (Design)"
    end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"]
    
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
        
    end_idx = len(text)
    for marker in end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx + len(start_marker):end_idx]
    lines = section_text.splitlines()
    clean_lines = [line.strip() for line in lines if line.strip()]
    
    for i, line in enumerate(clean_lines):
        if line.startswith("(cid:") or line.startswith("Page ") or "Agenda Item" in line:
            continue
            
        if i + 1 < len(clean_lines):
            next_line = clean_lines[i+1]
            if "Updates" in next_line or "Project Description" in next_line:
                name = line.strip()
                if len(name) < 5 or "Meeting" in name:
                    continue
                design_projects.append(name)

design_projects = list(set(design_projects))
print("Identified Design Projects:", design_projects)

count = 0
for proj in design_projects:
    total = df_funding[df_funding["Project_Name"] == proj]["Amount"].sum()
    if total > 50000:
        count += 1

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-16012235446979576453': ['civic_docs'], 'var_function-call-16012235446979577650': ['Funding'], 'var_function-call-12574336957284000911': 'file_storage/function-call-12574336957284000911.json', 'var_function-call-12574336957284002122': 'file_storage/function-call-12574336957284002122.json'}

exec(code, env_args)

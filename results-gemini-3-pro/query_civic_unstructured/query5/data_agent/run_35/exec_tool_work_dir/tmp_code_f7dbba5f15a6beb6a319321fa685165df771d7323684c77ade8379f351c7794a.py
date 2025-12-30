code = """import json
import re

key_civic = "var_function-call-6738799764007294516"
key_funding = "var_function-call-6738799764007295879"

path_civic = locals()[key_civic]
path_funding = locals()[key_funding]

with open(path_civic, "r") as f:
    civic_docs = json.load(f)

with open(path_funding, "r") as f:
    funding_data = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc.get("text", "")
    lines = text.splitlines()
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        is_title = False
        look_ahead_range = 5
        for j in range(1, look_ahead_range + 1):
            if i + j < len(lines):
                next_line = lines[i+j].strip()
                # Check for keywords indicating a project block start
                # avoiding regex for simplicity with quotes
                if "Updates:" in next_line or "Project Description:" in next_line or "Project Updates:" in next_line:
                    is_title = True
                    break
        
        if is_title:
            if current_project:
                extracted_projects.append(current_project)
            current_project = {"name": line, "text_lines": []}
        else:
            if current_project:
                current_project["text_lines"].append(line)
    
    if current_project:
        extracted_projects.append(current_project)

total_funding = 0
included_projects = []

for proj in extracted_projects:
    full_text = " ".join(proj["text_lines"])
    
    # Extract Start Date
    start_date_str = ""
    # Simple search
    idx = full_text.find("Begin Construction:")
    if idx != -1:
        start_date_str = full_text[idx:idx+50]
    else:
        idx = full_text.find("Begin construction:")
        if idx != -1:
            start_date_str = full_text[idx:idx+50]
            
    started_in_2022 = False
    if "2022" in start_date_str:
        started_in_2022 = True
        
    # Check for Disaster related
    is_disaster = False
    disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Recovery"]
    
    if any(k.lower() in proj["name"].lower() for k in disaster_keywords):
        is_disaster = True
    if any(k in full_text for k in disaster_keywords):
        is_disaster = True
        
    if started_in_2022 and is_disaster:
        # Calculate Funding
        proj_funding = 0
        
        # Look for matches in funding data
        # Normalize name
        p_name = proj["name"].strip()
        
        # Exact match
        for frec in funding_data:
            f_name = frec["Project_Name"].strip()
            # Check exact match
            if f_name == p_name:
                proj_funding += int(frec["Amount"])
            # Check suffix match
            # "Project Name (Suffix)"
            elif f_name.startswith(p_name + " ("):
                proj_funding += int(frec["Amount"])
        
        if proj_funding > 0:
            total_funding += proj_funding
            included_projects.append({
                "name": p_name,
                "funding": proj_funding,
                "start": start_date_str
            })

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": included_projects}))"""

env_args = {'var_function-call-6738799764007294516': 'file_storage/function-call-6738799764007294516.json', 'var_function-call-6738799764007295879': 'file_storage/function-call-6738799764007295879.json'}

exec(code, env_args)

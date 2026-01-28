code = """import json

# Load data
with open(locals()['var_function-call-12303763025634533980'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-12303763025634534281'], 'r') as f:
    civic_docs = json.load(f)

def normalize(name):
    return name.lower().strip().replace("’", "'")

funding_projects = []
for entry in funding_data:
    name = entry['Project_Name']
    norm_name = normalize(name)
    is_fema_related = "fema" in norm_name or "emergency" in norm_name
    funding_projects.append({
        "original": entry,
        "norm_name": norm_name,
        "is_fema_related": is_fema_related
    })

extracted_projects = []
status_map = {
    "design": "design",
    "construction": "construction",
    "not started": "not started"
}
current_section_status = None

for doc in civic_docs:
    text = doc['text']
    lines = text.split(chr(10))
    
    current_project_name = None
    current_project_text = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if "Capital Improvement Projects (" in line:
            if current_project_name:
                extracted_projects.append({
                    "name": current_project_name,
                    "status_category": current_section_status,
                    "text": chr(10).join(current_project_text)
                })
                current_project_name = None
                current_project_text = []
            
            lower_line = line.lower()
            if "design" in lower_line:
                current_section_status = "design"
            elif "construction" in lower_line:
                current_section_status = "construction"
            elif "not started" in lower_line:
                current_section_status = "not started"
            else:
                current_section_status = "unknown"
            continue
        
        k1 = ["Updates:", "Project Schedule:", "Project Description:", "Page ", "Agenda Item"]
        k2 = ["To:", "Prepared by:", "Approved by:", "Subject:", "Date prepared:"]
        k3 = ["Meeting date:", "RECOMMENDED ACTION:", "DISCUSSION:", "Capital Improvement Projects", "item", "commission meeting"]
        skip_keywords = k1 + k2 + k3
        
        is_keyword = any(k.lower() in line.lower() for k in skip_keywords)
        is_bullet = line.startswith("(") or (len(line) > 0 and ord(line[0]) == 12)
        
        if current_section_status and not is_keyword and not is_bullet and len(line) > 5:
            is_proj_name = False
            for next_line in lines[i+1:]:
                next_line = next_line.strip()
                if not next_line:
                    continue
                if "Updates" in next_line or "Project Description" in next_line or next_line.startswith("(cid"):
                    is_proj_name = True
                break
            
            if is_proj_name:
                if current_project_name:
                    extracted_projects.append({
                        "name": current_project_name,
                        "status_category": current_section_status,
                        "text": chr(10).join(current_project_text)
                    })
                
                current_project_name = line
                current_project_text = []
                continue

        if current_project_name:
            current_project_text.append(line)

    if current_project_name:
        extracted_projects.append({
            "name": current_project_name,
            "status_category": current_section_status,
            "text": chr(10).join(current_project_text)
        })

results = []
matched_funding_indices = set()

for proj in extracted_projects:
    p_name = proj['name']
    p_text = proj['text'].lower()
    p_norm = normalize(p_name)
    
    is_related = "fema" in p_text or "emergency" in p_text or "fema" in p_norm or "emergency" in p_norm
    
    funding_match = None
    for idx, fp in enumerate(funding_projects):
        if p_norm == fp['norm_name'] or fp['norm_name'].startswith(p_norm):
             funding_match = fp['original']
             matched_funding_indices.add(idx)
             break
    
    if funding_match:
        f_name_norm = normalize(funding_match['Project_Name'])
        if "fema" in f_name_norm or "emergency" in f_name_norm:
            is_related = True
            
    if is_related:
        status = proj['status_category']
        if status == "construction":
            if "completed" in p_text and "construction was completed" in p_text:
                status = "completed"
            elif "under construction" in p_text:
                status = "construction" 
            if "notice of completion" in p_text:
                status = "completed"

        results.append({
            "Project_Name": p_name,
            "Funding_Source": funding_match['Funding_Source'] if funding_match else None,
            "Amount": funding_match['Amount'] if funding_match else None,
            "Status": status
        })

for idx, fp in enumerate(funding_projects):
    if idx not in matched_funding_indices and fp['is_fema_related']:
        results.append({
            "Project_Name": fp['original']['Project_Name'],
            "Funding_Source": fp['original']['Funding_Source'],
            "Amount": fp['original']['Amount'],
            "Status": "Unknown"
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16622059259501542198': ['Funding'], 'var_function-call-16622059259501542215': ['civic_docs'], 'var_function-call-3040997018406236735': 'file_storage/function-call-3040997018406236735.json', 'var_function-call-3040997018406238616': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-12303763025634533980': 'file_storage/function-call-12303763025634533980.json', 'var_function-call-12303763025634534281': 'file_storage/function-call-12303763025634534281.json'}

exec(code, env_args)

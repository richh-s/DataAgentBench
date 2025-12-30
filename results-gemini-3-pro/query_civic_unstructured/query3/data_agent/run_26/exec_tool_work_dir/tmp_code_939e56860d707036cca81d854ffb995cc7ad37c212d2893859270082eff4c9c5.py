code = """import json

# Load data
with open(locals()['var_function-call-12303763025634533980'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-12303763025634534281'], 'r') as f:
    civic_docs = json.load(f)

def normalize(name):
    return name.lower().strip().replace("’", "'")

keywords = ["fema", "emergency", "caloes", "caljpia", "disaster", "fire"]

funding_projects = []
for entry in funding_data:
    name = entry['Project_Name']
    norm_name = normalize(name)
    is_related = any(k in norm_name for k in keywords)
    funding_projects.append({
        "original": entry,
        "norm_name": norm_name,
        "is_related": is_related
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
    
    is_related = any(k in p_text for k in keywords) or any(k in p_norm for k in keywords)
    
    funding_match = None
    for idx, fp in enumerate(funding_projects):
        if p_norm == fp['norm_name'] or fp['norm_name'].startswith(p_norm):
             funding_match = fp['original']
             matched_funding_indices.add(idx)
             break
    
    if funding_match and funding_match.get('is_related'):
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
    if idx not in matched_funding_indices and fp['is_related']:
        results.append({
            "Project_Name": fp['original']['Project_Name'],
            "Funding_Source": fp['original']['Funding_Source'],
            "Amount": fp['original']['Amount'],
            "Status": "Unknown"
        })

# Clean
cleaned = {}
status_priority = {
    "completed": 5,
    "construction": 4,
    "design": 3,
    "not started": 2,
    "unknown": 1,
    "Unknown": 1
}

for r in results:
    name = r['Project_Name']
    # Filter noise
    if len(name) < 5 or name.strip() == "Project)" or name.lower().startswith("a plan that includes"):
        continue
    
    status = r['Status']
    
    if name not in cleaned:
        cleaned[name] = r
    else:
        curr_p = status_priority.get(cleaned[name]['Status'], 0)
        new_p = status_priority.get(status, 0)
        if new_p > curr_p:
            cleaned[name] = r

final_list = list(cleaned.values())

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-16622059259501542198': ['Funding'], 'var_function-call-16622059259501542215': ['civic_docs'], 'var_function-call-3040997018406236735': 'file_storage/function-call-3040997018406236735.json', 'var_function-call-3040997018406238616': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-12303763025634533980': 'file_storage/function-call-12303763025634533980.json', 'var_function-call-12303763025634534281': 'file_storage/function-call-12303763025634534281.json', 'var_function-call-17901036195019998186': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000', 'Status': 'unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'unknown'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'not started'}, {'Project_Name': 'Project)', 'Funding_Source': None, 'Amount': None, 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'a plan that includes the evaluation of a siren system and possible locations.', 'Funding_Source': None, 'Amount': None, 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'a plan that includes the evaluation of a siren system and possible locations.', 'Funding_Source': None, 'Amount': None, 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'unknown'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'Unknown'}], 'var_function-call-7166261158105362311': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}], 'var_function-call-6860842330600921148': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000', 'Status': 'unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'unknown'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'Unknown'}]}

exec(code, env_args)

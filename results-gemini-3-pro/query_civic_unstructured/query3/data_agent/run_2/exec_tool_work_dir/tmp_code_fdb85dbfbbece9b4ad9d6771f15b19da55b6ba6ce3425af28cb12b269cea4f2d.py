code = """import json

# Load Funding Data
f_path = locals()['var_function-call-18338097190438491803']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
d_path = locals()['var_function-call-7592181240174987408']
with open(d_path, 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = chr(10).join([doc['text'] for doc in civic_docs])

# Sections
sections = [
    ("design", "Capital Improvement Projects (Design)"),
    ("construction", "Capital Improvement Projects (Construction)"),
    ("not started", "Capital Improvement Projects (Not Started)")
]

section_positions = []
for status, header in sections:
    idx = full_text.find(header)
    if idx != -1:
        section_positions.append({"status": status, "start": idx, "header": header})

section_positions.sort(key=lambda x: x['start'])

# Add end positions
for i in range(len(section_positions) - 1):
    section_positions[i]['end'] = section_positions[i+1]['start']
if section_positions:
    section_positions[-1]['end'] = len(full_text)

# Keywords to identify relevant projects
# Based on prompt and hints
keywords = ['emergency', 'fema', 'caloes', 'disaster', 'warning', 'fire']

# Find project occurrences
project_matches = []
for record in funding_data:
    p_name = record['Project_Name']
    idx = full_text.find(p_name)
    if idx != -1:
        status = "Unknown"
        for section in section_positions:
            if section['start'] <= idx < section['end']:
                status = section['status']
                break
        
        project_matches.append({
            "name": p_name,
            "idx": idx,
            "status": status,
            "funding_record": record
        })
    else:
        # Not found in text
        # Check if name has keywords
        if any(k in p_name.lower() for k in keywords):
             project_matches.append({
                "name": p_name,
                "idx": -1,
                "status": "not started", # Default for not found but relevant projects
                "funding_record": record
            })

# Sort matches
project_matches.sort(key=lambda x: x['idx'])

results = []
seen_projects = set() # To avoid exact duplicates if any

for i in range(len(project_matches)):
    match = project_matches[i]
    p_name = match['name']
    
    if p_name in seen_projects:
        continue
        
    if match['idx'] == -1:
        results.append({
            "Project_Name": p_name,
            "Funding_Source": match['funding_record']['Funding_Source'],
            "Amount": match['funding_record']['Amount'],
            "Status": match['status']
        })
        seen_projects.add(p_name)
        continue

    start = match['idx']
    
    # Determine end of text block
    next_idx = len(full_text)
    if i < len(project_matches) - 1:
        # Check subsequent matches
        for j in range(i+1, len(project_matches)):
            candidate = project_matches[j]['idx']
            if candidate > start:
                next_idx = candidate
                break
            # If candidate == start (overlapping/duplicate), skip it for boundary finding
            
    # Also clamp to section end
    current_section_end = len(full_text)
    for section in section_positions:
        if section['start'] <= start < section['end']:
            current_section_end = section['end']
            break
    
    end = min(next_idx, current_section_end)
    
    block = full_text[start:end]
    
    # Check keywords
    is_relevant = False
    if any(k in p_name.lower() for k in keywords):
        is_relevant = True
    elif any(k in block.lower() for k in keywords):
        is_relevant = True
        
    if is_relevant:
        final_status = match['status']
        block_lower = block.lower()
        if final_status == "construction":
            if "construction was completed" in block_lower or "notice of completion" in block_lower:
                final_status = "completed"
            # Else remains "construction"
        
        results.append({
            "Project_Name": p_name,
            "Funding_Source": match['funding_record']['Funding_Source'],
            "Amount": match['funding_record']['Amount'],
            "Status": final_status
        })
        seen_projects.add(p_name)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8827426620448851046': ['civic_docs'], 'var_function-call-8827426620448850527': ['Funding'], 'var_function-call-6655663227324629394': 'file_storage/function-call-6655663227324629394.json', 'var_function-call-7592181240174987408': 'file_storage/function-call-7592181240174987408.json', 'var_function-call-18338097190438491803': 'file_storage/function-call-18338097190438491803.json', 'var_function-call-2449875268920696225': [{'Project Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding Source': 'Local Business Support', 'Amount': '43000', 'Status': 'not started'}, {'Project Name': 'Clover Heights Storm Drain', 'Funding Source': 'Infrastructure Bond', 'Amount': '53000', 'Status': 'design'}, {'Project Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding Source': 'National Foundation Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding Source': 'Community Fund', 'Amount': '68000', 'Status': 'not started'}, {'Project Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project Name': 'Guardrail Replacement Citywide', 'Funding Source': 'International Aid', 'Amount': '39000', 'Status': 'not started'}, {'Project Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Road Bridge Repairs', 'Funding Source': 'Technology Innovation Fund', 'Amount': '68000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Culvert Repairs', 'Funding Source': 'Federal Assistance', 'Amount': '54000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project Name': 'Birdview Avenue Improvements', 'Funding Source': 'National Foundation Fund', 'Amount': '79000', 'Status': 'not started'}, {'Project Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Culvert Repairs', 'Funding Source': 'Community Fund', 'Amount': '57000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project Name': 'Encinal Canyon Road Drainage Improvements', 'Funding Source': 'Non-profit Organization Grant', 'Amount': '34000', 'Status': 'not started'}, {'Project Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project Name': 'Dume Drive and Fernhill Drive Speed Humps Project', 'Funding Source': 'Philanthropic Donation', 'Amount': '90000', 'Status': 'not started'}, {'Project Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project Name': 'Outdoor Warning Sirens', 'Funding Source': 'Social Impact Investment', 'Amount': '28000', 'Status': 'not started'}, {'Project Name': 'Outdoor Warning Sirens (FEMA)', 'Funding Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}]}

exec(code, env_args)

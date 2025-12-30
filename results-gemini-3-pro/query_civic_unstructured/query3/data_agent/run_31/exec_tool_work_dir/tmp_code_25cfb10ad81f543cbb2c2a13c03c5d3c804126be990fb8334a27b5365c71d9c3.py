code = """import json
import sqlite3
import re

# Load funding data
funding_file = locals()['var_function-call-10486156171359470717']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
docs_file = locals()['var_function-call-11751913869658535097']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = chr(10).join([d['text'] for d in civic_docs])

# Define statuses and sections
sections = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started"
}

def clean_name(name):
    # Remove suffixes like (FEMA Project), (CalOES Project)
    return re.sub(r'[ ' + chr(9) + ']*[(].*?[)]$', '', name).strip()

project_funding_map = {}
for record in funding_data:
    full_name = record['Project_Name']
    base_name = clean_name(full_name)
    if base_name not in project_funding_map:
        project_funding_map[base_name] = []
    project_funding_map[base_name].append(record)

section_positions = []
for header, status in sections.items():
    pattern = re.escape(header)
    for match in re.finditer(pattern, full_text, re.IGNORECASE):
        section_positions.append({'start': match.start(), 'name': header, 'status': status})

section_positions.sort(key=lambda x: x['start'])
section_positions.append({'start': len(full_text), 'name': 'END', 'status': None})

# Store found project info: base_name -> {status, is_relevant_text}
project_info = {}

all_base_names = list(project_funding_map.keys())
all_base_names.sort(key=len, reverse=True)

# Scan sections
for i in range(len(section_positions) - 1):
    section = section_positions[i]
    next_section = section_positions[i+1]
    
    section_text = full_text[section['start']:next_section['start']]
    section_status = section['status']
    
    # Find matches in this section
    matches = []
    for base_name in all_base_names:
        start = 0
        while True:
            idx = section_text.find(base_name, start)
            if idx == -1:
                break
            matches.append({'name': base_name, 'start': idx})
            start = idx + 1
            
    matches.sort(key=lambda x: (x['start'], -len(x['name'])))
    
    # Filter overlaps
    valid_matches = []
    last_end = -1
    for m in matches:
        if m['start'] >= last_end:
            valid_matches.append(m)
            last_end = m['start'] + len(m['name'])
    
    for k in range(len(valid_matches)):
        match = valid_matches[k]
        base_name = match['name']
        
        # If we already found this project in a previous section (e.g. Design), skip later mentions (e.g. Not Started)
        # This assumes the first mention is the primary status.
        if base_name in project_info:
            continue
            
        start = match['start']
        end_of_block = valid_matches[k+1]['start'] if k+1 < len(valid_matches) else len(section_text)
        
        # Validation
        following_text = section_text[start+len(base_name):start+len(base_name)+200]
        indicators = ["updates", "description", "schedule", "cid"]
        if not any(ind in following_text.lower() for ind in indicators):
            continue 
            
        block_text = section_text[start:end_of_block]
        
        status = section_status
        if status == "construction":
            lower_block = block_text.lower()
            if "construction was completed" in lower_block or "notice of completion" in lower_block:
                status = "completed"
        
        keywords = ['emergency', 'fema', 'fire', 'disaster', 'caloes', 'caljpia']
        is_relevant_text = any(kw in block_text.lower() for kw in keywords)
        
        project_info[base_name] = {
            'status': status,
            'is_relevant_text': is_relevant_text
        }

# Generate Results
results = []
keywords = ['emergency', 'fema', 'fire', 'disaster', 'caloes', 'caljpia']

for base_name, info in project_info.items():
    funding_records = project_funding_map.get(base_name, [])
    
    # Check if project is relevant (text or funding name)
    is_relevant_name = False
    for record in funding_records:
        if any(kw in record['Project_Name'].lower() for kw in keywords):
            is_relevant_name = True
            break
            
    if info['is_relevant_text'] or is_relevant_name:
        for record in funding_records:
            results.append({
                "Project Name": record['Project_Name'],
                "Funding Source": record['Funding_Source'],
                "Amount": record['Amount'],
                "Status": info['status']
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8394565906188942673': 'file_storage/function-call-8394565906188942673.json', 'var_function-call-10486156171359470717': 'file_storage/function-call-10486156171359470717.json', 'var_function-call-11751913869658535097': 'file_storage/function-call-11751913869658535097.json', 'var_function-call-16109786718814839838': 'file_storage/function-call-16109786718814839838.json', 'var_function-call-10633738942368961552': [{'Project Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'design'}, {'Project Name': 'City Traffic Signals Backup Power', 'Funding Source': 'Social Impact Investment', 'Amount': '85000', 'Status': 'not started'}, {'Project Name': '2021 Annual Street Maintenance', 'Funding Source': 'Public-Private Partnership (PPP)', 'Amount': '24000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding Source': 'National Foundation Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project Name': 'Storm Drain Master Plan', 'Funding Source': 'Social Impact Investment', 'Amount': '77000', 'Status': 'not started'}, {'Project Name': 'Guardrail Replacement Citywide', 'Funding Source': 'International Aid', 'Amount': '39000', 'Status': 'not started'}, {'Project Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Road Bridge Repairs', 'Funding Source': 'Technology Innovation Fund', 'Amount': '68000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Culvert Repairs', 'Funding Source': 'Federal Assistance', 'Amount': '54000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project Name': 'Clover Heights Storm Drain', 'Funding Source': 'Infrastructure Bond', 'Amount': '53000', 'Status': 'not started'}, {'Project Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Culvert Repairs', 'Funding Source': 'Community Fund', 'Amount': '57000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project Name': 'Encinal Canyon Road Drainage Improvements', 'Funding Source': 'Non-profit Organization Grant', 'Amount': '34000', 'Status': 'not started'}, {'Project Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding Source': 'Educational Sponsorship', 'Amount': '18000', 'Status': 'not started'}, {'Project Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project Name': 'Citywide Guardrail Replacement', 'Funding Source': 'Infrastructure Bond', 'Amount': '30000', 'Status': 'not started'}, {'Project Name': 'Malibu Park Storm Drain Repairs', 'Funding Source': 'Taxpayer Contribution', 'Amount': '50000', 'Status': 'not started'}, {'Project Name': 'Malibu Road Slope Repairs', 'Funding Source': 'Development Bank Loan', 'Amount': '44000', 'Status': 'not started'}, {'Project Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding Source': 'International Aid', 'Amount': '37000', 'Status': 'not started'}, {'Project Name': 'Birdview Avenue Improvements', 'Funding Source': 'National Foundation Fund', 'Amount': '79000', 'Status': 'not started'}, {'Project Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding Source': 'International Aid', 'Amount': '85000', 'Status': 'not started'}, {'Project Name': 'Outdoor Warning Sirens', 'Funding Source': 'Social Impact Investment', 'Amount': '28000', 'Status': 'not started'}, {'Project Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project Name': 'Outdoor Warning Sirens (FEMA)', 'Funding Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}]}

exec(code, env_args)

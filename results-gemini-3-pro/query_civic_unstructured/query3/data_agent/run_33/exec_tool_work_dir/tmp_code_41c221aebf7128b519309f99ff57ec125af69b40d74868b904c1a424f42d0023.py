code = """import json
import re

# Load data
with open(locals()['var_function-call-62592550053274037'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-62592550053277018'], 'r') as f:
    civic_docs = json.load(f)

full_text = "\\n".join([d.get('text', '') for d in civic_docs])

keywords = ['emergency', 'fema']

def has_keywords(text):
    return any(k in text.lower() for k in keywords)

def normalize_name(name):
    pattern = r'\\s*\\((?:.*?(?:FEMA|CalOES|CalJPIA).*?)\\)$'
    clean = re.sub(pattern, '', name, flags=re.IGNORECASE)
    return clean.strip()

unique_names = set()
for item in funding_data:
    unique_names.add(normalize_name(item['Project_Name']))
    unique_names.add(item['Project_Name'])

headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

header_positions = []
for h in headers:
    for m in re.finditer(re.escape(h), full_text, re.IGNORECASE):
        header_positions.append((m.start(), "HEADER", h))

project_positions = []
for name in unique_names:
    if len(name) < 5: continue
    for m in re.finditer(re.escape(name), full_text, re.IGNORECASE):
        project_positions.append((m.start(), "PROJECT", name))

# Sort: by Position, then Type (HEADER before PROJECT)
all_positions = sorted(header_positions + project_positions, key=lambda x: (x[0], x[1]))

project_info_map = {} 
current_header = "Unknown"

i = 0
while i < len(all_positions):
    current_pos = all_positions[i][0]
    
    # Identify the group at this position
    group_end = i
    while group_end < len(all_positions) and all_positions[group_end][0] == current_pos:
        group_end += 1
    
    # Items from i to group_end-1 are at current_pos
    group = all_positions[i:group_end]
    
    # Find next position for segment end
    next_pos = all_positions[group_end][0] if group_end < len(all_positions) else len(full_text)
    segment = full_text[current_pos:next_pos]
    
    # Process group
    # First update header if present
    for _, type_, content in group:
        if type_ == "HEADER":
            current_header = content
            
    # Then process projects
    for _, type_, content in group:
        if type_ == "PROJECT":
            # Determine status from segment
            status = "not started"
            if "Updates:" in segment or "Project Schedule:" in segment or "Project Description:" in segment:
                if "Design" in current_header: 
                    status = "design"
                elif "Not Started" in current_header: 
                    status = "not started"
                elif "Construction" in current_header:
                    if "completed" in segment.lower():
                        status = "completed"
                    else:
                        status = "construction"
                
                relevant = has_keywords(segment)
                
                # Store
                # If matches multiple times, we might overwrite. 
                # We overwrite only if "relevant" is true? Or just overwrite.
                # Assuming linear scan is fine.
                project_info_map[content] = {'status': status, 'relevant': relevant}
            else:
                # If segment doesn't look like a project section, maybe it's just a mention.
                # Don't overwrite existing good status with "not started" or None.
                if content not in project_info_map:
                    project_info_map[content] = {'status': "not started", 'relevant': False}

    i = group_end

final_output = []
for item in funding_data:
    p_name = item['Project_Name']
    norm_name = normalize_name(p_name)
    
    info = project_info_map.get(p_name) or project_info_map.get(norm_name)
    
    name_relevant = has_keywords(p_name)
    text_relevant = info['relevant'] if info else False
    
    if name_relevant or text_relevant:
        status_to_report = info['status'] if info else "not started"
        
        final_output.append({
            "Project_Name": p_name,
            "Funding_Source": item['Funding_Source'],
            "Amount": item['Amount'],
            "Status": status_to_report
        })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-2440996547258625204': ['Funding'], 'var_function-call-2440996547258622967': ['civic_docs'], 'var_function-call-2122594864921453126': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-2122594864921454085': 'file_storage/function-call-2122594864921454085.json', 'var_function-call-62592550053274037': 'file_storage/function-call-62592550053274037.json', 'var_function-call-62592550053277018': 'file_storage/function-call-62592550053277018.json', 'var_function-call-16195692788718819122': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Social Impact Investment', 'Amount': '77000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}]}

exec(code, env_args)

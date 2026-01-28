code = """import json

# Load data
with open(locals()['var_function-call-15070344879824368496'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-15070344879824368069'], 'r') as f:
    civic_docs = json.load(f)

keywords = ["park", "road", "fema", "fire", "emergency warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail", "emergency"]

parsed_projects = []
current_project = None
current_section_status = "design"
buffer = []

text = civic_docs[0]['text']
lines = text.split(chr(10))

for line in lines:
    line = line.strip()
    if not line:
        continue
        
    # Headers
    if "Capital Improvement Projects (Design)" in line:
        current_section_status = "design"
        current_project = None
        buffer = []
        continue
    if "Capital Improvement Projects (Construction)" in line:
        current_section_status = "construction"
        current_project = None
        buffer = []
        continue
    if "Capital Improvement Projects (Not Started)" in line:
        current_section_status = "not started"
        current_project = None
        buffer = []
        continue
    if "Disaster Recovery Projects" in line:
        current_section_status = "disaster"
        current_project = None
        buffer = []
        continue

    # Bullet detection
    is_bullet = line.startswith("(cid:190)") or line.startswith(chr(190))
    
    if is_bullet:
        # Determine Type
        is_start = False
        if "Project Description:" in line:
            is_start = True
        elif "Updates:" in line and "Project Updates" not in line:
            is_start = True
            
        if is_start:
            # Start New Project
            if buffer:
                name = buffer[-1]
                prev_content = buffer[:-1]
                
                # Append prev_content to current_project if exists
                if current_project:
                    current_project['text'] += " ".join(prev_content) + " "
                
                # Create New Project
                # Validate Name
                if "Page" not in name and "Agenda Item" not in name:
                    current_project = {
                        "Project_Name": name,
                        "Status_Section": current_section_status,
                        "text": ""
                    }
                    parsed_projects.append(current_project)
                else:
                    current_project = None
            
            if current_project:
                current_project['text'] += line + " "
            buffer = []
            
        else:
            # Continuation Bullet (Schedule, etc)
            if current_project:
                # Add buffer and line
                current_project['text'] += " ".join(buffer) + " " + line + " "
            buffer = []
            
    else:
        # Buffer text
        buffer.append(line)

# Handle last buffer
if current_project and buffer:
    current_project['text'] += " ".join(buffer)

# Process Parsed Projects
results = []
funding_map = {f['Project_Name']: f for f in funding_data}

for p in parsed_projects:
    p_name = p['Project_Name']
    p_text = p['text'].lower()
    p_topics = []
    
    full_text = (p_name + " " + p_text).lower()
    for kw in keywords:
        if kw in full_text:
            p_topics.append(kw)
            
    # Status
    status = p['Status_Section']
    if status == "construction":
        if "completed" in p_text:
            status = "completed"
        else:
            status = "design"
    if status == "disaster":
        if "completed" in p_text:
            status = "completed"
        else:
            status = "design"
            
    # Filter
    is_related = False
    if "fema" in p_topics or "emergency" in p_topics or "emergency warning" in p_topics:
        is_related = True
    if "fema" in p_name.lower() or "emergency" in p_name.lower():
        is_related = True
        
    if is_related:
        f_info = funding_map.get(p_name)
        if f_info:
            results.append({
                "Project Name": p_name,
                "Funding Source": f_info['Funding_Source'],
                "Amount": f_info['Amount'],
                "Status": status
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18371054564754366390': 'file_storage/function-call-18371054564754366390.json', 'var_function-call-18371054564754362375': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-15070344879824368496': 'file_storage/function-call-15070344879824368496.json', 'var_function-call-15070344879824368069': 'file_storage/function-call-15070344879824368069.json', 'var_function-call-2633647079085397024': [], 'var_function-call-8767218630817718124': {'parsed_count': 45, 'sample_parsed': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project'], 'funding_count': 500, 'sample_funding': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_function-call-9458519939930987624': [], 'var_function-call-7913651078523279337': {'parsed_fema_related': ['Outdoor Warning Signs'], 'funding_fema_related': ['Birdview Avenue Improvements (FEMA/CalOES Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)']}, 'var_function-call-4055307384925035367': 'Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor pha', 'var_function-call-12757605701528930721': ['Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022', 'Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff'], 'var_function-call-12760073400268136563': 'Clover Heights Storm Drainage Improvements\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to CalOES for review and working with consultant\n\nto finalize plans and specifications\n\n(cid:190) Project Schedule:\n\n(cid:131) Final Design: Summer, 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Co', 'var_function-call-6907064033902616679': {'is_extracted': True, 'funding_match': True, 'extracted_keys_sample': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Median Improvements Project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'Clover Heights Storm Drainage Improvements'], 'text_sample': '(cid:190) Updates: (cid:190) Project Schedule: ', 'has_fema': False}}

exec(code, env_args)

code = """import json

# Load data
with open(locals()['var_function-call-15070344879824368496'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-15070344879824368069'], 'r') as f:
    civic_docs = json.load(f)

parsed_projects = {}
current_project = None
buffer = []
text = civic_docs[0]['text']
lines = text.split(chr(10))

for line in lines:
    line = line.strip()
    if not line: continue
    if "Capital Improvement Projects" in line:
        current_project = None
        buffer = []
        continue

    is_bullet = line.startswith("(cid:190)") or line.startswith(chr(190))
    if is_bullet:
        is_start = False
        if "Project Description:" in line: is_start = True
        elif "Updates:" in line and "Project Updates" not in line: is_start = True
        
        if is_start:
            if buffer:
                name = buffer[-1]
                if "Page" not in name and "Agenda Item" not in name:
                    current_project = {"Project_Name": name, "text": ""}
                    parsed_projects[name] = current_project
                else: current_project = None
            if current_project: current_project['text'] += line + " "
            buffer = []
        else:
            if current_project: current_project['text'] += " ".join(buffer) + " " + line + " "
            buffer = []
    else:
        buffer.append(line)
if current_project and buffer: current_project['text'] += " ".join(buffer)

target = "Outdoor Warning Signs"
print("__RESULT__:")
if target in parsed_projects:
    print(json.dumps({
        "found": True, 
        "text": parsed_projects[target]['text'],
        "has_sirens": "sirens" in parsed_projects[target]['text'].lower()
    }))
else:
    print(json.dumps({"found": False}))"""

env_args = {'var_function-call-18371054564754366390': 'file_storage/function-call-18371054564754366390.json', 'var_function-call-18371054564754362375': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-15070344879824368496': 'file_storage/function-call-15070344879824368496.json', 'var_function-call-15070344879824368069': 'file_storage/function-call-15070344879824368069.json', 'var_function-call-2633647079085397024': [], 'var_function-call-8767218630817718124': {'parsed_count': 45, 'sample_parsed': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project'], 'funding_count': 500, 'sample_funding': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_function-call-9458519939930987624': [], 'var_function-call-7913651078523279337': {'parsed_fema_related': ['Outdoor Warning Signs'], 'funding_fema_related': ['Birdview Avenue Improvements (FEMA/CalOES Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)']}, 'var_function-call-4055307384925035367': 'Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor pha', 'var_function-call-12757605701528930721': ['Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022', 'Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff'], 'var_function-call-12760073400268136563': 'Clover Heights Storm Drainage Improvements\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to CalOES for review and working with consultant\n\nto finalize plans and specifications\n\n(cid:190) Project Schedule:\n\n(cid:131) Final Design: Summer, 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Co', 'var_function-call-6907064033902616679': {'is_extracted': True, 'funding_match': True, 'extracted_keys_sample': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Median Improvements Project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'Clover Heights Storm Drainage Improvements'], 'text_sample': '(cid:190) Updates: (cid:190) Project Schedule: ', 'has_fema': False}, 'var_function-call-3511556721614350788': [{'Project Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}], 'var_function-call-15199465999562571182': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Median Improvements Project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'Clover Heights Storm Drainage Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study', 'Malibu Road Slope Repairs', 'Encinal Canyon Road Repairs', 'PCH Signal Synchronization System Improvements Project', 'Storm Drain Trash Screens Phase Two', 'Bluffs Park Shade Structure', 'Marie Canyon Green Streets', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs', 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'Kanan Dume Biofilter', 'City Traffic Signals Backup Power'], 'var_function-call-12728615354157449567': [{'Project Name': 'Clover Heights Storm Drainage Improvements', 'Funding Source': 'Development Bank Loan', 'Amount': 22000, 'Status': 'design'}, {'Project Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding Source': 'Educational Sponsorship', 'Amount': 97000, 'Status': 'design'}]}

exec(code, env_args)

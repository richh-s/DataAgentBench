code = """import json
import re

# Load data
with open(locals()['var_function-call-5680067546526520620'], 'r') as f:
    civic_data = json.load(f)
    
with open(locals()['var_function-call-10418813875074106507'], 'r') as f:
    funding_data = json.load(f)

text = civic_data[0]['text']

# Map normalized base names to funding records
base_to_funding = {}
for r in funding_data:
    name = r['Project_Name']
    # Normalize: lower, remove punctuation, remove suffixes
    # Suffixes are in parens.
    if "(" in name:
        base = name.split("(")[0].strip()
    else:
        base = name.strip()
    
    base_norm = base.lower()
    if base_norm not in base_to_funding:
        base_to_funding[base_norm] = []
    base_to_funding[base_norm].append(r)

# Parse text projects
lines = text.splitlines()
projects = []
current_project = None
current_section = ""
current_block = []

base_names_set = set(base_to_funding.keys())

for line in lines:
    line = line.strip()
    if not line: continue
    
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
        current_section = line
        continue
    
    # Check if line matches a base name
    # We do exact match on normalized string
    line_norm = line.lower()
    
    # Sometimes text has slight diffs, but exact match worked for many in previous step.
    # Let's check if line_norm is in base_names_set
    if line_norm in base_names_set:
        if current_project:
            projects.append({
                "name": current_project,
                "section": current_section,
                "text": " ".join(current_block)
            })
        current_project = line
        current_block = []
    else:
        if current_project:
            current_block.append(line)

if current_project:
    projects.append({
        "name": current_project,
        "section": current_section,
        "text": " ".join(current_block)
    })

# Analyze and Sum Funding
total_funding = 0
qualified_projects = []

for p in projects:
    name = p['name']
    txt = p['text']
    base_norm = name.lower()
    
    # 1. Start Date Check
    started_in_2022 = False
    
    # Explicit dates
    if "Begin Construction" in txt:
        idx = txt.find("Begin Construction")
        snippet = txt[idx:idx+50]
        if "2022" in snippet:
            started_in_2022 = True
    
    # Completed in 2022 (implies started <= 2022)
    # The prompt specifically asks for "projects that started in 2022".
    # If completed in 2022, it *could* have started in 2022.
    # For "Bluffs Park Shade Structure", "Construction was completed November 2022".
    # For "Broad Beach Road...", "Construction was completed, November 2022".
    # For "Marie Canyon Green Streets", "Construction was completed, January 2023" (started 2022 likely).
    # "Point Dume Walkway Repairs", "Construction was completed, November 2022".
    
    # I will assume projects completed in late 2022 started in 2022 given the scope of civic projects (often < 1 year).
    # If completed early 2022 (e.g. Jan), might have started 2021.
    # But here completion is Nov 2022.
    if "Construction was completed" in txt:
        idx = txt.find("Construction was completed")
        snippet = txt[idx:idx+50]
        if "2022" in snippet:
            started_in_2022 = True
    
    # Name check
    if "2022" in name:
        started_in_2022 = True

    if not started_in_2022:
        continue

    # 2. Disaster Related Check
    is_disaster = False
    
    # Check text keywords
    keywords = ["FEMA", "CalOES", "CalJPIA", "Disaster", "Woolsey Fire"]
    for k in keywords:
        if k.lower() in txt.lower():
            is_disaster = True
            break
            
    # Check funding record suffixes
    funding_records = base_to_funding.get(base_norm, [])
    for fr in funding_records:
        fname = fr['Project_Name']
        if "FEMA" in fname or "CalOES" in fname or "CalJPIA" in fname:
            is_disaster = True
            break
            
    if is_disaster:
        # Sum funding
        p_funding = 0
        for fr in funding_records:
            p_funding += int(fr['Amount'])
        
        qualified_projects.append({
            "name": name,
            "funding": p_funding,
            "reason": "Started 2022 and Disaster Related"
        })
        total_funding += p_funding

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": qualified_projects}))"""

env_args = {'var_function-call-5680067546526520620': 'file_storage/function-call-5680067546526520620.json', 'var_function-call-10418813875074106507': 'file_storage/function-call-10418813875074106507.json', 'var_function-call-2251975116002946257': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the consultant to finalize the design plans for t'}, {'name': 'PCH Median Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) On September 22, 2022, the City received four (4) construction bids and'}, {'name': 'Westward Beach Road Repair Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City working with consultant on the design of the shoulder repairs (cid'}, {'name': 'Westward Beach Road Drainage Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans are under review by Fish and Wildlife and City is expecting comme'}, {'name': 'Clover Heights Storm Drainage Improvements', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City submitted plans to CalOES for review and working with consultant t'}, {'name': 'Latigo Canyon Road Retaining Wall Repair Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans and specifications have been completed (cid:131) Awaiting final F'}, {'name': 'Storm Drain Master Plan', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Field data collection has been completed and storm drain inventory has '}, {'name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans and specifications are being finalized by consultant (cid:190) Pr'}, {'name': 'Civic Center Water Treatment Facility Phase 2', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the State Water Board regarding the Cultural Reso'}, {'name': 'Permanent Skate Park', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the consultant to finalize the design plans for t'}, {'name': 'PCH at Trancas Canyon Road Right Turn Lane', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City submitted plans to Caltrans for review and expecting comments in t'}, {'name': 'Outdoor Warning Signs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Project to be discussed during a joint Public Works and Public Safety C'}, {'name': 'Malibu Bluffs Park South Walkway Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City to request proposal from consultant for design services (cid:190) '}, {'name': 'Trancas Canyon Park Playground', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is currently working on the final design plans (cid:190) Estimate'}, {'name': 'Malibu Canyon Road Traffic Study', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Project Description: This project will consist of a traffic study on Malibu Canyon Road ne'}, {'name': 'Malibu Road Slope Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Project is currently under construction (cid:190) Complete Construction: April 20'}, {'name': 'Encinal Canyon Road Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Project is currently under construction (cid:190) Complete Construction: Summer 2'}, {'name': 'PCH Signal Synchronization System Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) On February 27, 2023, City Council awarded the contract to GMZ Engineer'}, {'name': 'Storm Drain Trash Screens Phase Two', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Project is currently out to bid. Bids are due on March 23, 2023. (cid:1'}, {'name': 'Bluffs Park Shade Structure', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Construction was completed November 2022. Notice of completion filed January 2023'}, {'name': 'Marie Canyon Green Streets', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, January 2023 (cid:131) Scheduled for Counci'}, {'name': 'Broad Beach Road Water Quality Repair', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completio'}, {'name': 'Point Dume Walkway Repairs', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completio'}, {'name': 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study and includes'}, {'name': 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study and includes'}, {'name': 'Kanan Dume Biofilter', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the City’s Enhanced Watershed Manageme'}, {'name': 'City Traffic Signals Backup Power', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project will include upgrading the backup power system to the Ci'}]}

exec(code, env_args)

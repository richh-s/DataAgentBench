code = """import json

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
    if "(" in name:
        base = name.split("(")[0].strip()
    else:
        base = name.strip()
    
    base_norm = base.lower()
    if base_norm not in base_to_funding:
        base_to_funding[base_norm] = []
    base_to_funding[base_norm].append(r)

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
    line_norm = line.lower()
    if line_norm in base_names_set:
        if current_project:
            projects.append({"name": current_project, "text": " ".join(current_block)})
        current_project = line
        current_block = []
    else:
        if current_project:
            current_block.append(line)
if current_project:
    projects.append({"name": current_project, "text": " ".join(current_block)})

# Debug "Broad Beach Road Water Quality Repair"
target = "broad beach road water quality repair"
print("__RESULT__:")
debug_info = []
for p in projects:
    if target in p['name'].lower():
        debug_info.append(f"Project Found: {p['name']}")
        txt = p['text']
        debug_info.append(f"Snippet: {txt[:100]}")
        
        # Check start
        started = False
        if "Construction was completed" in txt:
            idx = txt.find("Construction was completed")
            snip = txt[idx:idx+50]
            debug_info.append(f"Completion Snippet: {snip}")
            if "2022" in snip:
                started = True
        debug_info.append(f"Started 2022: {started}")
        
        # Check disaster
        is_disaster = False
        funding_recs = base_to_funding.get(p['name'].lower(), [])
        debug_info.append(f"Funding Records: {[r['Project_Name'] for r in funding_recs]}")
        for fr in funding_recs:
            if "CalJPIA" in fr['Project_Name']:
                is_disaster = True
        debug_info.append(f"Is Disaster: {is_disaster}")

print(json.dumps(debug_info))"""

env_args = {'var_function-call-5680067546526520620': 'file_storage/function-call-5680067546526520620.json', 'var_function-call-10418813875074106507': 'file_storage/function-call-10418813875074106507.json', 'var_function-call-2251975116002946257': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the consultant to finalize the design plans for t'}, {'name': 'PCH Median Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) On September 22, 2022, the City received four (4) construction bids and'}, {'name': 'Westward Beach Road Repair Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City working with consultant on the design of the shoulder repairs (cid'}, {'name': 'Westward Beach Road Drainage Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans are under review by Fish and Wildlife and City is expecting comme'}, {'name': 'Clover Heights Storm Drainage Improvements', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City submitted plans to CalOES for review and working with consultant t'}, {'name': 'Latigo Canyon Road Retaining Wall Repair Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans and specifications have been completed (cid:131) Awaiting final F'}, {'name': 'Storm Drain Master Plan', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Field data collection has been completed and storm drain inventory has '}, {'name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans and specifications are being finalized by consultant (cid:190) Pr'}, {'name': 'Civic Center Water Treatment Facility Phase 2', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the State Water Board regarding the Cultural Reso'}, {'name': 'Permanent Skate Park', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the consultant to finalize the design plans for t'}, {'name': 'PCH at Trancas Canyon Road Right Turn Lane', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City submitted plans to Caltrans for review and expecting comments in t'}, {'name': 'Outdoor Warning Signs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Project to be discussed during a joint Public Works and Public Safety C'}, {'name': 'Malibu Bluffs Park South Walkway Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City to request proposal from consultant for design services (cid:190) '}, {'name': 'Trancas Canyon Park Playground', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is currently working on the final design plans (cid:190) Estimate'}, {'name': 'Malibu Canyon Road Traffic Study', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Project Description: This project will consist of a traffic study on Malibu Canyon Road ne'}, {'name': 'Malibu Road Slope Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Project is currently under construction (cid:190) Complete Construction: April 20'}, {'name': 'Encinal Canyon Road Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Project is currently under construction (cid:190) Complete Construction: Summer 2'}, {'name': 'PCH Signal Synchronization System Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) On February 27, 2023, City Council awarded the contract to GMZ Engineer'}, {'name': 'Storm Drain Trash Screens Phase Two', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Project is currently out to bid. Bids are due on March 23, 2023. (cid:1'}, {'name': 'Bluffs Park Shade Structure', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Construction was completed November 2022. Notice of completion filed January 2023'}, {'name': 'Marie Canyon Green Streets', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, January 2023 (cid:131) Scheduled for Counci'}, {'name': 'Broad Beach Road Water Quality Repair', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completio'}, {'name': 'Point Dume Walkway Repairs', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completio'}, {'name': 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study and includes'}, {'name': 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study and includes'}, {'name': 'Kanan Dume Biofilter', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the City’s Enhanced Watershed Manageme'}, {'name': 'City Traffic Signals Backup Power', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project will include upgrading the backup power system to the Ci'}], 'var_function-call-16824871823733367553': {'total_funding': 0, 'projects': []}}

exec(code, env_args)

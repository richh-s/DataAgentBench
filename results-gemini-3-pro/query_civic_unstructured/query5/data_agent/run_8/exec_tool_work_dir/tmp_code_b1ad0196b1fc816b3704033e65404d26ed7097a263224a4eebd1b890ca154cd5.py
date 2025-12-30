code = """import json
import re

# Load data
with open(locals()['var_function-call-5680067546526520620'], 'r') as f:
    civic_data = json.load(f)
with open(locals()['var_function-call-10418813875074106507'], 'r') as f:
    funding_data = json.load(f)

text = civic_data[0]['text']
lines = text.splitlines()

# 1. Extract Projects from Text
# We use the heuristic that lines matching (fuzzy) funding names are projects.
# But we also need to catch projects that might not match perfectly.
# Let's stick to the "lines matching funding base names" approach but broaden it.
# Actually, the Funding DB has the comprehensive list of projects.
# I will use the Funding DB names (normalized) to scan the text.

# Prepare tokens for funding names
funding_map = []
for r in funding_data:
    name = r['Project_Name']
    # Base name for matching (remove parens)
    if "(" in name:
        base = name.split("(")[0]
    else:
        base = name
    norm = re.sub(r'[^\w\s]', '', base).lower()
    tokens = set(norm.split())
    funding_map.append({
        "tokens": tokens,
        "record": r,
        "base_norm": norm
    })

# Scan text for headers that match funding names
projects = []
current_project = None
current_text = []

# To identify project headers in text, we look for lines that have high overlap with funding names
# AND are likely headers (short, not sentences).

for line in lines:
    line_clean = line.strip()
    if not line_clean: continue
    
    # Check if header
    # Heuristic: line length < 100, no ending punctuation like period (unless abbreviation)
    if len(line_clean) > 100 or line_clean.endswith('.'):
        if current_project:
            current_text.append(line_clean)
        continue
    
    # Check overlap with any funding name
    line_norm = re.sub(r'[^\w\s]', '', line_clean).lower()
    line_tokens = set(line_norm.split())
    if not line_tokens: continue
    
    match_found = False
    for item in funding_map:
        # Check if line_tokens is a superset or subset or high overlap
        # We want the text line to BE the project name.
        # So line tokens should match funding tokens closely.
        if item['tokens'] == line_tokens:
            match_found = True
            break
        # Also check "Repair" vs "Repairs"
        # Jaccard index
        intersection = len(line_tokens.intersection(item['tokens']))
        union = len(line_tokens.union(item['tokens']))
        if union > 0 and intersection / union > 0.8:
            match_found = True
            break
            
    if match_found:
        if current_project:
            projects.append({"name": current_project, "text": " ".join(current_text)})
        current_project = line_clean
        current_text = []
    else:
        if current_project:
            current_text.append(line_clean)

if current_project:
    projects.append({"name": current_project, "text": " ".join(current_text)})

# 2. Process extracted projects
total_funding = 0
results = []

for p in projects:
    name = p['name']
    txt = p['text']
    
    # Determine Start Year
    start_2022 = False
    
    # Check "Begin Construction" or "Construction was completed" or "Started"
    if "2022" in name:
        start_2022 = True
    
    # Look for dates in text
    # Regex for "Construction ... 2022"
    # Or "Completed ... 2022"
    if "2022" in txt:
        if "Construction was completed" in txt:
             # Check proximity
             idx = txt.find("Construction was completed")
             if "2022" in txt[idx:idx+60]:
                 start_2022 = True
        if "Begin Construction" in txt:
             idx = txt.find("Begin Construction")
             if "2022" in txt[idx:idx+60]:
                 start_2022 = True
    
    if not start_2022:
        continue

    # Determine Disaster
    is_disaster = False
    
    # Text keywords
    disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey Fire", "Disaster Recovery"]
    for k in disaster_keywords:
        if k.lower() in txt.lower() or k.lower() in name.lower():
            is_disaster = True
            break
    
    # Link to funding records
    p_tokens = set(re.sub(r'[^\w\s]', '', name).lower().split())
    matched_funding = []
    
    for item in funding_map:
        f_tokens = item['tokens']
        # Check overlap
        intersection = len(p_tokens.intersection(f_tokens))
        union = len(p_tokens.union(f_tokens))
        if union > 0 and intersection / union > 0.6:
            matched_funding.append(item['record'])
            # Check suffix in funding name
            fname = item['record']['Project_Name']
            if "(FEMA" in fname or "(CalOES" in fname or "(CalJPIA" in fname:
                is_disaster = True
    
    if is_disaster:
        # Calculate funding
        # Sum unique funding IDs
        # (Assuming Funding_ID is unique per amount)
        f_ids = set()
        amount = 0
        for r in matched_funding:
            if r['Funding_ID'] not in f_ids:
                amount += int(r['Amount'])
                f_ids.add(r['Funding_ID'])
        
        if amount > 0:
            results.append({
                "project": name,
                "amount": amount,
                "sources": [r['Project_Name'] for r in matched_funding]
            })
            total_funding += amount

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "details": results}))"""

env_args = {'var_function-call-5680067546526520620': 'file_storage/function-call-5680067546526520620.json', 'var_function-call-10418813875074106507': 'file_storage/function-call-10418813875074106507.json', 'var_function-call-2251975116002946257': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the consultant to finalize the design plans for t'}, {'name': 'PCH Median Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) On September 22, 2022, the City received four (4) construction bids and'}, {'name': 'Westward Beach Road Repair Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City working with consultant on the design of the shoulder repairs (cid'}, {'name': 'Westward Beach Road Drainage Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans are under review by Fish and Wildlife and City is expecting comme'}, {'name': 'Clover Heights Storm Drainage Improvements', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City submitted plans to CalOES for review and working with consultant t'}, {'name': 'Latigo Canyon Road Retaining Wall Repair Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans and specifications have been completed (cid:131) Awaiting final F'}, {'name': 'Storm Drain Master Plan', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Field data collection has been completed and storm drain inventory has '}, {'name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Plans and specifications are being finalized by consultant (cid:190) Pr'}, {'name': 'Civic Center Water Treatment Facility Phase 2', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the State Water Board regarding the Cultural Reso'}, {'name': 'Permanent Skate Park', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is working with the consultant to finalize the design plans for t'}, {'name': 'PCH at Trancas Canyon Road Right Turn Lane', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City submitted plans to Caltrans for review and expecting comments in t'}, {'name': 'Outdoor Warning Signs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Project to be discussed during a joint Public Works and Public Safety C'}, {'name': 'Malibu Bluffs Park South Walkway Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) City to request proposal from consultant for design services (cid:190) '}, {'name': 'Trancas Canyon Park Playground', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Design)', 'text_preview': '(cid:190) Updates: (cid:131) Staff is currently working on the final design plans (cid:190) Estimate'}, {'name': 'Malibu Canyon Road Traffic Study', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Project Description: This project will consist of a traffic study on Malibu Canyon Road ne'}, {'name': 'Malibu Road Slope Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Project is currently under construction (cid:190) Complete Construction: April 20'}, {'name': 'Encinal Canyon Road Repairs', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Project is currently under construction (cid:190) Complete Construction: Summer 2'}, {'name': 'PCH Signal Synchronization System Improvements Project', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) On February 27, 2023, City Council awarded the contract to GMZ Engineer'}, {'name': 'Storm Drain Trash Screens Phase Two', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Project is currently out to bid. Bids are due on March 23, 2023. (cid:1'}, {'name': 'Bluffs Park Shade Structure', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: Construction was completed November 2022. Notice of completion filed January 2023'}, {'name': 'Marie Canyon Green Streets', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, January 2023 (cid:131) Scheduled for Counci'}, {'name': 'Broad Beach Road Water Quality Repair', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Construction)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completio'}, {'name': 'Point Dume Walkway Repairs', 'start_year': 2022, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completio'}, {'name': 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study and includes'}, {'name': 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study and includes'}, {'name': 'Kanan Dume Biofilter', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project was identified in the City’s Enhanced Watershed Manageme'}, {'name': 'City Traffic Signals Backup Power', 'start_year': None, 'is_disaster': False, 'section': 'Capital Improvement Projects (Not Started)', 'text_preview': '(cid:190) Project Description: This project will include upgrading the backup power system to the Ci'}], 'var_function-call-16824871823733367553': {'total_funding': 0, 'projects': []}, 'var_function-call-13523823765171193655': ['Project Found: Broad Beach Road Water Quality Repair', 'Snippet: (cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completio', 'Completion Snippet: Construction was completed, November 2022 (cid:131', 'Started 2022: True', "Funding Records: ['Broad Beach Road Water Quality Repair']", 'Is Disaster: False']}

exec(code, env_args)

code = """import json
import re

# Load data
funding_path = locals()['var_function-call-12490776442151259677']
docs_path = locals()['var_function-call-2297309478391290844']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for d in civic_docs:
    full_text += d.get('text', '') + chr(10) + chr(10)

funding_map = {}
for rec in funding_data:
    name = rec['Project_Name']
    simple = re.sub(r'\s*\(.*?\)$', '', name).strip()
    if simple not in funding_map:
        funding_map[simple] = []
    funding_map[simple].append(rec)

search_names = sorted(funding_map.keys(), key=len, reverse=True)

total_funding = 0
matched_ids = set()
debug_log = []

disaster_keywords = ["FEMA", "CalOES", "Disaster", "Woolsey Fire", "Recovery", "CalJPIA"]

# Stricter patterns
# We want to match dates like "Fall 2022", "November 2022", "March 2022"
# Preceded by "Begin Construction:", "Advertise:", "Awarded:"
date_part = r"(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\s*2022"

start_patterns = [
    r"Begin Construction:\s*" + date_part,
    r"Advertise:\s*" + date_part,
    r"Construction started\s*:?\s*" + date_part,
    r"Notice to Proceed\s*:?\s*" + date_part,
    r"Award.*Contract\s*:?\s*" + date_part,
    r"Construction began\s*:?\s*" + date_part,
    r"Construction.*underway.*2022" # Maybe?
]

# Case-insensitive compile
patterns_compiled = [re.compile(p, re.IGNORECASE) for p in start_patterns]

for name in search_names:
    start_idx = 0
    while True:
        idx = full_text.find(name, start_idx)
        if idx == -1:
            break
            
        # Context window: Name + 1000 chars
        window = full_text[idx:idx+1000]
        
        # Verify it's a project section header or update block
        # Look for "Updates:" or "Project Schedule" within reasonable distance (e.g. 200 chars) from name
        # The name might be the header.
        
        # Check if the name is followed by newline or colon
        name_end = idx + len(name)
        following_chars = full_text[name_end:name_end+50]
        
        # Heuristic: Valid section if followed by newline or "Updates" or "Project Description"
        # Not just a mention in a list.
        # But some docs might just list them.
        
        # Let's check matching patterns in the window
        match_snippet = None
        started_2022 = False
        for pat in patterns_compiled:
            m = pat.search(window)
            if m:
                started_2022 = True
                match_snippet = m.group(0)
                break
        
        if started_2022:
            # Check Disaster
            is_disaster_text = False
            for k in disaster_keywords:
                if k.lower() in window.lower():
                    is_disaster_text = True
                    break
            
            records = funding_map[name]
            for rec in records:
                fid = rec['Funding_ID']
                if fid in matched_ids:
                    continue
                    
                rec_name = rec['Project_Name']
                is_disaster_rec = any(k in rec_name for k in ["FEMA", "CalOES", "Disaster", "CalJPIA"])
                
                if is_disaster_rec or is_disaster_text:
                    amt = rec['Amount']
                    if isinstance(amt, str):
                        amt = int(amt.replace(',', '').replace('$', ''))
                    
                    total_funding += amt
                    matched_ids.add(fid)
                    debug_log.append({
                        "Project": rec_name,
                        "Reason": "Disaster Rec" if is_disaster_rec else "Disaster Text",
                        "Snippet": match_snippet
                    })
        
        start_idx = idx + 1

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "details": debug_log}))"""

env_args = {'var_function-call-12490776442151259677': 'file_storage/function-call-12490776442151259677.json', 'var_function-call-12490776442151257162': 'file_storage/function-call-12490776442151257162.json', 'var_function-call-2297309478391290844': 'file_storage/function-call-2297309478391290844.json', 'var_function-call-13110656705966846907': {'total_funding': 1745000, 'matched_projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Civic Center Stormwater Diversion Structure', 'Encinal Canyon Road Drainage Improvements', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', '2021 Annual Street Maintenance', 'Guardrail Replacement Citywide', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Civic Center Way Improvements', 'Corral Canyon Culvert Repairs', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Clover Heights Storm Drain', 'Clover Heights Storm Drain (FEMA Project)', 'Annual Street Maintenance', 'Malibu Road Slope Repairs', 'Malibu Road Slope Repairs (CalOES Project)']}}

exec(code, env_args)

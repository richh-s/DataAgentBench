code = """import json
import re

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
matched_ranges = []
debug_log = []

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey Fire"]

date_part = r"(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\s*2022"
start_patterns = [
    r"Begin Construction:\s*" + date_part,
    r"Advertise:\s*" + date_part,
    r"Construction started\s*:?\s*" + date_part,
    r"Notice to Proceed\s*:?\s*" + date_part,
    r"Award.*Contract\s*:?\s*" + date_part,
    r"Construction began\s*:?\s*" + date_part,
    r"Construction.*underway.*2022"
]
patterns_compiled = [re.compile(p, re.IGNORECASE) for p in start_patterns]

for name in search_names:
    records = funding_map[name]
    
    # Check if this project family has any disaster suffix
    has_disaster_suffix = False
    for rec in records:
        if any(k in rec['Project_Name'] for k in ["FEMA", "CalOES", "CalJPIA"]):
            has_disaster_suffix = True
            break
            
    # If no suffix, we treat as Capital/Other and skip?
    # Unless we want to trust text extraction 100%.
    # Based on analysis, text extraction of "Disaster" keyword has false positives.
    # We will skip if no suffix.
    if not has_disaster_suffix:
        continue

    start_idx = 0
    while True:
        idx = full_text.find(name, start_idx)
        if idx == -1:
            break
        
        end_idx = idx + len(name)
        
        overlap = False
        for r_start, r_end in matched_ranges:
            if not (end_idx <= r_start or idx >= r_end):
                overlap = True
                break
        
        if overlap:
            start_idx = idx + 1
            continue

        window = full_text[idx:idx+1000]
        
        if "Updates:" in window or "Project Description:" in window or "Project Schedule:" in window:
            
            started_2022 = False
            for pat in patterns_compiled:
                if pat.search(window):
                    started_2022 = True
                    break
            
            if started_2022:
                matched_ranges.append((idx, end_idx))
                
                # Add ALL records for this project family
                # (Since it's a disaster project family and it started in 2022)
                for rec in records:
                    fid = rec['Funding_ID']
                    if fid not in matched_ids:
                        amt = rec['Amount']
                        if isinstance(amt, str):
                            amt = int(amt.replace(',', '').replace('$', ''))
                        
                        total_funding += amt
                        matched_ids.add(fid)
                        debug_log.append(rec['Project_Name'])
                        
        start_idx = idx + 1

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": debug_log}))"""

env_args = {'var_function-call-12490776442151259677': 'file_storage/function-call-12490776442151259677.json', 'var_function-call-12490776442151257162': 'file_storage/function-call-12490776442151257162.json', 'var_function-call-2297309478391290844': 'file_storage/function-call-2297309478391290844.json', 'var_function-call-13110656705966846907': {'total_funding': 1745000, 'matched_projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Civic Center Stormwater Diversion Structure', 'Encinal Canyon Road Drainage Improvements', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', '2021 Annual Street Maintenance', 'Guardrail Replacement Citywide', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Civic Center Way Improvements', 'Corral Canyon Culvert Repairs', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Clover Heights Storm Drain', 'Clover Heights Storm Drain (FEMA Project)', 'Annual Street Maintenance', 'Malibu Road Slope Repairs', 'Malibu Road Slope Repairs (CalOES Project)']}, 'var_function-call-15595486917710705673': {'total_funding': 1387000, 'details': [{'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': '2021 Annual Street Maintenance', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Corral Canyon Culvert Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Clover Heights Storm Drain', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Clover Heights Storm Drain (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Annual Street Maintenance', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Malibu Road Slope Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Malibu Road Slope Repairs (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}]}, 'var_function-call-8713040904819074516': {'total_funding': 1228000, 'projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Encinal Canyon Road Drainage Improvements', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Clover Heights Storm Drain', 'Clover Heights Storm Drain (FEMA Project)', 'Malibu Road Slope Repairs', 'Malibu Road Slope Repairs (CalOES Project)']}, 'var_function-call-16849463267787151857': {'total_funding': 1745000, 'projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Civic Center Stormwater Diversion Structure', 'Encinal Canyon Road Drainage Improvements', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', '2021 Annual Street Maintenance', 'Guardrail Replacement Citywide', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Civic Center Way Improvements', 'Corral Canyon Culvert Repairs', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Clover Heights Storm Drain', 'Clover Heights Storm Drain (FEMA Project)', 'Annual Street Maintenance', 'Malibu Road Slope Repairs', 'Malibu Road Slope Repairs (CalOES Project)']}, 'var_function-call-7124456111998180630': {'total_funding': 1387000, 'details': [{'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': '2021 Annual Street Maintenance', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Corral Canyon Culvert Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Clover Heights Storm Drain', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Clover Heights Storm Drain (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Annual Street Maintenance', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Malibu Road Slope Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Malibu Road Slope Repairs (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}]}, 'var_function-call-12312104766243362854': {'total_funding': 1364000, 'details': [{'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: April 2022'}, {'Project': '2021 Annual Street Maintenance', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Spring 2022'}, {'Project': 'Corral Canyon Culvert Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Clover Heights Storm Drain', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Clover Heights Storm Drain (FEMA Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Summer 2022'}, {'Project': 'Malibu Road Slope Repairs', 'Reason': 'Disaster Text', 'Snippet': 'Begin Construction: Fall 2022'}, {'Project': 'Malibu Road Slope Repairs (CalOES Project)', 'Reason': 'Disaster Rec', 'Snippet': 'Begin Construction: Fall 2022'}]}}

exec(code, env_args)

code = """import json
import re

with open(locals()['var_function-call-4323330023283925201'], 'r') as f:
    funding_data = json.load(f)

# Target projects identified from text analysis
targets = [
    "Marie Canyon Green Streets",
    "Civic Center Water Treatment Facility Phase 2",
    "Birdview Avenue Improvements",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements",
    "Broad Beach Road Water Quality Infrastructure Repairs",
    "Trancas Canyon Park Slope Stabilization Project",
    "Trancas Canyon Park Planting and Irrigation Repairs",
    "Bluffs Park Shade Structure",
    "PCH Signal Synchronization System Improvements Project",
    "PCH at Trancas Canyon Road Right Turn Lane"
]

# Suffixes to remove for normalization
suffixes = [
    r"\(FEMA Project\)", r"\(CalJPIA Project\)", r"\(CalOES Project\)",
    r"\(FEMA/CalOES Project\)", r"\(FEMA\)", r"\(CalJPIA\)", r"\(CalOES\)",
    r"\(Design\)", r"\(Construction\)"
]

def normalize(name):
    for s in suffixes:
        name = re.sub(s, "", name, flags=re.IGNORECASE)
    return name.strip()

# Normalize funding data
funding_map = {} # Normalized Name -> Total Amount
debug_matches = []

for entry in funding_data:
    original_name = entry['Project_Name']
    norm_name = normalize(original_name)
    amount = float(entry['Amount'])
    
    if norm_name not in funding_map:
        funding_map[norm_name] = 0
    funding_map[norm_name] += amount

# Match targets
total_funding = 0
matched_projects = set()
missing_projects = []

for t in targets:
    # Try exact match first
    # Then normalized match
    # Then fuzzy?
    
    t_norm = normalize(t)
    
    found = False
    # Check direct key
    if t_norm in funding_map:
        total_funding += funding_map[t_norm]
        matched_projects.add(t)
        debug_matches.append((t, t_norm, funding_map[t_norm]))
        found = True
    else:
        # Try to find a close match in funding keys
        # For example "Trancas Canyon Park Slope Stabilization Project" might be "Trancas Canyon Park Upper and Lower Slopes Repair"
        # Let's list potential candidates containing words
        candidates = []
        words = set(t_norm.split())
        for k in funding_map.keys():
            k_words = set(k.split())
            common = words.intersection(k_words)
            if len(common) > 2: # Arbitrary overlap
                candidates.append(k)
        
        if candidates:
            # Pick best? Or just report
            missing_projects.append((t, candidates))
        else:
            missing_projects.append((t, "No candidates"))

print("__RESULT__:")
print(json.dumps({
    "matched": list(matched_projects), 
    "missing": missing_projects, 
    "total_funding": total_funding,
    "debug": debug_matches
}))"""

env_args = {'var_function-call-5331130674983609150': 'file_storage/function-call-5331130674983609150.json', 'var_function-call-5331130674983611055': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11024242700101333530': 'file_storage/function-call-11024242700101333530.json', 'var_function-call-4323330023283925201': 'file_storage/function-call-4323330023283925201.json', 'var_function-call-3663834181193932891': [{'name': 'Marie Canyon Green Streets', 'context': 'anticipated to have a final design by March 2022. The project will be', 'date': 'March 2022'}, {'name': 'Marie Canyon Green Streets', 'context': '(cid:131) Complete Design: March 2022', 'date': 'March 2022'}, {'name': 'Marie Canyon Green Streets', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'PCH Median Improvements Project', 'context': 'project will have final approval by March 2022. The project will be', 'date': 'March 2022'}, {'name': 'PCH Median Improvements Project', 'context': '(cid:131) Complete Design: March 2022', 'date': 'March 2022'}, {'name': 'PCH Signal Synchronization System Improvements Project', 'context': 'approval by March 2022. The project will be advertised for construction', 'date': 'March 2022'}, {'name': 'PCH Signal Synchronization System Improvements Project', 'context': '(cid:131) Complete Final Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Westward Beach Road Improvements Project', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'shade structures at Malibu Bluffs Park.', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'shade structures at Malibu Bluffs Park.', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'context': 'Commission will then review the project in Spring 2022 before final', 'date': 'Spring 2022'}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'context': 'March 2022', 'date': 'March 2022'}, {'name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'context': '(cid:131) Begin Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'context': '(cid:131) Begin Construction: April 2022', 'date': 'April 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'within the City.', 'context': '(cid:131) Completion Date: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Agenda Item # 4.A.', 'context': 'beginning in April 2022.', 'date': 'April 2022'}, {'name': 'Agenda Item # 4.A.', 'context': '(cid:131) Begin Construction: April 2022', 'date': 'April 2022'}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'context': '(cid:131) The project design will commence during the Spring 2022.', 'date': 'Spring 2022'}, {'name': 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Civic Center Water Treatment Facility Phase 2', 'context': '(cid:131) Begin Construction: March 2022', 'date': 'March 2022'}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Civic Center Water Treatment Facility Phase 2', 'context': '(cid:131) Begin Construction: March 2022', 'date': 'March 2022'}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'context': '(cid:131) Completion Date: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Marie Canyon Green Streets', 'context': '(cid:131) Complete Design: March 2022', 'date': 'March 2022'}, {'name': 'PCH Median Improvements Project', 'context': '(cid:131) Complete Design: March 2022', 'date': 'March 2022'}, {'name': 'PCH Signal Synchronization System Improvements Project', 'context': '(cid:131) This project will be presented to the Planning Commission in May 2022.', 'date': 'May 2022'}, {'name': 'PCH Signal Synchronization System Improvements Project', 'context': 'by March 2022. The project will be advertised for construction bids', 'date': 'March 2022'}, {'name': 'PCH Signal Synchronization System Improvements Project', 'context': '(cid:131) Complete Final Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'shade structures at Malibu Bluffs Park.', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'context': 'Commission will then review the project in Spring 2022 before final', 'date': 'Spring 2022'}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'context': 'go to Council in April 2022 after the Funding Agreement is issued by', 'date': 'April 2022'}, {'name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'context': '(cid:131) Begin Design: Late Spring 2022', 'date': 'Spring 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'context': '(cid:131) Complete Design: March 2022', 'date': 'March 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'context': '(cid:131) Advertise: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'context': '(cid:131) Complete Design: April 2022', 'date': 'April 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'context': '(cid:131) Advertise: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}, {'name': 'City.', 'context': '(cid:131) Completion Date: Spring 2022', 'date': 'Spring 2022'}, {'name': 'damaged by the Woolsey Fire.', 'context': 'anticipated that the final design will be complete by March 2022. The', 'date': 'March 2022'}, {'name': 'damaged by the Woolsey Fire.', 'context': 'beginning in Spring 2022.', 'date': 'Spring 2022'}, {'name': 'damaged by the Woolsey Fire.', 'context': '(cid:131) Complete Design: March 2022', 'date': 'March 2022'}, {'name': 'damaged by the Woolsey Fire.', 'context': '(cid:131) Begin Construction: Spring 2022', 'date': 'Spring 2022'}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'context': 'completed by Spring 2022.', 'date': 'Spring 2022'}, {'name': 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'context': '(cid:131) Complete Design: Spring 2022', 'date': 'Spring 2022'}]}

exec(code, env_args)

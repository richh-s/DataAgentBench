code = """import json
import re

with open(locals()['var_function-call-13241760497320549299'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-8006204082577017619'], 'r') as f:
    funding = json.load(f)

project_map = {p['Project_Name']: int(p['Amount']) for p in funding}
project_names = list(project_map.keys())

found_projects = set()
matches_debug = []

for doc in civic_docs:
    text = doc['text']
    
    # Find all matches
    all_matches = []
    for pname in project_names:
        idx = text.find(pname)
        if idx != -1:
            all_matches.append((idx, pname))
    
    # Filter to keep longest name at each index
    # But wait, "Latigo Canyon" (len 13) at index 100.
    # "Latigo Canyon ... (FEMA)" (len 30) at index 100.
    # If I have multiple matches starting at same index, pick longest.
    
    # Group by index
    by_index = {}
    for idx, pname in all_matches:
        if idx not in by_index:
            by_index[idx] = []
        by_index[idx].append(pname)
    
    final_matches = []
    for idx in sorted(by_index.keys()):
        # Sort names by length desc
        names = sorted(by_index[idx], key=len, reverse=True)
        longest_name = names[0]
        final_matches.append((idx, longest_name))
        
    # Now use final_matches to define segments
    for i in range(len(final_matches)):
        start_idx, pname = final_matches[i]
        
        if i < len(final_matches) - 1:
            end_idx = final_matches[i+1][0]
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        
        # Search for Begin Construction
        match = re.search("Begin Construction[:\\s]+([^\\n]+)", segment, re.IGNORECASE)
        if match:
            date_str = match.group(1)
            if "Spring 2022" in date_str or "March 2022" in date_str or "April 2022" in date_str or "May 2022" in date_str:
                if pname not in found_projects:
                    found_projects.add(pname)
                    matches_debug.append({"project": pname, "matched_date": date_str})

count = len(found_projects)
total_funding = sum(project_map[p] for p in found_projects)

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "matches": matches_debug}))"""

env_args = {'var_function-call-14343582955729451491': 'file_storage/function-call-14343582955729451491.json', 'var_function-call-8006204082577017619': 'file_storage/function-call-8006204082577017619.json', 'var_function-call-13241760497320549299': 'file_storage/function-call-13241760497320549299.json', 'var_function-call-857092213890831436': 5, 'var_function-call-7877463796089574449': {'count': 31, 'total_funding': 1642000, 'projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Storm Drain Master Plan (FEMA Project)', 'Corral Canyon Road Bridge Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Civic Center Stormwater Diversion Structure', 'Malibu Park Drainage Improvements', 'Encinal Canyon Road Drainage Improvements', 'Latigo Canyon Road Culvert Repairs', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project', 'Civic Center Way Improvements', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Birdview Avenue Improvements', 'Clover Heights Storm Drain', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Marie Canyon Green Streets', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Storm Drain Master Plan', 'Bluffs Park Shade Structure', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Birdview Avenue Improvements (CalOES Project)', '2021 Annual Street Maintenance', 'Clover Heights Storm Drain (FEMA Project)', 'Annual Street Maintenance', 'Trancas Canyon Park Planting and Irrigation Repairs']}, 'var_function-call-10711722631610373796': {'count': 10, 'total_funding': 549000, 'matches': [{'project': 'Marie Canyon Green Streets', 'matched_date': 'Spring 2022'}, {'project': 'Bluffs Park Shade Structure', 'matched_date': 'Spring 2022'}, {'project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'matched_date': 'Spring 2022'}, {'project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'matched_date': 'April 2022'}, {'project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'matched_date': 'Spring 2022'}, {'project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'matched_date': 'Spring 2022'}, {'project': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'matched_date': 'April 2022'}, {'project': 'Civic Center Water Treatment Facility Phase 2', 'matched_date': 'March 2022'}, {'project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'matched_date': 'Spring 2022'}, {'project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'matched_date': 'Spring 2022'}]}}

exec(code, env_args)

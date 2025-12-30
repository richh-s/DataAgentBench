code = """import json
import re

with open(locals()['var_function-call-13241760497320549299'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-8006204082577017619'], 'r') as f:
    funding = json.load(f)

project_map = {p['Project_Name']: int(p['Amount']) for p in funding}
project_names = list(project_map.keys())

found_projects = set()

# Debugging list
matches_debug = []

for doc in civic_docs:
    text = doc['text']
    
    # Find all project positions
    proj_positions = []
    for pname in project_names:
        idx = text.find(pname)
        if idx != -1:
            proj_positions.append((idx, pname))
    
    # Sort by position
    proj_positions.sort()
    
    # Iterate and define segments
    for i in range(len(proj_positions)):
        start_idx, pname = proj_positions[i]
        # End at next project or end of text
        if i < len(proj_positions) - 1:
            end_idx = proj_positions[i+1][0]
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

env_args = {'var_function-call-14343582955729451491': 'file_storage/function-call-14343582955729451491.json', 'var_function-call-8006204082577017619': 'file_storage/function-call-8006204082577017619.json', 'var_function-call-13241760497320549299': 'file_storage/function-call-13241760497320549299.json', 'var_function-call-857092213890831436': 5, 'var_function-call-7877463796089574449': {'count': 31, 'total_funding': 1642000, 'projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Storm Drain Master Plan (FEMA Project)', 'Corral Canyon Road Bridge Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Civic Center Stormwater Diversion Structure', 'Malibu Park Drainage Improvements', 'Encinal Canyon Road Drainage Improvements', 'Latigo Canyon Road Culvert Repairs', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project', 'Civic Center Way Improvements', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Birdview Avenue Improvements', 'Clover Heights Storm Drain', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Marie Canyon Green Streets', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Storm Drain Master Plan', 'Bluffs Park Shade Structure', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Birdview Avenue Improvements (CalOES Project)', '2021 Annual Street Maintenance', 'Clover Heights Storm Drain (FEMA Project)', 'Annual Street Maintenance', 'Trancas Canyon Park Planting and Irrigation Repairs']}}

exec(code, env_args)

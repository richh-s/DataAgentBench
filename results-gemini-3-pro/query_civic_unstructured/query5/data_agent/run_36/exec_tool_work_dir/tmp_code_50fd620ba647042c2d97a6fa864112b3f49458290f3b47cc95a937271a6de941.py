code = """import json
import re

funding_file_path = locals()['var_function-call-7345581642634636200']
civic_docs_file_path = locals()['var_function-call-13795452578231862592']

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}
project_names = list(funding_map.keys())

# Regex for start date - stop at newline
# Using [^\n]+ to capture until newline
date_pattern = re.compile(r'(Begin Construction|Advertise|Start Date|Construction started)[:\s]+([^\n]+)', re.IGNORECASE)

matched_projects = {}

for doc in civic_docs:
    text = doc['text']
    
    project_indices = []
    for pname in project_names:
        start = 0
        while True:
            idx = text.find(pname, start)
            if idx == -1:
                break
            project_indices.append((idx, pname))
            start = idx + 1
            
    project_indices.sort()
    
    for i, (idx, pname) in enumerate(project_indices):
        if i + 1 < len(project_indices):
            end_idx = project_indices[i+1][0]
        else:
            end_idx = len(text)
        
        segment = text[idx:end_idx]
        
        is_disaster = False
        if any(suffix in pname for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)', '(CalJPIA/FEMA Project)', '(FEMA/CalOES Project)', '(FEMA)']):
            is_disaster = True
        
        if is_disaster:
            started_2022 = False
            dates = date_pattern.findall(segment)
            for action, date_str in dates:
                if "2022" in date_str:
                     # Double check action just in case
                     if any(x in action.lower() for x in ["begin construction", "advertise", "start date", "construction started"]):
                        started_2022 = True
                        break
            
            if started_2022:
                matched_projects[pname] = funding_map[pname]

total_funding = sum(matched_projects.values())

print("__RESULT__:")
print(json.dumps({
    "matched_projects": list(matched_projects.keys()),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-7345581642634636200': 'file_storage/function-call-7345581642634636200.json', 'var_function-call-13795452578231862592': 'file_storage/function-call-13795452578231862592.json', 'var_function-call-10640987408951217709': {'matched_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)'], 'total_funding': 1175000}, 'var_function-call-18230766214598277346': ['Latigo Canyon Road Culvert Repairs', 'Guardrail Replacement Citywide', 'Storm Drain Master Plan', 'Birdview Avenue Improvements', 'PCH Signal Synchronization System Improvements Project', 'Civic Center Way Improvements', 'Westward Beach Road Improvements Project', '2021 Annual Street Maintenance', 'Marie Canyon Green Streets', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Encinal Canyon Road Drainage Improvements', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Malibu Park Drainage Improvements', 'Corral Canyon Road Bridge Repairs', 'Trancas Playground Resurfacing', 'Legacy Park Paver Repair Project', 'Annual Street Maintenance', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Malibu Road Slope Repairs', 'Bluffs Park Shade Structure', 'PCH Median Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Malibu Bluffs Park South Walkway', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'Trancas Canyon Park Slope Stabilization Project'], 'var_function-call-159456767394318242': {'matched_projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)'], 'total_funding': 568000}}

exec(code, env_args)

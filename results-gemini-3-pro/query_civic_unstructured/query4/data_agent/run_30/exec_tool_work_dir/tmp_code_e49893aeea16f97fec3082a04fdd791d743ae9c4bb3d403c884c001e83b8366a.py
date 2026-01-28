code = """import json

with open(locals()['var_function-call-8238280487498580574'], 'r') as f:
    funding_data = json.load(f)

found_projects = [
    "Trancas Canyon Park Planting and Irrigation Repairs",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements",
    "Trancas Canyon Park Slope Stabilization Project",
    "Encinal Canyon Road Drainage Improvements",
    "Latigo Canyon Road Culvert Repairs",
    "Marie Canyon Green Streets",
    "Bluffs Park Shade Structure",
    "Broad Beach Road Water Quality Infrastructure Repairs",
    "Civic Center Water Treatment Facility Phase 2"
]

total_funding = 0

for fp in found_projects:
    for item in funding_data:
        name = item['Project_Name']
        if name == fp or name.startswith(fp + " ("):
            total_funding += int(item['Amount'])

result = {
    "project_count": len(found_projects),
    "total_funding": total_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8238280487498580574': 'file_storage/function-call-8238280487498580574.json', 'var_function-call-8238280487498581651': 'file_storage/function-call-8238280487498581651.json', 'var_function-call-6947653279821994463': {'project_count': 9, 'projects': ['Trancas Canyon Park Planting and Irrigation Repairs', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Trancas Canyon Park Slope Stabilization Project', 'Encinal Canyon Road Drainage Improvements', 'Latigo Canyon Road Culvert Repairs', 'Marie Canyon Green Streets', 'Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Civic Center Water Treatment Facility Phase 2'], 'total_funding': 459000}, 'var_function-call-9436239953568858208': {'Trancas Canyon Park Planting and Irrigation Repairs': ['Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)'], 'Latigo Canyon Road Roadway/Retaining Wall Improvements': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)'], 'Trancas Canyon Park Slope Stabilization Project': ['Trancas Canyon Park Slope Stabilization Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)'], 'Encinal Canyon Road Drainage Improvements': ['Encinal Canyon Road Drainage Improvements', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)'], 'Latigo Canyon Road Culvert Repairs': ['Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'], 'Marie Canyon Green Streets': ['Marie Canyon Green Streets'], 'Bluffs Park Shade Structure': ['Bluffs Park Shade Structure'], 'Broad Beach Road Water Quality Infrastructure Repairs': ['Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'], 'Civic Center Water Treatment Facility Phase 2': ['Civic Center Water Treatment Facility Phase 2']}}

exec(code, env_args)

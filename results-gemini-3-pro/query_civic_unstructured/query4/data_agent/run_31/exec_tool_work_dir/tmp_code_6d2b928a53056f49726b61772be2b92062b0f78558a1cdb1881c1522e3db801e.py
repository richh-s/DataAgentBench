code = """import json
import re

path_funding = locals()['var_function-call-8803859908455603463']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

identified_names = locals()['var_function-call-10233603179972647313']

def normalize(name):
    # Remove (...) at the end
    # e.g. "Name (FEMA Project)" -> "Name"
    # But be careful not to remove essential parts?
    # Suffixes seem to be source related.
    return re.sub(r'\s*\(.*Project.*\)', '', name).strip()
    # Or just remove any parenthesis at end?
    # Some names might be "Project (Phase 2)". "Phase 2" is part of project identity.
    # The hint says: "Disaster project names often include suffixes like '(FEMA Project)', '(CalJPIA Project)', or '(CalOES Project)'."
    # I should target those.

def normalize_strict(name):
    name = re.sub(r'\s*\(FEMA.*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES.*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA.*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(FEMA/CalOES.*\)', '', name, flags=re.IGNORECASE)
    # Also generic "(... Project)"
    # Let's remove any parens containing "Project"
    name = re.sub(r'\s*\([^)]*Project[^)]*\)', '', name, flags=re.IGNORECASE)
    return name.strip()

started_project_bases = set()
for name in identified_names:
    started_project_bases.add(normalize_strict(name))

# Count
num_projects = len(started_project_bases)

# Sum funding
total_funding = 0
for record in funding_data:
    pname = record['Project_Name']
    base = normalize_strict(pname)
    if base in started_project_bases:
        total_funding += int(record['Amount'])

print('__RESULT__:')
print(json.dumps({"count": num_projects, "total_funding": total_funding, "projects": list(started_project_bases)}))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json', 'var_function-call-4031632959131545213': ['scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'damaged by the Woolsey Fire.', 'beginning in April 2022.', 'March 2022', 'beginning in Spring 2022.', '(cid:131) The project consultant has started the design of this project.', 'assessment district will be created.', 'advertised for construction bids shortly after this date.', 'timber with non-combustible materials.', 'Fire.', '(cid:131) Next public community meeting is scheduled for March 25th.', 'is finalizing the bid documents.', 'that was damaged by the Woolsey Fire.', 'Metro.'], 'var_function-call-2765771842290335904': [], 'var_function-call-1028562691190283738': 'Done', 'var_function-call-2831729942517060244': {'db_names_sample': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements'], 'marker_count': 268, 'snippet': 'mer 2023\n(cid:131) Begin Construction: Fall 2023\n\nLatigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have been completed\n(cid:131) Awaiting final FEMA/CalOES approval for scope modification\n\n(cid:'}, 'var_function-call-12524213056519618730': ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'], 'var_function-call-10233603179972647313': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'PCH at Trancas Canyon Road Right Turn Lane', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Marie Canyon Green Streets']}

exec(code, env_args)

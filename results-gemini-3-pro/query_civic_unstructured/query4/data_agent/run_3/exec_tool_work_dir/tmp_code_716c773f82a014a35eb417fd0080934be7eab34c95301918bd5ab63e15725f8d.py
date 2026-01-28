code = """import json
import difflib

# Load Funding Table
funding_file = locals()['var_function-call-7462164871944196063']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extracted projects
extracted_list = [
    "Marie Canyon Green Streets", 
    "shade structures at Malibu Bluffs Park.", 
    "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)", 
    "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)", 
    "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)", 
    "Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)", 
    "Latigo Canyon Road Culvert Repairs (FEMA Project)", 
    "Civic Center Water Treatment Facility Phase 2", 
    "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)", 
    "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)"
]
# I removed duplicates and obvious garbage manually for the list definition, 
# but I should check "damaged by the Woolsey Fire." is garbage. Yes.

# Mapping "shade structures..." to "Bluffs Park Shade Structure"
# I will try to match automatically or manually.
# Manual mapping for the known issue:
name_corrections = {
    "shade structures at Malibu Bluffs Park.": "Bluffs Park Shade Structure"
}

# Create a dictionary for funding lookup: Name -> Amount
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

found_projects = []
total_funding = 0

for name in extracted_list:
    target_name = name_corrections.get(name, name)
    
    if target_name in funding_map:
        found_projects.append(target_name)
        total_funding += funding_map[target_name]
    else:
        # Try fuzzy match if not found?
        # But most seem exact matches based on the format.
        # "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)"
        # Let's check if it exists in funding_map
        pass

print('__RESULT__:')
print(json.dumps({"count": len(found_projects), "total_funding": total_funding, "projects": found_projects}))"""

env_args = {'var_function-call-11551916714829244463': 'file_storage/function-call-11551916714829244463.json', 'var_function-call-11551916714829245086': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13876112048585230110': 'file_storage/function-call-13876112048585230110.json', 'var_function-call-15823956005309354737': ['Marie Canyon Green Streets', 'shade structures at Malibu Bluffs Park.', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Civic Center Water Treatment Facility Phase 2', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'shade structures at Malibu Bluffs Park.', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'damaged by the Woolsey Fire.'], 'var_function-call-7462164871944196063': 'file_storage/function-call-7462164871944196063.json'}

exec(code, env_args)

code = """import json
import difflib

# Load data
with open(locals()['var_function-call-2334395091731137035'], 'r') as f:
    funding_data = json.load(f)

found_projects = json.loads(locals()['var_function-call-2342195948270717268'])

# Create a clean lookup for funding
# We will use a dictionary: Name -> Amount
# But wait, there might be duplicate names? 
# In the preview, names looked unique per ID, but let's check.
funding_lookup = {}
all_funding_names = []
for entry in funding_data:
    name = entry['Project_Name'].strip()
    amount = int(entry['Amount'])
    funding_lookup[name] = amount
    all_funding_names.append(name)

# manual mapping for noisy names
manual_map = {
    "shade structures at Malibu Bluffs Park.": "Bluffs Park Shade Structure",
    "Marie Canyon Green Streets": "Marie Canyon Green Streets", # Exact
    "Civic Center Water Treatment Facility Phase 2": "Civic Center Water Treatment Facility Phase 2" # Exact
}

total_funding = 0
count_projects = 0
matched_projects = []

for p in found_projects:
    raw_name = p['Project_Name'].strip()
    
    # Filtering noise
    if "Agenda Item" in raw_name or "Woolsey Fire" in raw_name and "Project" not in raw_name:
        continue
    
    # Try exact match
    match_name = None
    if raw_name in funding_lookup:
        match_name = raw_name
    elif raw_name in manual_map:
        mapped = manual_map[raw_name]
        if mapped in funding_lookup:
            match_name = mapped
    
    # Fuzzy match if not found
    if not match_name:
        # Try to find closest match in funding names
        # We need a high cutoff to avoid bad matches
        matches = difflib.get_close_matches(raw_name, all_funding_names, n=1, cutoff=0.8)
        if matches:
            match_name = matches[0]
            
    if match_name:
        amount = funding_lookup[match_name]
        total_funding += amount
        count_projects += 1
        matched_projects.append({"Raw": raw_name, "Matched": match_name, "Amount": amount})
    else:
        # If no match found, maybe print it to see if we missed something
        matched_projects.append({"Raw": raw_name, "Matched": "NO MATCH", "Amount": 0})

print("__RESULT__:")
print(json.dumps({"count": count_projects, "total_funding": total_funding, "details": matched_projects}))"""

env_args = {'var_function-call-3266784049698579057': 'file_storage/function-call-3266784049698579057.json', 'var_function-call-3266784049698579578': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-2334395091731140458': 'file_storage/function-call-2334395091731140458.json', 'var_function-call-2334395091731137035': 'file_storage/function-call-2334395091731137035.json', 'var_function-call-2342195948270717268': [{'Project_Name': 'Marie Canyon Green Streets', 'st': 'Spring 2022'}, {'Project_Name': 'shade structures at Malibu Bluffs Park.', 'st': 'Spring 2022'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'st': 'April 2022'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Agenda Item # 4.A.', 'st': 'April 2022'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'st': 'March 2022'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'st': 'Spring 2022'}, {'Project_Name': 'damaged by the Woolsey Fire.', 'st': 'Spring 2022'}]}

exec(code, env_args)

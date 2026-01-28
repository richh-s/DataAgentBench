code = """import json

# Load previous result
prev_res = json.loads("""{"total_funding": 568000, "projects": ["Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)", "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)", "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)", "Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)", "Clover Heights Storm Drain (FEMA Project)", "Latigo Canyon Road Culvert Repairs (FEMA Project)", "Malibu Road Slope Repairs (CalOES Project)", "Westward Beach Road Shoulder Repairs (CalOES Project)", "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)", "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)"], "records": ["Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)", "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)", "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)", "Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)", "Clover Heights Storm Drain (FEMA Project)", "Latigo Canyon Road Culvert Repairs (FEMA Project)", "Malibu Road Slope Repairs (CalOES Project)", "Westward Beach Road Shoulder Repairs (CalOES Project)", "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)", "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)"]}""")

found_projects = prev_res['projects']

# Load funding data
with open(locals()['var_function-call-7842478251555825611'], 'r') as f:
    funding_data = json.load(f)

# Calculate Base Names
base_names = set()
for p in found_projects:
    # Split by ' (' to strip suffix
    base = p.split(' (')[0]
    base_names.add(base)

# Sum funding for all records matching base names
processed_ids = set()
total_funding = 0
matched_records = []

for record in funding_data:
    r_name = record['Project_Name']
    r_id = record['Funding_ID']
    r_amt = int(record['Amount'])
    
    # Check if r_name belongs to any base name
    # Logic: r_name IS base OR r_name STARTSWITH base + " ("
    for base in base_names:
        if r_name == base or r_name.startswith(base + " ("):
            if r_id not in processed_ids:
                total_funding += r_amt
                processed_ids.add(r_id)
                matched_records.append(r_name)
            break # Already matched this record

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_records": matched_records}))"""

env_args = {'var_function-call-7842478251555825910': 'file_storage/function-call-7842478251555825910.json', 'var_function-call-7842478251555825611': 'file_storage/function-call-7842478251555825611.json', 'var_function-call-8008446632726579032': {'total_funding': 568000, 'projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)'], 'records': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)']}}

exec(code, env_args)

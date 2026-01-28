code = """import json

# Load disaster-related funding records
disaster_funding_var = locals()['var_functions.query_db:96']
disaster_funding = []
if isinstance(disaster_funding_var, str) and disaster_funding_var.endswith('.json'):
    with open(disaster_funding_var, 'r') as f:
        disaster_funding = json.load(f)
else:
    disaster_funding = list(disaster_funding_var) if disaster_funding_var else []

# Load civic documents (full data)
civic_docs_var = locals()['var_functions.query_db:97']
civic_docs = []
if isinstance(civic_docs_var, str) and civic_docs_var.endswith('.json'):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(civic_docs_var) if civic_docs_var else []

# Build funding lookup table
funding_lookup = {}
for rec in disaster_funding:
    proj_name = rec.get('Project_Name', '').strip()
    amount_str = rec.get('Amount', '0')
    if proj_name and amount_str:
        try:
            amount = int(amount_str)
            funding_lookup[proj_name] = amount
        except:
            pass

print(f"Found {len(funding_lookup)} disaster-related funding records")
print(f"Found {len(civic_docs)} civic documents")

# Test: Look for 2022 Morning View project details
morning_view_funding = 0
morning_view_name = "2022 Morning View Resurfacing & Storm Drain Improvements"
if morning_view_name in funding_lookup:
    morning_view_funding = funding_lookup[morning_view_name]
    print(f"Found funding for {morning_view_name}: ${morning_view_funding}")

# Check if this appears in civic docs
for doc in civic_docs:
    text = doc.get('text', '')
    if morning_view_name in text:
        print(f"Found {morning_view_name} in civic document: {doc.get('filename')}")
        # Look for disaster markers
        if '(FEMA' in text or '(CalOES' in text or '(CalJPIA' in text:
            print("  Document contains disaster-related projects")

# Look for any disaster projects specifically with 2022 in the name
disaster_2022_projects = {}
for proj_name, amount in funding_lookup.items():
    if '2022' in proj_name:
        disaster_2022_projects[proj_name] = amount
        print(f"2022 Disaster project: {proj_name} = ${amount}")

print(f"\nTotal of {len(disaster_2022_projects)} disaster projects with 2022 in name")
print(f"Total funding for these: ${sum(disaster_2022_projects.values())}")

result = {
    'disaster_2022_count': len(disaster_2022_projects),
    'disaster_2022_total': sum(disaster_2022_projects.values()),
    'projects': disaster_2022_projects
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:47': 'file_storage/functions.query_db:47.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:70': {'total_funding': 0, 'project_count': 0, 'projects': []}, 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:73': [], 'var_functions.query_db:76': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.query_db:81': 'file_storage/functions.query_db:81.json', 'var_functions.execute_python:90': {'loaded': True, 'funding_count': 500}, 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.execute_python:93': {'num_civic_docs': 5, 'num_funding_recs': 500, 'funding_lookup_size': 500}, 'var_functions.query_db:96': [], 'var_functions.query_db:97': 'file_storage/functions.query_db:97.json'}

exec(code, env_args)

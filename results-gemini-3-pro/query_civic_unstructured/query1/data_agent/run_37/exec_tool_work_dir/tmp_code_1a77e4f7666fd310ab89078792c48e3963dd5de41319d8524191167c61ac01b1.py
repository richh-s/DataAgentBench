code = """import json

funding_file_path = locals()['var_function-call-2838577088197188033']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

keywords = ["morning", "westward", "slope", "water", "treatment", "civic"]

potential_matches = []
for entry in funding_data:
    name = entry['Project_Name']
    amount = int(entry['Amount'])
    if any(k in name.lower() for k in keywords):
        potential_matches.append((name, amount))

print("__RESULT__:")
print(json.dumps(potential_matches))"""

env_args = {'var_function-call-2838577088197188033': 'file_storage/function-call-2838577088197188033.json', 'var_function-call-2838577088197188526': 'file_storage/function-call-2838577088197188526.json', 'var_function-call-7878716980368608955': ['civic_docs'], 'var_function-call-11182446621266237343': 'file_storage/function-call-11182446621266237343.json', 'var_function-call-11192819882122169413': {'count': 12, 'matches': ['Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Bluffs Park South Walkway', 'Birdview Avenue Improvements (CalOES Project)', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Clover Heights Storm Drain', 'Storm Drain Master Plan', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'Outdoor Warning Signs', 'Trancas Canyon Park Playground Resurfacing'], 'unmatched': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'and rejected all bids due to a budget shortfall', 'or phasing out the project', 'Westward Beach Road Repair Project', 'comments mid-April. This project required their review since the project', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'cleared the project.', 'to finalize plans and specifications', 'been finalized and incorporated into GIS.', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Resources review for the SRF funding application', 'schedule will be developed upon the completion of the Cultural', 'Resources review.', 'the Spring 2023.', 'Commission meeting for project direction due to concerns regarding', 'sirens height and feedback from residents and the community.', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'feasible traffic safety improvements can be constructed at this location.', 'City will be issuing a RFQ/P for design services in the summer of 2023']}, 'var_function-call-8514923340229520344': {'count': 12, 'pairs': [['PCH Median Improvements Project', 'PCH Median Improvements Project'], ['Westward Beach Road Drainage Improvements Project', 'Westward Beach Road Drainage Improvements Project'], ['Clover Heights Storm Drainage Improvements', 'Clover Heights Storm Drain'], ['Latigo Canyon Road Retaining Wall Repair Project', 'Latigo Canyon Road Retaining Wall Repair Project'], ['Storm Drain Master Plan', 'Storm Drain Master Plan'], ['Permanent Skate Park', 'Permanent Skate Park'], ['project', 'Birdview Avenue Improvements (CalOES Project)'], ['PCH at Trancas Canyon Road Right Turn Lane', 'PCH at Trancas Canyon Road Right Turn Lane'], ['Outdoor Warning Signs', 'Outdoor Warning Signs'], ['Malibu Bluffs Park South Walkway Repairs', 'Malibu Bluffs Park South Walkway Repairs'], ['Trancas Canyon Park Playground', 'Trancas Canyon Park Playground Resurfacing'], ['Malibu Canyon Road Traffic Study', 'Malibu Canyon Road Traffic Study']]}}

exec(code, env_args)

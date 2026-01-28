code = """import json

# Load funding data
with open(locals()['var_function-call-14381109173196317470'], 'r') as f:
    funding_data = json.load(f)

funding_names = [item['Project_Name'] for item in funding_data]

# Search queries
queries = [
    "Morning View",
    "Water Treatment",
    "Trancas Canyon Park Slope",
    "project_8"
]

results = {}
for q in queries:
    matches = [name for name in funding_names if q.lower() in name.lower()]
    results[q] = matches

# Also check exact amount for project_8
p8 = next((item for item in funding_data if item['Project_Name'] == 'project_8'), None)

print("__RESULT__:")
print(json.dumps({"matches": results, "project_8_data": p8}))"""

env_args = {'var_function-call-14381109173196317470': 'file_storage/function-call-14381109173196317470.json', 'var_function-call-14381109173196319441': 'file_storage/function-call-14381109173196319441.json', 'var_function-call-3599675758928509690': 'file_storage/function-call-3599675758928509690.json', 'var_function-call-7727963684795353611': 10, 'var_function-call-7768305805941479735': 'file_storage/function-call-7768305805941479735.json', 'var_function-call-14396097720879051946': 'file_storage/function-call-14396097720879051946.json', 'var_function-call-13789292492221773073': {'count': 13, 'matched': ['PCH Median Improvements Project', 'Trancas Canyon Park Playground (substr: Trancas Canyon Park Playground Resurfacing)', 'Westward Beach Road Drainage Improvements Project', 'Permanent Skate Park', 'Malibu Canyon Road Traffic Study', 'project (fuzzy: project_8)', 'Malibu Bluffs Park South Walkway Repairs', 'Outdoor Warning Signs', 'Latigo Canyon Road Retaining Wall Repair Project', 'Westward Beach Road Repair Project (fuzzy: Westward Beach Road Shoulder Repairs (CalOES Project))', 'Clover Heights Storm Drainage Improvements (substr: Clover Heights Storm Drain)', 'Storm Drain Master Plan', 'PCH at Trancas Canyon Road Right Turn Lane'], 'unmatched': ['and rejected all bids due to a budget shortfall', 'City will be issuing a RFQ/P for design services in the summer of 2023', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'feasible traffic safety improvements can be constructed at this location.', 'or phasing out the project', 'cleared the project.', 'the Spring 2023.', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Resources review for the SRF funding application', 'sirens height and feedback from residents and the community.', 'schedule will be developed upon the completion of the Cultural', 'Civic Center Water Treatment Facility Phase 2', 'to finalize plans and specifications', 'been finalized and incorporated into GIS.', 'Resources review.', 'Commission meeting for project direction due to concerns regarding', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'project and will submit to the County for review.', 'comments mid-April. This project required their review since the project']}}

exec(code, env_args)

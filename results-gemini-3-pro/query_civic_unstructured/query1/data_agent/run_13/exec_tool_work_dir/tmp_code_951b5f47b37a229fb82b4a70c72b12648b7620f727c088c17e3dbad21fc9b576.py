code = """import json

# Get file paths from local variables
funding_path = locals()['var_function-call-2725984221883882111']

# Load Funding Data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funded_projects = {}
for item in funding_data:
    try:
        amt = float(item.get('Amount', 0))
        if amt > 50000:
            funded_projects[item['Project_Name']] = amt
    except ValueError:
        continue

keywords = ["Morning", "Westward", "Clover", "Trancas", "Civic"]
matches = []
for name in funded_projects:
    for k in keywords:
        if k in name:
            matches.append(name)

matches = sorted(list(set(matches)))
print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_function-call-2725984221883880881': ['Funding'], 'var_function-call-2725984221883881496': ['civic_docs'], 'var_function-call-2725984221883882111': 'file_storage/function-call-2725984221883882111.json', 'var_function-call-2725984221883882726': 'file_storage/function-call-2725984221883882726.json', 'var_function-call-1453355728292058709': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-15427466270111541878': 1, 'var_function-call-18115326973790218237': {'count': 9, 'projects': ['Malibu Bluffs Park South Walkway Repairs', 'Westward Beach Road Drainage Improvements Project', 'Outdoor Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Canyon Road Traffic Study', 'PCH Median Improvements Project', 'Storm Drain Master Plan', 'Permanent Skate Park', 'Latigo Canyon Road Retaining Wall Repair Project'], 'candidates': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'and rejected all bids due to a budget shortfall', 'or phasing out the project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'comments mid-April. This project required their review since the project', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'cleared the project.', 'Clover Heights Storm Drainage Improvements', 'to finalize plans and specifications', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'been finalized and incorporated into GIS.', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Resources review for the SRF funding application', 'schedule will be developed upon the completion of the Cultural', 'Resources review.', 'Permanent Skate Park', 'project', 'PCH at Trancas Canyon Road Right Turn Lane', 'the Spring 2023.', 'Outdoor Warning Signs', 'Commission meeting for project direction due to concerns regarding', 'sirens height and feedback from residents and the community.', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'feasible traffic safety improvements can be constructed at this location.', 'City will be issuing a RFQ/P for design services in the summer of 2023']}}

exec(code, env_args)

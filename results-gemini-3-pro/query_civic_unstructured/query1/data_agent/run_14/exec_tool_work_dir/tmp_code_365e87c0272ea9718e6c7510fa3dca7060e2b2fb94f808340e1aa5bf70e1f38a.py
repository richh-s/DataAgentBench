code = """import json

with open(locals()['var_function-call-14769478683806682002'], 'r') as f:
    funding_data = json.load(f)

keywords = ["Morning View", "Westward", "Trancas", "Civic Center"]
hits = []

for item in funding_data:
    name = item['Project_Name']
    for k in keywords:
        if k.lower() in name.lower():
            hits.append(item)

print("__RESULT__:")
print(json.dumps(hits))"""

env_args = {'var_function-call-14769478683806682002': 'file_storage/function-call-14769478683806682002.json', 'var_function-call-14769478683806682871': 'file_storage/function-call-14769478683806682871.json', 'var_function-call-602477253164993976': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-11227068865765284835': {'matches': ['PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study'], 'extracted_names': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Median Improvements Project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'Clover Heights Storm Drainage Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study', 'feasible traffic safety improvements can be constructed at this location.'], 'count': 9}, 'var_function-call-8128620880073992273': [{'extracted': 'Clover Heights Storm Drainage Improvements', 'funding_name': 'Clover Heights Storm Drain', 'amount': 53000.0}, {'extracted': 'Trancas Canyon Park Playground', 'funding_name': 'Trancas Canyon Park Playground Resurfacing', 'amount': 65000.0}]}

exec(code, env_args)
